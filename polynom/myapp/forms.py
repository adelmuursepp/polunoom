# -*- coding: utf-8 -*-
from django import forms


class PolynomForm(forms.Form):
	polynom = forms.CharField(label='Proovi arvutada näitena toodud polünoomi nullkohad või kirjuta ise vabaliikmega polünoom', initial = 'x**3-2x**2-5x+6')