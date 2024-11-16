import os.path
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from customers.forms import CustomerForm
from customers.models import Customer


# Home Page
def index(request):
    return render(request, 'index.html')


# About Page with List of Customers
def about(request):
    data = Customer.objects.all()  # Fetch all customer objects
    context = {'data': data}
    return render(request, 'about.html', context)


# Features Page
def features(request):
    return render(request, 'features.html')


# Pricing Page
def pricing(request):
    return render(request, 'pricing.html')



# Contact Form (Customer Form Integration)
def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer details submitted successfully!")
            return redirect('contact')  # Redirect to the same page after submission
        else:
            messages.error(request, "Error in form submission. Please correct the errors below.")
    else:
        form = CustomerForm()
    return render(request, 'contact.html', {'form': form})


# Update Customer Details
def update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, f'Customer updated successfully! Image "{file_name}" uploaded.')
            else:
                messages.success(request, 'Customer details updated successfully.')
            return redirect('about_us')  # Redirect to the about page
        else:
            messages.error(request, 'Please confirm your changes.')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update.html', {'form': form, 'customer': customer})


# Delete Customer
def delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    try:
        customer.delete()
        messages.success(request, 'Customer deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}. Customer not deleted!')
    return redirect('about_us')  # Redirect to the about page after deletion
