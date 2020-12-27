from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()

            messages.success("Registration is successfull..")
            return redirect('index')
        else:
            return render(request, "index.html")
    else:
        userform = UserForm()
        context = {
            'userform': userform,
        }
        return render(request, "index.html", context)


def registration(request):
    context = {}
    values = {}
    if request.method == "POST":
        userform = UserForm(request.POST)
        userform1 = UserForm_1(request.POST)

        if userform.is_valid() and userform1.is_valid():

            user = userform.save()
            user.set_password(user.password)
            user.save()

            u1 = userform1.save(commit=False)
            u1.user = user

            u1.save()

            messages.success(request,"Registration is successfull..")
            return redirect('index')
        else:
            userform = UserForm()
            userform1 = UserForm_1()
            context = {
                "userform": userform,
                "userform1": userform1,
            }
            return render(request, "registration.html", context)
    else:
        userform = UserForm()
        userform1= UserForm_1()
        context = {
            "userform":userform,
            "userform1":userform1,
        }
    return render(request, "registration.html", context)


def userlogin(request):
    if request.method == "POST":
        authform = AuthenticationForm(request=request, data=request.POST)
        if authform.is_valid():
            uname = authform.cleaned_data['username']
            password = authform.cleaned_data['password']
            user = authenticate(username=uname,password=password)
            # if user is not None:
            if user:
                if user.is_active:
                    login(request, user)
                    a_user = request.user
                    username = User.objects.get(username=a_user)

                    try:
                        if username.profile.is_complete:
                            if username.profile.position == "student":
                                return redirect("s_panel")
                            if username.profile.position == "teacher":
                                return redirect("t_panel")
                            if username.profile.position == "institute":
                                return redirect("i_panel")

                    except:
                        return redirect('userprofile')

                else:
                    messages.error("Contact your administrator for account activation...")
                    loginform = AuthenticationForm()
                    context = {
                        'loginform': loginform,
                    }
                    return render(request, "login.html", context)
            # else:
            #     messages.error("Invalid credentials...")
            #     loginform = AuthenticationForm()
            #     context = {
            #         'loginform': loginform,
            #     }
            #     return render(request, "login.html", context)
        else:
            messages.error(request, "please enter valid username and password")
            loginform = AuthenticationForm()
            context = {
                'loginform': loginform,
            }
            return render(request, "login.html", context)
    else:
        loginform = AuthenticationForm()
        context = {
            'loginform': loginform,
        }
        return render(request, "login.html", context)


def userprofile(request):
    user = request.user

    username = User.objects.get(username=user)
    uid = username.id
    # profile_form = ProfileForm()
    user_data = User.objects.get(username=user)
    u1 = UserModel.objects.get(user__username=user) #for fetch contact

    institutes = Institute.objects.all()

    context = {
        # 'profile_form': profile_form,
        'user_data': user_data,
        'uid': uid,
        'u1':u1,
        'institutes':institutes,
    }
    return render(request, "profile.html", context)


def saveprofile(request):
    user = request.user
    username = User.objects.get(username=user)

    gender = request.POST.get("gender")
    birthdate = request.POST.get("birthdate")
    contact = request.POST.get("contact")
    uid = request.POST.get("uid")
    position = request.POST.get("position")
    institute = request.POST.get("institute")
    # institute = institute.inst_code
    print("*/*/",institute)
    user_profile = Profile(user_id=uid,gender=gender,birthdate=birthdate,contact=contact,position=position,is_complete=True, institute=institute)
    user_profile.save()

    if username.profile.position == "student":
        return redirect("s_panel")
    elif username.profile.position == "teacher":
        return redirect("t_panel")
    else:
        return redirect('userprofile')
    # return None

def complete_profile(request):
    user = request.user
    username = User.objects.get(username=user)
    profiledata=Profile.objects.get(user=username)
    print("ss",profiledata.institute)

    # inst_data = profiledata.institute
    inst_data = Institute.objects.get(inst_code=profiledata.institute)
    print(inst_data)
    context = {"uname":username,"profiledata":profiledata,"inst_data":inst_data}
    return render(request,"cprofile.html",context)


def student_panel(request):
    return render(request, "s_panel.html")


def teacher_panel(request):
    return render(request, "t_panel.html")


def intitute_panel(request):
    return render(request, "i_panel.html")


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")


def notes(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, "notes.html", context)


def que_paper(request):
    que_paper = Question_Papers.objects.all()
    context = {
        'que_paper': que_paper,
    }
    return render(request, "que_paper.html", context)


def model_papers(request):
    model_papers = Model_Papers.objects.all()
    context = {
        'model_papers': model_papers,
    }
    return render(request, "model_papers.html", context)


