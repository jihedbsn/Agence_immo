from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import BadHeaderError, send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        else:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, email=email)
            if has_contacted:
                messages.error(request, 'This Email is already used to make an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        number=number, message=message, user_id=user_id, realtor_email=realtor_email)
        
        contact.save()

        send_mail(
            'Property Listing Iquiry',
            'There has been an inquiry for '+ listing,
            'jihed.mohamed97@gmail.com',
            [realtor_email, 'mohamed.jihed.bousnina@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'Your request has been submitted, a realtor will contact you soon!')

        return redirect('/listings/'+listing_id)