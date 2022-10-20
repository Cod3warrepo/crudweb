
# from django.contrib.auth.forms import UserCreationForm

# from .models import CustomUserModel


# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = 'CustomUserModel'
#         fields = ('email', 'username')

        
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUserModel


class CustomForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('email', 'username', 'password1', 'password2')
