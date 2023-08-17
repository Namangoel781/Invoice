from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':

            fm = UserLogin(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']    
                upass = fm.cleaned_data['password']    
                userObj = authenticate(username=uname, password=upass)
                if userObj is not None:
                    login(request, userObj)

                    return HttpResponseRedirect('/home/')
        else:
            fm = UserLogin()
        return render(request,'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/home/')
    
def logout_view(request):
     
     logout(request)

     return HttpResponseRedirect('/')



def home(request):
        return render(request, 'home.html')
        
# def add_client(request):
#      if request.method == "POST":
#           company_name = request.POST["company"]
#           gst_number = request.POST["gst"]
#           country = request.POST["Company"]
#           state = request.POST['state']
#           address = request.POST['address']
#           new_client = Client(company_name=company_name, gst_number=gst_number, country=country, state=state, address=address)
#           new_client.save()
#           client = Client.objects.all().values('Company_name').distinct()
#           client_d = {'clientd': client}
#           return render(request, 'Add.html', client_d)

# def add_client(request):

#      clientForm = ClientForm(request.POST)

#      return render(request, 'clients.html', {'clientForm':clientForm})


def add_client(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ClientFm = ClientForm(request.POST)
            if ClientFm.is_valid():
                company = request.POST["company_name"]
                gst_number = request.POST["gst_number"]
                country = request.POST["country"]
                state = request.POST['state']
                address = request.POST['address']
                new_client = Client(company_name=company, gst_number=gst_number, country=country, state=state, address=address)
                new_client.save()
                ClientFm = ClientForm()
        else:
            ClientFm = ClientForm()
        return render(request, 'clients.html', {'ClientFm': ClientFm})
    else:
        return HttpResponseRedirect('/')

# def add_service(request):
#      if request.method == "POST":
#           Client = request.POST["client"]
#           description = request.POST["qty"]
#           quantity = request.POST['qty']
#           amount = request.POST['amt']
#           new_service = Services(client=Client, description=description, quantity=quantity, amount=amount)
#           new_service.save()

#      return render(request, 'Add.html')

def company(request):
     if request.user.is_authenticated:
         if request.method == "POST":
             CompanyFm = CompanyForm(request.POST)
             if CompanyFm.is_valid():
                client = request.POST["client"]
                company_name = request.POST["company"]
                handle_by = request.POST["handle"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                account_number = request.POST["acct"]
                ifsc_code = request.POST["ifsc"]
                bank_name = request.POST["bank"]
                gst_number = request.POST["gst"]
                new_provider = Company(client = client, company_name = company_name, handle_by = handle_by, 
                email = email, phone = phone, account_number = account_number, ifsc_code = ifsc_code, 
                bank_name = bank_name, gst_number = gst_number)
                new_provider.save()
                CompanyFm = CompanyForm()
               #  provider = Company.objects.all()
                client = Client.objects.all().values('company_name').distinct()
         else:
             CompanyFm = CompanyForm
             details = {'CompanyFm':CompanyFm}
         return render(request, 'addinvoice.html' , details) 
     else:
         return HttpResponseRedirect('/')
     

def delete(request, id):
     delete_provider = Company.objects.get(id=id)
     delete_provider.delete()
     return HttpResponseRedirect('/company/')

def addinvoice(request):
        if request.method == "POST":
          Client = request.POST["client"]
          description = request.POST["qty"]
          quantity = request.POST['qty']
          amount = request.POST['amt']
          new_service = Services(client=Client, description=description, quantity=quantity, amount=amount)
          new_service.save()
        return render(request, 'addinvoice.html')

