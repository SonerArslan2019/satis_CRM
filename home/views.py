from django.shortcuts import render, redirect


def ilksayfa(request):
    if request.user.is_authenticated:
        return redirect('home:imalat_homepage')
    return render(request, 'home.html')


def imalat_homepage(request):
    return render(request, 'imalat_homepage.html')


def mr30_isemri_kapilar(request):
    return render(request, "isemri_mr30/mr30_isemri_kapilar.html")


def mr30_isemriolustur(request):
    return render(request, "isemri_mr30/mr30_isemriolustur.html")


# def mr30_imalatolustur(request):
#     return render(request, "isemri_mr30/mr30_imalatolustur.html")


def view_401(request):
    return render(request, '401.html', {})
