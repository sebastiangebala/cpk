from django.shortcuts import render

def centrum(request):
    return render(request, 'centrum/base.html', {})
