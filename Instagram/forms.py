rom django import forms
from .models import Image,Comment
from user.models import Profile


class PhotoUploadModelForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = [ 'title','image','caption']
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comment']        