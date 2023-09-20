from django.shortcuts import render, redirect
from .models import *
from . forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.lorem_ipsum import paragraphs
from django.contrib import messages
# from django.views.generic import CreateView
# Create your views here.


def home(request):
    agency = None
    q = request.POST.get('q' or None)
    if q:
        properties=Property.objects.filter(Q(status__icontains=q) | Q(property_location__icontains=q)).order_by("-date_posted")
    else:
        properties=Property.objects.all().order_by("-date_posted")
    if request.user.is_authenticated:
        request.session.keys=request.user
        agency = Agency.objects.filter(agent=request.session.keys).first()

    else:
        agency=Agency.objects.none()
    paginator = Paginator(properties, 12)
    page = request.GET.get('page')
    property_list = paginator.get_page(page)

    context={
        "property_list": property_list,
        "agency": agency,
    }
    # print(paragraphs(5)[0])
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
            messages.info(request, "property listed")
            return redirect('agent-list', pk=pk)
    form = PropertyForm()
    if request.user.is_authenticated:
        try:
            agency = Agency.objects.get(id=pk, agent=request.user)
            agency_property=Property.objects.filter(agency=agency)
            enquiry=[i.agency_property_enquiry for i in agency_property]
            property_count = agency.property_set.count()
            # print(property_count)
        except Agency.DoesNotExist:
            return redirect("home")
    else:
        return redirect('home')

    context={
        "property_list": agency_property,
        "agency": agency,
        "form": form,
        "enquiries":enquiry,
        "property_count":property_count,
    }

    return render(request, 'agent-list.html', context)


def address(request):
    if request.method=="POST":
        add_form = AddressForm(request.POST)
        if add_form.is_valid():
            add_form=add_form.save(commit=False)
            add_form.user=request.user
            add_form.save()
            messages.success(request, "your location has been set")
            return redirect("create-agency")
    add_form=AddressForm()
    context = {
        "add_form": add_form,
    }
    return render(request, 'address.html', context)


def agencycreate(request):
    address= Address.objects.get(user=request.user)
    agency = Agency.objects.filter(agent=request.user)
    if address is None:
        messages.info(request, "add a location address")
        return redirect("address")

    if request.method=="POST":
        agency_form = CreateAgency(request.POST, request.FILES)
        if agency_form.is_valid():
            instance=agency_form.save(commit=False)
            instance.agent=request.user
            if agency.exists():
                messages.info(request, "This owner already has an agency")
                return redirect('home')
            instance.agent_location=address
            instance.save()
            messages.success(request, "agency registered")
            return redirect('home')
    instance=CreateAgency()
    context={
        "agency_form":instance,
    }
    return render(request, 'agencycreate.html', context)


def estate_detail(request, property_id):
    property_detail = Property.objects.get(property_id=property_id)
    images = ImageModel.objects.filter(property=property_detail)
    images_count=images.count()

    if request.method == "POST":
        enquiry_form = EnquiryForm(request.POST)
        if enquiry_form.is_valid():
            enquiry_form= enquiry_form.save(commit=False)
            enquiry_form.property = property_detail
            enquiry_form.save()
            messages.info(request, "offer sent")
            return redirect('home')
    enquiry_form = EnquiryForm()
    context={
        "property_detail":property_detail,
        "form": enquiry_form,
        "images": images,
        "images_count":images_count,
    }
    return render(request, 'estate_detail.html', context)


def property_images_add(request, id):
    form = PropertyImageUploadForm()
    property = Property.objects.get(id=id)
    # images = ImageModel.objects.filter(property=property)
    # total=0
    # for image in images:
    #     total +=1
    # print(f"{total} images for {property}")

    if request.method=="POST":
        form = PropertyImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.property=property
            form.save()
            messages.info(request, "property image added. have more?")
            return redirect("add-properties", id)      
    context={
        "images": property,
        "form": form,
    }
    return render(request, 'text.html', context)


def edit_property_detail(request, id):
    queryset = Property.objects.get(id=id)
    if request.method=="GET":
        form = PropertyForm(instance=queryset)
        context = {
            'form': form,
        }
        return render(request, "edit_property_detail.html", context)
    elif request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the following errors:')
            context = {
                'form': form,
            }
            return render(request, "edit_property_detail.html", context)


def deleteImage(request, id):
    images = ImageModel.objects.get(id=id)
    if request.method=="POST":
        images.delete()
        return redirect("home")

