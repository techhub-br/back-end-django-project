from django.shortcuts import render
from .models import UserProfile

def user_profile_list(request):
    user_profiles = UserProfile.objects.all().order_by('ranking')
    return render(request, 'user_profiles/user_profile_list.html', {'user_profiles': user_profiles})
