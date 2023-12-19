from django.shortcuts import render, redirect


def satis_ilksayfa(request):
    if request.user.is_authenticated:
        return redirect('satis:musteri_listele')
    return render(request, 'home.html')


def view_401(request):
    return render(request, '401.html', {})
