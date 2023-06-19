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
from .models import Comment, Profile
from django.contrib import messages

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


# class ProfileView(DetailView):
#     context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
#     model = User
#     template_name = 'users/profile.html'


# class EditProfileView(UpdateView):
#     context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
#     model = Profile
#     template_name = 'users/profile_edit.html'
#     fields = ['nickname', 'profile_photo', 'note']


def profile_edit_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', pk=pk)
    else:
        form = forms.ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'users/profile_edit.html', context)


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    comments = Comment.objects.filter(profile=profile)
    comment_form = forms.CommentForm()

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.profile = profile
            comment.save()
            return redirect('users:profile', pk=pk)

    context = {
        'user': user,
        'profile': profile,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'users/profile.html', context)


# @login_required
# class CommentCreate(CreateView):
#     model = Comment
#     fields = ['to_user', 'text']

#     def form_valid(self, form):
#         form.instance.writer = self.request.user
#         return super().form_valid(form)

# @login_required
# def add_comment(request):
#     if request.method == 'POST':
#         form = forms.CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.profile = request.user.profile
#             comment.save()
#             return redirect('profile', username=request.user.username)
#     else:
#         form = forms.CommentForm()
#     return render(request, 'add_comment.html', {'form': form})


@login_required
def add_comment_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            if comment.content:
                comment.user = request.user
                comment.profile = profile
                comment.save()
                return redirect('users:profile', pk=pk)
            else:
                messages.error(request, '댓글을 입력해주세요.')
    else:
        comment_form = forms.CommentForm()

    context = {
        'profile': profile,
        'comment_form': comment_form
    }
    return render(request, 'users/add_comment.html', context)