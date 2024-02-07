# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
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

def add_data_ojt_form(request):
    return render(request, 'add_data_ojt_form.html')

def edit_data_ojt(request, application_id):
    # Retrieve the application object from the database based on the application_id
    application = get_object_or_404(InternshipApplication, id=application_id)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        ojt_duration = request.POST.get('ojt_duration')
        province = request.POST.get('province')
        school = request.POST.get('school')
        school_address = request.POST.get('school_address')
        
        # Update the fields of the retrieved application object
        application.ojt_duration = ojt_duration
        application.province = province
        application.school = school
        application.school_address = school_address
        
        # Save the updated application object to the database
        application.save()
        
        # Redirect to a success page or any other page
        return redirect('epmd')  # You can change 'home' to the appropriate URL name
        
    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, 'edit_data_ojt.html', {'application': application})

def view_data_ojt(request, application_id):
    # Retrieve the application object from the database based on the application_id
    application = get_object_or_404(InternshipApplication, id=application_id)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        ojt_duration = request.POST.get('ojt_duration')
        province = request.POST.get('province')
        school = request.POST.get('school')
        school_address = request.POST.get('school_address')
        
        # Update the fields of the retrieved application object
        application.ojt_duration = ojt_duration
        application.province = province
        application.school = school
        application.school_address = school_address
        
        # Save the updated application object to the database
        application.save()
        
        # Redirect to a success page or any other page
        return redirect('epmd')  # You can change 'home' to the appropriate URL name
        
    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, 'view_data_ojt.html', {'application': application})

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