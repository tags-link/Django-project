from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    users = User.objects.all()
    return render(request,'dashboard.html',{'user':users})