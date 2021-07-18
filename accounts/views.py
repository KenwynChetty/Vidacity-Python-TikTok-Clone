from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile
from feed.models import Post
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
# Create your views here.

def registerPage(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username Is Taken!')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Is Taken!')
				return redirect('register')
			else:
				userForm = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				userForm.save()
				print('User Created')
				user = authenticate(username=username, password=password1)
				login(request,user)
				return redirect('accounts:setup_profile')

		else: 
			messages.info('Password Not Matching')
			return redirect('register')
	else:
		return render(request, 'register.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

@login_required
def setup_profile(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)

        if pform.is_valid():
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('home')
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'setup_profile.html', {
        'pform': pform,
    })


def profile(request):
	posts = Post.objects.all()
	return render(request, 'profile.html',{'posts':posts})


@login_required
def UserChatList(request):
	current_user = request.user.id
	user_p = get_user_model()
	users = user_p.objects.filter().exclude(id=current_user)
	return render(request, 'userschatlist.html',{'user_pro':users})