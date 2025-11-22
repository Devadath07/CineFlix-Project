from django import forms

from .models import Movie

import os

class MovieForm(forms.ModelForm):

    class Meta:

        model = Movie

        # fields = ['name','photo']

        # fields = '__all__' 
        # when all fields are getting from form we use this magic method or

        exclude = ['uuid','active_status']

        # for styling
        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Movie Name'}),

            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter movie description'}),

            'release_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'runtime':forms.TimeInput(attrs={'class':'form-control','type':'time'},format='%H:%M'),

            'industry':forms.Select(attrs={'class':'form-select'}),

            'certification':forms.Select(attrs={'class':'form-select'}),

            'genre':forms.SelectMultiple(attrs={'class':'form-select'}),

            'artists':forms.SelectMultiple(attrs={'class':'form-select'}),

            'video':forms.TextInput(attrs={'class':'form-control','type':'url','placehodler':'Enter Video URL'}),

            'tags':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter Tags with #'}),

            'languages':forms.SelectMultiple(attrs={'class':'form-select'})

        }

    def clean(self):

        cleaned_data =  super().clean()

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3*1024*1024:  # 3 is mb and it is converted to byte

            self.add_error('photo','maximum file size upto 3 MB') # to get error first is field of error, next is what is error



