from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    success = False

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            success = True
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'success': success
    })