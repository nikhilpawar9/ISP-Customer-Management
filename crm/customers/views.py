from django.shortcuts import render
from django.http import HttpResponse
from customers.models import Customer
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render (request, 'customers/dashboard.html')


def customers(request):
    cust=Customer.objects.all()

    return render (request, 'customers/customers.html', {'cust':cust})




def addcustomer(request):
    if (request.method== 'POST'  ) :
        name = request.POST.get('name')
        email = request.POST.get('email')
        primarymobile = request.POST.get('primarymobile')
        alternatemobile = request.POST.get('alternatemobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        connectiontype = request.POST.get('connectiontype')
        
        if connectiontype == 'wireless':
            catcablelength= request.POST.get('catcablelength')
            p2pdevice= request.POST.get('p2pdevice')
            wirelessrouterprice= request.POST.get('wirelessrouterprice')
            ftthfiberlength = '0'
            ftthrouterprice = '0'
            closerbox= '0'
            patchcord= '0'
        
        elif connectiontype == 'ftth':
            catcablelength= '0'
            p2pdevice= '0'
            wirelessrouterprice= 0            
            ftthfiberlength = request.POST.get('ftthfiberlength')
            ftthrouterprice = request.POST.get('ftthrouterprice')
            closerbox= request.POST.get('closerbox')
            patchcord= request.POST.get('patchcord')
        
        installationcharges= request.POST.get('installationcharges')
        ontusername= request.POST.get('ontusername')
        ontpassword= request.POST.get('ontpassword')
        customerphoto= request.POST.get('customerphoto')
        kycdocument= request.POST.get('kycdocument')
        
        addcustomer = Customer(name = name, email=email, primary_mobile= primarymobile, alternate_mobile = alternatemobile, address=address, city=city, state=state, zipcode=zipcode, connection_type= connectiontype, cat_6_cable_length = catcablelength, p2p_device_price=p2pdevice, wireless_router_price=wirelessrouterprice, ftth_fiber_length = ftthfiberlength, closer_box = closerbox, patch_cord = patchcord, ftth_router_price = ftthfiberlength, installation_charges= installationcharges, username= ontusername, password = ontpassword, customer_photo = customerphoto, kYC_document = kycdocument)
        addcustomer.save()
    return render (request, 'customers/addcustomer.html')


def login(request):
    return render (request, 'customers/login.html')

def logout(request):
    return render (request, 'customers/logout.html')

def signup(request):
    if request.method == "POST":       
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render (request, 'customers/signup.html', {'form':fm})