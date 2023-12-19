from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('satis:musteri_listele')

    return render(request, "loginform.html", {"form": form, 'title': 'Giriş Yap', })


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Başarıyla çıkış yapıldı.')
        return redirect('home:satis_ilksayfa')
    else:
        messages.error(request, 'Çıkış yapmak için önce giriş yapmalısınız.')
        return redirect('home:401')
