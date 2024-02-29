from django import forms
from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput
from .models import Author, Item
from .models import User

class UserRegisterForm(forms.ModelForm):
    avatar = ImageField()
    password = CharField(max_length = 128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("avatar", "username", "first_name", "last_name")

class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)

class ItemCreateForm(forms.ModelForm):
    image = ImageField()
    class Meta:
        model= Item
        fields = "__all__"

class ItemUpdateForm(forms.ModelForm):
    image = ImageField()
    class Meta:
        model = Item
        fields = "__all__"

# class AuthorRegisterForm(forms.ModelForm):
#     avatar = ImageField()
#     password = CharField(max_length = 128, widget=PasswordInput)

#     # def save(self, commit=True):
#     #     user = super().save(commit)
#     #     user.set_password(self.cleaned_data["password"])
#     #     user.save()
#     #     return user

#     class Meta:
#         model = Author
#         fields = ("avatar", "username", "first_name", "last_name")




# class AuthorLoginForm(Form):
#     username = CharField(max_length=128)
#     password = CharField(max_length=128, widget=PasswordInput)