from datetime import timedelta, datetime, date

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince
from ckeditor.fields import RichTextField
import os

# Create your models here.


#from .validators import validate_author_email, validate_justin

#
# class PostModelQuerySet(models.query.QuerySet):
#     def active(self):
#         return self.filter(active=True)
#
#     def post_title_items(self, value):
#         return self.filter(title__icontains=value)
#
#
# class PostModelManager(models.Manager):
#     def get_queryset(self):
#         return PostModelQuerySet(self.model, using=self._db)
#
#     def all(self, *args, **kwargs):
#         #qs = super(PostModelManager, self).all(*args, **kwargs).active() #.filter(active=True)
#         #print(qs)
#         qs = self.get_queryset().active()
#         return qs
#
#     def get_timeframe(self, date1, date2):
#         #assume datetime objects
#         qs = self.get_queryset()
#         qs_time_1 = qs.filter(publish_date__gte=date1)
#         qs_time_2 = qs_time_1.filter(publish_date__lt=date2) # Q Lookups
#         #final_qs = (qs_time_1 | qs_time_2).distinct()
#         return qs_time_2

def path_and_rename(instance, filename):
    return (str(instance)+".jpg")


class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True) #empty in the database
    title           = models.CharField(
                            max_length=240,
                            verbose_name='Post title',
                            unique=True,
                            error_messages={
                                "unique": "This title is not unique, please try again.",
                                "blank": "This field is not full, please try again."
                            },
                            help_text='Must be a unique title.')
    sub_tittle = models.TextField()
    slug            = models.SlugField(null=True, blank=True)
    post_thumbnail  = models.ImageField(default='blog.jpg', upload_to=path_and_rename)
    content         = RichTextField(null=True, blank=True)

    # publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    published       = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug= slugify(self.title)

        super(PostModel, self).save(*args, **kwargs)





    def __str__(self):
        return self.title


class Komentar(models.Model):
    """docstring for Commentar."""

    nama = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    website = models.CharField(max_length=200)
    konten = models.TextField()
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    published       = models.BooleanField(default=True)




    def __str__(self):
        return self.nama


'''
python manage.py makemigrations #every time you change models.py
python manage.py migate


ModelForm
forms.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')

'''
@receiver(models.signals.post_delete, sender=PostModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.post_thumbnail:
        if os.path.isfile(instance.post_thumbnail.path):
            os.remove(instance.post_thumbnail.path)
