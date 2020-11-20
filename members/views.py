from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm, PasswordChangingForm


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	# foom_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')


def password_success(request):
	return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('story-list')

	def get_object(self):
		return self.request.user
