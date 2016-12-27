from django.shortcuts import render

from forms import Signup_form

def signup(request):
    form = Signup_form()

    name = request.POST.get('name','')
    email = request.POST.get('email', '')
    pass1 = request.POST.get('pass1', '')
    pass2 = request.POST.get('pass2', '')

    # Do some validations here

    user = User.objects.create_user(name, email, pass2)
    if user:
        user.save()

    return render(request, 'signup.html', {'form': form})
