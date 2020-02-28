from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import ville_choices, price_choices, bedroom_choices


def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[: 3]
    context = {
        'listings': listing,
        'ville_choices': ville_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvps': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
