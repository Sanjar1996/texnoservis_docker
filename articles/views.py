from django.shortcuts import render, redirect

from .models import *


def index(request):
    about = AboutModel2.objects.all()
    hodim = HodimModel.objects.all()
    portfolio = Portfolio.objects.all()
    image_portfolio = ImagePortfolio.objects.all()
    faq = FAQModel.objects.all()

    if request.method == "POST":
        contact = ContactModel(
            name=request.POST['name'],
            email_address=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        contact.save()

        return redirect('home_page')

    context = {
        'hodim': hodim,
        'portfolio': portfolio,
        'image_portfolio': image_portfolio,
        'about': about,
        'faq': faq,
    }
    return render(request, 'index.html', context)
