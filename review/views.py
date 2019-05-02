from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# from profileapp.models import Profile
# from datetime import datetime
# from django.core.files.storage import FileSystemStorage

@login_required(login_url='signin')
def add_review(request): 
	if request.method == 'POST':
		print('post')
		form = ReviewForm(request.POST)
		if form.is_valid():
			print('form valid')
			new_review = form.save(commit=False)
			# print(new_review)
			# print(User.objects.get(user=request.user))
			new_review.user=request.user
			print('new review')
			new_review.save()
			return redirect('tour:index')
	else:
	    return render(request, 'add_review.html', { 'form': ReviewForm })
