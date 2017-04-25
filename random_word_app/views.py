from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random

def index(request):
	return render (request, 'index.html')

def attempt(request):
	generate_word = get_random_string(length = 14)
	#request.session['number'] = 0
	request.session['number'] +=1
	request.session['word'] = generate_word
	return redirect('/')
