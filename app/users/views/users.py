from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def home(request):
    if request.user.is_authenticated:
        if request.user.is_Administrative:
            return redirect('administratives:administratives_home')
        elif request.user.is_Professor:
            return redirect('professors:professors_home')
    return render(request, 'home.html')

def error_404(request, exception):
        data = {}
        return render(request, '404.html', data)


def error_403(request, exception):
    data = {}
    return render(request, '403.html', data)