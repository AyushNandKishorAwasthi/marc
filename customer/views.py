import datetime
from . models import Response 
from crmapp.models import Customer
from adminapp.models import Product
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

#locals() jitene bhi local variable han unko frontend me bhej dega
#cache_control = ye ek decorator views ko call karne se pahle session ko server se validate karta hai
# login view
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            userid = request.session["userid"]
            cust = Customer.objects.get(emailaddress=userid)
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect('crmapp:login')
        #return render(request,'login.html') 
#logout view
def logout(request):
    try:
        #delete session
        del request.session['userid']
    except KeyError:
        return redirect('crmapp:login')
    return redirect('crmapp:login')

#response view 13/04/24
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def response(request):
    try:
        #check if user is logged in :-)
        if request.session['userid']!=None:
            cust = Customer.objects.get(emailaddress = request.session['userid'])
            print('inside first if')
            if request.method=='POST':
                # name = request.POST['name']
                # contactno = request.POST['contactno']
                # emailaddress = request.POST['emailaddress']
                name = cust.name
                contactno = cust.contactno
                emailaddress = cust.emailaddress
                responsetype = request.POST['responsetype']
                subject = request.POST['subject']
                responsetext = request.POST['responsetext']
                posteddate = datetime.datetime.today() 
                #creating object and saving to Response Table
                res = Response(name=name,contactno = contactno, emailaddress = emailaddress, responsetype = responsetype, subject = 
                subject, responsetext = responsetext, posteddate = posteddate)
                res.save()
                return render(request,'response.html',{'msg':'Response Saved Successfully'})
            return render(request,'response.html')
    except KeyError:
        return redirect('crmapp:login')

#viewprofile    view 
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            userid = request.session["userid"]
            cust = Customer.objects.get(emailaddress=userid)
            if request.method == 'POST':
                name = request.POST["name"]
                gender = request.POST["gender"]
                address = request.POST["address"]
                contactno = request.POST["contactno"]
                emailaddress = request.POST["emailaddress"]
                Customer.objects.filter(emailaddress = emailaddress).update(name = name, gender = gender, address = address, contactno = contactno )
                #Customer update does not require to be saved by save() function
                print("dAta saved")
                return redirect("customer:customerhome")
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect('crmapp:login')

# viewProducts View
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def products(request):
    try:
        if request.session["userid"]!=None:
            userid = request.session["userid"]
            cust = Customer.objects.get(emailaddress=userid)
            prod = Product.objects.all()
            return render(request,"products.html",locals())
    except KeyError:
        return redirect('crmapp:login')