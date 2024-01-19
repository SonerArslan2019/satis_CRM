from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('satis:musteri_listele')  # Başarılı giriş sonrası yönlendirme
        else:
            # Başarısız giriş durumu
            return render(request, "loginform.html", {"error": "Kullanıcı adı veya şifre hatalı"})
    return render(request, "loginform.html", {})


def logout_view(request):
    logout(request)
    return redirect('user:login_view')
