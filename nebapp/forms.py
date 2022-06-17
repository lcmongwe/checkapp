from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


from django.forms import ModelForm
from .models import *


# CREATE POST FORM
class CreatePostForm(ModelForm):
    class Meta:
        model= Post
        # fields= "__all__"
        fields=('title', 'description', 'location','image'  )

        labels={
            'title': 'Title',
            'description':'description',
            'location':'location',
            'image':'image',     
        }

        widgets={
           'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'  title '}),
           'description':forms.TextInput(attrs={'class': 'form-control','placeholder':'description'}),
           'image':forms.URLInput(attrs={'class': 'form-control','placeholder':'enter url'}),

        }





# authentication forms
class RegisterUserForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','name','image','email','location','password1','password2')

    def __init__(self, *args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
