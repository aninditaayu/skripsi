from django import forms
from learning.models import Bab, Materi, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('deskripsi_diri', 'picture')


class BabForm(forms.ModelForm):
    nama = forms.CharField(max_length=128, help_text="Silahkan masukkan Bab")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bab
        fields = ('nama',)


class MateriForm(forms.ModelForm):
    judul_materi = forms.CharField(max_length=128, help_text="Masukkan judul materi")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Materi

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('bab',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

