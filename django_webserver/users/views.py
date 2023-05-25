from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# from .forms import UserForm
from . import forms
from models import Comment

# Create your views here.

def register(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home:mainpage')
    else:
        form = forms.UserForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
class CommentCreate(CreateView):
    model = Comment
    fields = ['to_user', 'text']

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)