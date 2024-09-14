from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Project

def home(request):
    return render(request, 'portfolio_app/home.html')



def about(request):
    return render(request, 'portfolio_app/about.html')

def projects_view(request):
    projects = Project.objects.only('name')  # Select only necessary fields
    return render(request, 'portfolio_app/projects.html', {'projects': projects})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm

def reach_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            # Return a JSON response with the success message
            return JsonResponse({'message': 'Your message has been successfully sent!'})
        else:
            # Return a JSON response with errors if the form is invalid
            return JsonResponse({'message': 'There was an error with your submission.'}, status=400)
    
    form = ContactForm()
    return render(request, 'portfolio_app/reach_me.html', {'form': form})


