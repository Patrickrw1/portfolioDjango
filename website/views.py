from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send an email - also change in settings.py
        send_mail(
            'Message from' + message_name, # subject
            message, # message
            message_email, # from email
            ['patrickrw@hotmail.com'], # To email 
            
        )
        
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog_details.html', {})
