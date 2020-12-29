from django.shortcuts import render

def homeAction(request):
    context = {}
    return render(request,'ResumeWebsite/index.html', context)