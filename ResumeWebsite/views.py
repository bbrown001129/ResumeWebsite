from django.shortcuts import render

def homeAction(request):
    return render(request,'ResumeWebsite/index.html', {})