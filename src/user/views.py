from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import UserProfile

def index(request):
    user_list = UserProfile.objects.order_by('user__username')
    return render(request, 'user/index.html', {'user_list': user_list})

class UserProfileView(DetailView):
    model = UserProfile
    slug_field = "user__username"