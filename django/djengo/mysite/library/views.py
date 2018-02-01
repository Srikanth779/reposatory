
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views herer





from django.http import HttpResponse
def index(request):

    return HttpResponse('Hello World')
