from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages


def login_view(request):
    # POST isteği varsa formu işle, yoksa boş form göster
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # Kullanıcıyı doğrula
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yapıldı.')
            return redirect('home:satis_homepage')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')

    # Form geçersizse veya GET isteği varsa, formu göster
    context = {"form": form, 'title': 'Giriş Yap'}
    return render(request, "loginform.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Başarıyla çıkış yapıldı.')
        return redirect('home:satis_ilksayfa')
    else:
        messages.error(request, 'Çıkış yapmak için önce giriş yapmalısınız.')
        return redirect('home:401')
