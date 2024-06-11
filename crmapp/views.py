from django.shortcuts import render,redirect
# OjectDoesNotExist exceptions is used here when user does not exist in the database
from django.core.exceptions import ObjectDoesNotExist
from .models import Enquiry, Customer, Login
from adminapp.models import Product
import datetime

# index view
def index(request):
    return render(request,'index.html')

# aboutus view
def aboutus(request):
    return render(request,'aboutus.html')

# registration view
def registration(request):
    if request.method =='POST':
        name = request.POST["name"]
        gender = request.POST['gender']
        address = request.POST['address']
        contactno = request.POST['contactno']
        emailaddress = request.POST['emailaddress']
        password = request.POST['password']
        regdate = datetime.datetime.today()
        #Object Relation Mapping 
        cust = Customer(name = name, gender = gender, address = address, contactno = contactno, emailaddress = emailaddress, regdate = regdate)
        cust.save() #data goes to customer table
        log = Login(userid = emailaddress, password = password, usertype = "customer")
        log.save() #data goes to login table
        return render(request, 'registration.html',{"msg":"Registration is done"})
    return render(request,'registration.html')

# login view
def login(request):
    if request.method=='POST':
        userid = request.POST['userid']
        password = request.POST['password']
        msgP=''
        try:
            obj = Login.objects.get(userid = userid, password = password)
            if obj is not None:
                if obj.usertype=='customer':
                    # msgP = 'Welcome Customer'
                    request.session["userid"]=userid
                    return redirect("customer:customerhome")
                elif obj.usertype=='admin':
                    # msgP = 'Welcome Admin'
                    request.session['adminid'] = userid
                    return redirect("adminapp:adminhome")
        except ObjectDoesNotExist:
            msgF='Invalid User'
        if msgP !='' and msgP:
            return render(request,'login.html',{'msgP': msgP})
        else: 
            return render(request,'login.html',{'msgF': msgF})    
    return render(request,'login.html')

# contactus view
# Enquirry ko savve karne ke liye alag se view banae bina data koo save karna hai 
def contactus(request):
    print("this is request",request)
    if request.method == 'POST':
        print("inside if")
        name = request.POST["name"]
        contact = request.POST["contact"]
        email = request.POST["email"]
        subject = request.POST["message"]
        postdate = datetime.datetime.today()
        # classVar  = ModelName(field = postVariable)
        # isko ORM bolte hai Object Relationship mapping
        enq = Enquiry(name = name,contact = contact, emailaddress=email, subject = subject, posteddate=postdate)    
        enq.save()
        return render(request,"contactus.html",{"msg":"Enquiry is saved"})
    return render(request,"contactus.html")

#Products View
def productsView(request):
    prod = Product.objects.all()
    return render(request,'products.html',locals())