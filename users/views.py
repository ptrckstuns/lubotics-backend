from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Wishlist
from django.views.generic import DetailView, View
from django.urls import reverse


def logout_view(request):
	logout(request)
	messages.success(request, f'Successfully logged out!')
	return redirect('login')

    # Redirect to a success page.
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)	
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login!')
			return redirect('login')
		# else:
		# 	messages.error(request, 'Document deleted.')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

# @login_required
class ProfileView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs): # get wishlist
		try:
			wishlist = Wishlist.objects.get(user=self.request.user)
		except Exception:
			# messages.warning(self.request, "You do not have any wishes")
			wishlist = []
			# return redirect("/")
		context = {
			'title': 'Profile',
			'object': wishlist
		}
	# return render(request, 'users/profile.html',  {'title': 'Profile'})
		return render(self.request, 'users/profile.html', context)


def editprofile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else: 
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}

	
	return render(request, 'users/edit_profile.html', context)
