
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import csv
from customers.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerSearchForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render (request, 'customers/dashboard.html')

@login_required(login_url='/signin')

def customers_list(request):
    customer_list=Customer.objects.all()
    form = CustomerSearchForm(request.POST )
    context = {
        "form": form,
        "customer_list": customer_list,
    }
    
    if request.method == 'POST':
        customer_list=Customer.objects.filter(name = form['name'].value())   
        context = {
        "form": form,
        "customer_list": customer_list,
    }
    return render (request, 'customers/customers_list.html',context)


@login_required(login_url='/signin')

def customerQuickView(request,customername):
    cs = Customer.objects.filter(name=customername)
    return render(request,'customers/customer_quickview.html',{'cs':cs[0]})
@login_required(login_url='/signin')
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

  





def user_profile(request):
    return render(request, 'customers/profile.html')
def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    
    else:
        fm = UserCreationForm()
    return render(request, 'customers/sign_up.html' , {'form' : fm})

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request , data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        fm = AuthenticationForm()

    return render(request,'customers/signin.html', {'form' : fm})
@login_required(login_url='/signin')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin')








def export_csv(request):
    customer_list=Customer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition' ] = 'attachment; filename = Customers'+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Name','Pri. Mobile','Alt. Mobile','Email','Address','Zip Code','City','State','Connection Type','Cat 6 Cable Length','P2P Device Price','Wireless Router Price','FTTH fiber Length','Closer Box','Patch Cord','FTTH Router Price','Inst. Charges','UserName'])
    for cu in customer_list:
         writer.writerow([cu.name,cu.primary_mobile,cu.alternate_mobile,cu.email,cu.address,cu.zipcode,cu.city,cu.state,cu.connection_type,cu.cat_6_cable_length,cu.p2p_device_price,cu.wireless_router_price,cu.ftth_fiber_length,cu.closer_box,cu.patch_cord,cu.ftth_router_price,cu.installation_charges,cu.username])

    return response
