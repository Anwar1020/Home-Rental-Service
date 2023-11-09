import email
import imp
from pickle import NONE
import re
from select import select
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile, Post, PostAddress, PostDetail

def landing(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, 'landing.html', { })

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        address = request.POST['address']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signuppage')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signuppage')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, username = username, email = email, address = address)
                new_profile.save()
                return redirect('signinpage')

        else:
            messages.info(request, 'Password not matching')
            return redirect('signuppage')
    return render(request, 'signup.html', { })

def signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:     
            user = authenticate(username=User.objects.get(email=email), password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Credentials are invalid!')
                return redirect('signinpage')
        except:
            messages.info(request, 'You are not a user')
            return redirect('signinpage')
    return render(request, 'signin.html', {})

@login_required(login_url='signinpage')
def homepage(request):
    user_object = User.objects.get(username = request.user.username)
    # print(user_object)
    # user_profile = Profile.objects.get(user = user_object)
    context = {
        # 'user_profile' : user_profile
    }
    
    return render(request, 'home.html', context)

@login_required(login_url='signinpage')
def logout(request):
    auth.logout(request)
    return redirect('signinpage')

@login_required(login_url='signinpage')
def createpost(request):
    if request.method == 'POST':
        hname = request.POST['hname']
        hdivision = request.POST['division']
        hdistrict = request.POST['district']
        hupazila = request.POST['upazila']
        addrdesc = request.POST['addrdesc']
        rooms = request.POST['rooms']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        gfacility = request.POST['gfacility']
        sdesc = request.POST['sdesc']
        price = request.POST['price']
        email = request.POST['email']
        phone = request.POST['phone']
        imgadd = request.FILES.get('imgadd')

        if(gfacility == 'on'):
            gfacility = True
        else:
            gfacility = False

        # user_object = User.objects.get(username = request.user.username)
        # user_profile = Profile.objects.get(user=user_object)

        new_post = Post.objects.create(username = request.user.username, price = price, images = imgadd)
        new_postdetail = PostDetail.objects.create(house_name = hname, room_no = rooms, bedroom_no = bedrooms, 
                                        bathroom_no = bathrooms, gas_facility = gfacility, description = sdesc)
        new_postaddress = PostAddress.objects.create(home_div = hdivision, home_dist = hdistrict,
                                        home_upa = hupazila, addr_desc = addrdesc, contact1 = email, contact2 = phone)

        new_post.save()
        new_postdetail.save()
        new_postaddress.save()

        return redirect("homepage")

    return render(request, 'createpost.html',{})

def search(request):
    return render(request,"dropdown.html",{})