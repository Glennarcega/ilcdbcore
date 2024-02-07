# myapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InternshipApplication

def home(request):
    return render(request, 'home.html')

def c3d2(request):
    return render(request, 'c3d2.html')

def epmd(request):
    # Add logic for the epmd view if needed
    return render(request, 'epmd.html')

def tmd(request):
    # Add logic for the tmd view if needed
    return render(request, 'tmd.html')

def projectClick(request):
    # Add logic for the projectClick view if needed
    return render(request, 'projectClick.html')



def insert_data(request):
    if request.method == 'POST':
        # Assuming you receive data from a form POST request
        ojt_duration = request.POST.get('ojt_duration')
        province = request.POST.get('province')
        school = request.POST.get('school')
        school_address = request.POST.get('school_address')
        
        # Create an instance of InternshipApplication with the provided id
        new_application = InternshipApplication(
            
            ojt_duration=ojt_duration,
            province=province,
            school=school,
            school_address=school_address
        )
        
        # Save the new application to the database
        new_application.save()
        
        return redirect('epmd')
    else:
        return HttpResponse('Please use a POST request to insert data.')
    
def epmd(request):
    applications = InternshipApplication.objects.all()
    return render(request, 'epmd.html', {'applications': applications})