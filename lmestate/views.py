from django.shortcuts import render, redirect
from .models import *
from . forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import CreateView
# Create your views here.
from django.db.models import Count


def home(request):
    q = request.POST.get('q' or None)
    if q:
        properties=Property.objects.filter(Q(status__icontains=q) | Q(property_location__icontains=q)).order_by("-date_posted")
    else:
        properties=Property.objects.all().order_by("-date_posted")
    agency = Agency.objects.all()[:3]

    paginator = Paginator(properties, 4)
    page = request.GET.get('page')
    property_list = paginator.get_page(page)

    context={
        "property_list": property_list,
        "agency": agency,
        # "q": q,
    }
    return render(request, 'index.html', context)



def base(request):
    return render(request, "home.html")


def agentList(request, pk):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form= form.save(commit=False)
            form.agency = Agency.objects.get(id=pk)
            form.save()
            return redirect('agent-list', pk=pk)
    form = PropertyForm()
    if request.user.is_authenticated:
        try:
            agency = Agency.objects.get(id=pk, agent=request.user)
            agency_property=Property.objects.filter(agency=agency)
            enquiry=[i.agency_property_enquiry for i in agency_property]
            for b in enquiry:
                for i in b:
                    print(i)
        except Agency.DoesNotExist:
            return redirect("home")
    else:
        return redirect('home')

    context={
        "property_list": agency_property,
        "agency": agency,
        "form": form,
        "enquiries":enquiry,
    }
    return render(request, 'agent-list.html', context)


def address(request):
    if request.method=="POST":
        add_form = AddressForm(request.POST)
        if add_form.is_valid():
            add_form=add_form.save(commit=False)
            add_form.user=request.user
            add_form.save()
            return redirect("create-agency")
    add_form=AddressForm()
    context = {
        "add_form": add_form,
    }
    return render(request, 'address.html', context)


def agencycreate(request):
    address= Address.objects.get(user=request.user)
    if address is None:
        return redirect("address")
    if request.method=="POST":
        agency_form = CreateAgency(request.POST, request.FILES)
        if agency_form.is_valid():
            agency_form=agency_form.save(commit=False)
            agency_form.agent=request.user
            agency_form.agent_location=address
            agency_form.save()
            return redirect('home')
    agency_form=CreateAgency()
    context={
        "agency_form":agency_form,
    }
    return render(request, 'agencycreate.html', context)


def estate_detail(request, property_id):
    property_detail = Property.objects.get(property_id=property_id)
    images = ImageModel.objects.filter(property=property_detail)

    if request.method == "POST":
        enquiry_form = EnquiryForm(request.POST)
        if enquiry_form.is_valid():
            enquiry_form= enquiry_form.save(commit=False)
            enquiry_form.property = property_detail
            enquiry_form.save()
            return redirect('home')
    enquiry_form = EnquiryForm()
    context={
        "property_detail":property_detail,
        "form": enquiry_form,
        "images": images,
    }
    return render(request, 'estate_detail.html', context)


def property_images_add(request, id):
    form = PropertyImageUploadForm()
    property = Property.objects.get(id=id)
    images = ImageModel.objects.filter(property=property)
    total=0
    for image in images:
        total +=1
    print(f"{total} images for {property}")

    if request.method=="POST":
        form = PropertyImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.property=property
            form.save()
            return redirect("add-properties", id)      
    context={
        "images": property,
        "form": form,
    }
    return render(request, 'text.html', context)
