from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy, reverse
# from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
# from .forms import UserForm
from . import forms
# from models import Comment, Profile
from .models import Profile

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


class ProfileView(DetailView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
    model = User
    template_name = 'users/profile.html'


class EditProfileView(UpdateView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
    model = Profile
    template_name = 'users/profile_edit.html'
    fields = ['nickname', 'profile_photo', 'note']


# @login_required
# class CommentCreate(CreateView):
#     model = Comment
#     fields = ['to_user', 'text']

#     def form_valid(self, form):
#         form.instance.writer = self.request.user
#         return super().form_valid(form)