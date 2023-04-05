from django.shortcuts import render, redirect
from .models import Work, Contractor, Customer
#from .forms import WorkForm
#from .forms import DetailForm
#from .forms import ContractorForm


def index(request):
    return render(request, "index.html")


def work(request):
    works = Work.objects.order_by('work_name')

    return render(request, 'work.html', {'works': works})


def contractor(request):
    contractors = Contractor.objects.order_by('contractor_name')

    return render(request, 'contractor.html', {'contractors': contractors})

def customer(request):
    customers = Customer.objects.order_by('last_name')

    return render(request, 'customer.html', {'customers': customers})


#def add_work(request):
    #if request.method == 'POST':
       # form = WorkForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('/work/')
    #else:
       # form = WorkForm()

    #return render(request, 'forms.html', {'form': form})


#def add_contractor(request):
    #if request.method == 'POST':
        #form = ContractorForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('/contractor/')
    #else:
        #form = ContractorForm()

    #return render(request, 'forms.html', {'form': form})


#def add_customer(request):
    #if request.method == 'POST':
        #form = CustomerForm(request.POST)
        #if form.is_valid():
            #result = form.cleaned_data
            #new = Customer(
                #name=result['name'],
                #last_name=result['last_name'],
                #phone=result['phone'])
            #new.save()
            #return redirect('/customers/')
    #else:
        #form = CustomerForm()

        #return render(request, 'forms.html', {'form': form})
