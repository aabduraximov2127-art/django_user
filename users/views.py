from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from . import forms
from unidecode import unidecode
# Create your views here.
User=get_user_model()



def normalize(text):
    if text:
        return unidecode(text).lower()
    return ""

def user_view(request):
    query = request.GET.get('q')

    users = User.objects.all()

    if query:
        query_norm = normalize(query)

        filtered_users = []

        for user in users:
            name = normalize(user.first_name)

            if query_norm in name:
                filtered_users.append(user)

        users = filtered_users

    return render(request, "index.html", {
        "users": users,
        "query": query
    })

def user_delete(request, id):
    user=get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return redirect("user_view")
    return render(request, "user_delete.html",{"user": user})


def user_update(request, slug):
    user=get_object_or_404(User, slug=slug)
    form=forms.UserForm(request.POST,request.FILES,instance=user)
    if request.POST:
        if form.is_valid():
            form.save()
        return redirect('user_view')
   
    return render(request, "user_update.html", {"form": form})

def user_create(request):
    form=forms.UserForm(request.POST,request.FILES)
    if request.POST:
        if form.is_valid():
            form.save()
        return redirect('user_view')
    return render(request, "user_create.html", {"form": form})

def user_detail(request, slug):
    user=get_object_or_404(User, slug=slug)
    return render(request, "user_detail.html", {"user": user})