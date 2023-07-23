from django.shortcuts import render, redirect
from .models import *
from . forms import PropertyForm
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    agency = Agency.objects.all()[:3]
    properties=Property.objects.all().order_by("-date_posted")
    # gency = Agency.objects.get(agent = request.user)
    # propertiies = Property.objects.get(agency = gency)
    # image = propertiies.image.all()
    # print(image.url)
    paginator = Paginator(properties, 4)
    page = request.GET.get('page')
    property_list = paginator.get_page(page)

    context={
        "property_list": property_list,
        "agency": agency,
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
    try:
        agency = Agency.objects.get(id=pk, agent=request.user)
        agency_property=Property.objects.filter(agency=agency)
    except Agency.DoesNotExist:
        return redirect('home')

    context={
        "property_list": agency_property,
        "agency": agency,
        "form": form,
    }
    return render(request, 'agent-list.html', context)


def estate_detail(request, property_id):
    property_detail = Property.objects.get(property_id=property_id)

    context={
        "property_detail":property_detail,
    }
    return render(request, 'estate_detail.html', context)