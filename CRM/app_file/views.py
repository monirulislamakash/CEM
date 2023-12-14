from django.shortcuts import render,redirect
from .models import *
from django.contrib import auth
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
import stripe
stripe.api_key = "sk_test_51NrQRGG2zlBREdyvQAvw9tZV7ijuGGWJvtuSoKt5CYSFTytEFXDDlT1HNMPTc7g4XZqpxuCtnWLUBbEwQCh22UbU00JRNfqGfU"


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    return redirect(signin)
def customur_list(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            block=request.POST.get("block")
            all_customur=Customur.objects.get(id=block)
            if all_customur.Block== False:
                all_customur.Block=True
                all_customur.save()
                return redirect(customur_list)
            else:
                all_customur.Block=False
                all_customur.save()
                return redirect(customur_list)
        all_customur=Customur.objects.filter(Delete=False)
        sendvar={
            "customur":all_customur
        }
        return render(request,"customur.html",sendvar)
    return redirect(signin)
def block_customur_list(request):
    if request.user.is_authenticated:
        all_customur=Customur.objects.filter(Block=True)
        sendvar={
            "customur":all_customur
        }
        return render(request,"customur.html",sendvar)
    return redirect(signin)
    
def deleted_customur_list(request):
    if request.user.is_authenticated:
        all_customur=Customur.objects.filter(Delete=True)
        sendvar={
            "customur":all_customur
        }
        return render(request,"customur.html",sendvar)
    return redirect(signin)

def profile(request,id):
    if request.user.is_authenticated:
        all_customur=Customur.objects.filter(id=id)
        sendvar={
            "customur":all_customur
        }
        return render(request,"profile.html",sendvar)
    return redirect(signin)
def customur_profile(request,id):
    if request.user.is_authenticated:
        all_customur=Customur.objects.get(id=id)
        if request.method=="POST":
            if all_customur.Delete== False:
                all_customur.Delete=True
                all_customur.save()
                return redirect(customur_list)
            else:
                all_customur.Delete=False
                all_customur.save()
                return redirect(customur_list)
        sendvar={
            "profile":all_customur
        }
        return render(request,"profile.html",sendvar)
    return redirect(signin)

def search_customur(request):
    if request.user.is_authenticated:
        search=request.POST.get("search")
        if request.method=="POST":
            name=Customur.objects.filter(Name__icontains=search)
            phone=Customur.objects.filter(Phone__icontains=search)
            email=Customur.objects.filter(Email__icontains=search)
            name_phone=name.union(phone)
            name_phone_email=name_phone.union(email)
            sendvar={
                'customur':name_phone_email,
            }
            return render(request,"customur.html",sendvar)
        return redirect(customur_list)
    return redirect(signin)
def signin(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"signin.html",{'error':"Invalide user or password"})
    return render(request,"signin.html")
def logout(request):
    auth.logout(request)
    return redirect(index)
def email_marketing(request):
    get=Customur.objects.all()
    email=[]
    for i in get:
        email.append(i.Email)
    sendvar={
        'mailnumber':len(email)
    }
    if request.method=="POST":
        subject = request.POST.get("subject")
        message = request.POST.get("mail")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email
        mseg=EmailMultiAlternatives( subject, message, email_from, recipient_list )
        mseg.content_subtype="html"
        mseg.send()
    return render(request,"emai_marketing.html",sendvar)
def ProductAndPricing(request):
    product=ProductPrice.objects.all()
    sendvar={
        "product":product,
    }
    return render(request,"productandpricing.html",sendvar)
def subscribe_plan(request):
    return render(request,"subscribe_plans.html")
    
def checkout_buy(request,id):
    get_product=ProductPrice.objects.get(id=id)
    print(get_product)
    if request.method=="POST":
        get_email=request.POST.get("email")
        get_name=request.POST.get("name")
        amount=get_product.price
        get_source=request.POST.get("stripeToken")
        Create_customer=stripe.Customer.create(
            email=get_email,
            name=get_name,
            source=get_source,
        )
        charge=stripe.Charge.create(
            customer=Create_customer,
            amount=amount*100,
            currency='usd',
            description="Discription"
        )
        return render(request,"index.html")
    sendvar={
        "get_product":get_product,
    }
    return render(request,"checkout.html",sendvar)
def checkout_subscribe(request,id):
    get_product=ProductPrice.objects.get(id=id)
    print(get_product)
    if request.method=="POST":
        get_email=request.POST.get("email")
        get_name=request.POST.get("name")
        amount=get_product.price
        get_source=request.POST.get("stripeToken")
        Create_customer=stripe.Customer.create(
            email=get_email,
            name=get_name,
            source=get_source,
        )
        charge=stripe.Charge.create(
            customer=Create_customer,
            amount=amount*100,
            currency='usd',
            description="Discription"
        )
        return render(request,"index.html")
    sendvar={
        "get_product":get_product,
    }
    return render(request,"checkout.html",sendvar)