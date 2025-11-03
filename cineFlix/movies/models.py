from django.db import models

import uuid

from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField

# Create your models here.

class BaseClass (models.Model) :

    uuid = models.UUIDField(unique=True,default=uuid.uuid4)

    activate_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 

        abstract = True

class IndustryChoices(models.TextChoices) :

    MOLLYWOOD = 'Mollywood','Mollywood'

    HOLLYWOOD = 'Hollywood','Hollywood'

    BOLLYWOOD = 'Bollywood','Bollywood'

    TOLLYWOOD = 'Tollywood','Tollywood'

class CertificationChoice(models.TextChoices) :

    A = 'A','A'

    UA = 'U/A','U/A'

    U = 'U','U'

    S = 'S','S'


class GenreChoice(models.TextChoices) :

    ACTION = 'Action','Action'

    ROMANTIC = 'Romantic','Romantic'

    THRILLER = 'Thriller','Thriller'

    COMEDY = 'Comedy','Comedy',

    HORROR = 'Horror','Horror'


class ArtistsChoioces(models.TextChoices) :

    MOHANLAL = 'Mohan Lal','Mohan Lal'

    MAMMOOTY = 'Mammotty','Mammootty'

    NIVINPAULY = 'Nivin Pauly','Nivin Pauly'


class LanguageChoices(models.TextChoices) :
    
    MALAYALAM = 'Malayalam','Malayalam'

    ENGLISH = 'English','English'

    HINDI = 'Hindi','Hindi'

    TAMIL = 'Tamil','Tamil'

    TELUGU = 'Telugu','Telugu'

    KANNADA = 'Kannada','Kannada'

class Movie(BaseClass) :

    name = models.CharField(max_length=50)

    photo = models.ImageField(upload_to='movies/banner-images')

    description = models.TextField() 

    release_date = models.DateField()

    industry = models.CharField(max_length=20,choices=IndustryChoices.choices)

    runtime = models.TimeField()

    certification = models.CharField(max_length=5,choices=CertificationChoice.choices)

    genre = MultiSelectField(choices=GenreChoice.choices)

    artists = MultiSelectField(choices=ArtistsChoioces.choices)
    
    video = EmbedVideoField()

    tags = models.TextField()

    languages = MultiSelectField(choices=LanguageChoices.choices)

    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural = 'Movies'

    def _str_(self):
            
        return f'{self.name}'