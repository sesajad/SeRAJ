from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('administratives:home')
        elif request.user.is_professor:
            return redirect('professors:home')
        else:
            return redirect('students:home')
    return render(request, 'home.html')

def error_404(request, exception):
        data = {}
        return render(request, '404.html', data)


def error_403(request, exception):
    data = {}
    return render(request, '403.html', data)
