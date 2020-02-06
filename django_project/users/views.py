from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# importing flash message
from django.contrib import messages
from .templates.users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves the new user to the database..really simple huh?
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You may now Login')
            # now get redirected to home page need to import redirect fn
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    return render(request, 'users/profile.html')
