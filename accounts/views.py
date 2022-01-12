from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST': #회원정보를 입력 받음
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else: #회원정보 입력 창으로 이동
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})
