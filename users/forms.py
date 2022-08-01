from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Skill
class CutsomUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name','email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CutsomUserForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            # self.fields['title'].widget.attrs.update({'class':'input'})
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email', 'username', 'location', 'bio', 'short_intro', 'profile_img', 'social_github', 'social_linkedin', 'social_youtube', 'social_twitter']
    # def __init__(self, *args, **kwargs):
    #     super(CutsomUserForm, self).__init__(*args, **kwargs)

    #     for name,field in self.fields.items():
    #         field.widget.attrs.update({'class':'input'})

class Skill(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(Skill, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})