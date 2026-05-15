from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as auth_login,
    logout
)
from unidecode import unidecode

from .forms import UserForm, RegisterForm, LoginForm

User = get_user_model()

def user_list(request):
    users = User.objects.all()
    query = request.GET.get("q")
    users = User.objects.all()

    if query:
        q = normalize(query)

        users = [
            u for u in users
            if q in normalize(u.first_name)
        ]
    return render(request, "index.html", {"users": users})

def normalize(text):
    if text:
        return unidecode(text).lower()
    return ""



def home(request):



    return render(request, "home.html")



def user_create(request):

    if request.method == "POST":

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("user_list")

    else:
        form = UserForm()

    return render(request, "user_create.html", {
        "form": form
    })



def user_update(request, slug):

    user = get_object_or_404(User, slug=slug)

    if request.method == "POST":

        form = UserForm(
            request.POST,
            request.FILES,
            instance=user
        )

        if form.is_valid():
            form.save()
            return redirect("user_detail", slug=user.slug)

    else:
        form = UserForm(instance=user)

    return render(request, "user_update.html", {
        "form": form
    })



def user_delete(request, id):

    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.delete()
        return redirect("user_list")

    return render(request, "user_delete.html", {"user": user})


def user_detail(request, slug):

    user = get_object_or_404(User, slug=slug)

    return render(request, "user_detail.html", {"user": user})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# def login(request):

#     if request.method == "POST":

#         form = LoginForm(request, data=request.POST)

#         if form.is_valid():

#             user = form.get_user()
#             auth_login(request, user)
        
        
#             return redirect("user_list")

#     else:
#         form = LoginForm()

#     return render(request, "login.html", {
#         "form": form
#     })



# def logout_view(request):
#     logout(request)
#     return redirect("login")

