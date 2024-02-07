from django import forms
from .models import mission
from .models import vision, slogan
from .models import pic1, about, whatsets, post1, post2, post3
from .models import obj1, obj2, obj3, obj4, obj5, obj6, obj7, Image

class missionAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = mission
        fields = '__all__'

class visionAdminForm(forms.ModelForm):
    vcontent = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = vision
        fields = '__all__'

class sloganAdminForm(forms.ModelForm):
    slcontent = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = slogan
        fields = '__all__'

class Pic1Form(forms.ModelForm):
    
    class Meta:
        model = pic1
        fields = ['caption', 'image']

class aboutAdminForm(forms.ModelForm):
    abtcontent = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = about
        fields = '__all__'

class whatsetsAdminForm(forms.ModelForm):
    wscontent = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = whatsets
        fields = '__all__'

class post1AdminForm(forms.ModelForm):
    p1content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = post1
        fields = '__all__'

class post2AdminForm(forms.ModelForm):
    p2content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = post2
        fields = '__all__'

class post3AdminForm(forms.ModelForm):
    p3content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = post3
        fields = '__all__'

class obj1AdminForm(forms.ModelForm):
    obj1content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj1
        fields = '__all__'

class obj2AdminForm(forms.ModelForm):
    obj1content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj2
        fields = '__all__'

class obj3AdminForm(forms.ModelForm):
    obj3content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj3
        fields = '__all__'

class obj4AdminForm(forms.ModelForm):
    obj4content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj4
        fields = '__all__'

class obj5AdminForm(forms.ModelForm):
    obj5content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj5
        fields = '__all__'

class obj6AdminForm(forms.ModelForm):
    obj6content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj6
        fields = '__all__'

class obj7AdminForm(forms.ModelForm):
    obj7content = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))

    class Meta:
        model = obj7
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


