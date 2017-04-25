from django.shortcuts import render, redirect
import random

def index(request):
	return render (request, 'index.html')

def results(request):
	words = ['free', 'what', 'about', 'why', 'who', 'broke', 'flower', 'sea', 'scream', 'she', 'he', 'you', 'thousand', 'these', 'eyes', 'A', 'time', 'rose', 'moon', 'honey', 'fall', 'winter', 'summer', 'spring', 'passionate', 'love', 'I', 'a', 'me', 'my', 'seek', 'bliss', 'emerald', 'gold', 'one']
	value = request.POST['number']
	print value
	poem = []
	for x in range(0, int(value)):
			random_word =random.choice(words)
			poem.append(random_word)
	string = ' '.join(poem)
	context = {
	'poem':string
	}
	print context
	return render(request, 'index.html', context)


