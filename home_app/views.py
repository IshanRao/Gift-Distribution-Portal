from django.shortcuts import render,redirect
from . models import *

def distributor_login(req) :
    return render(req,'home_app/distributor_login.html')

def distributor_gift_selection(req) :
    return render(req,'home_app/distributor_gift_selection.html')

def distributor_peoplelist(req) :
    return render(req,'home_app/distributor_peoplelist.html')

def user_landing(req) :
    return render(req,'home_app/user_landing.html')

def user_gift_selection(req) :
    return render(req,'home_app/user_gift_selection.html')

def user_detail(req) :
    return render(req,'home_app/user_detail.html')    

def user_successful_giftorder(req) :
    return render(req,'home_app/user_successful_giftorder.html')
