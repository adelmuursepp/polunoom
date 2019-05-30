from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import PolynomForm
from .nullkohad import *

def polynom(request):
	formivastus='x**3-2x**2-5x+6'

	if request.method == "POST":
		form = PolynomForm(request.POST)

		if form.is_valid():
			formivastus = form.cleaned_data['polynom']


	form=PolynomForm()
	vastused = NullKohad(formivastus)
	

	
	return render(request, 'form.html', {'form': form, 'polynom': polynom, "vastused":vastused})


def graph(request):


	

	
	return HttpResponse("blaa")

