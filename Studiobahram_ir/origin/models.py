import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateField()
    picture = models.ImageField(upload_to="posts/pics/%Y/%m/%d/",default="posts/pics/%Y/%m/%d/img.jpg")
    file_post = models.FileField(upload_to="posts/files/%Y/%m/%d/",default="posts/files/%Y/%m/%d/file")
    about_post = models.TextField(help_text="Writeing about post ...")
    github_url = models.URLField(max_length=300,default="https://github.com/")
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Instruction(models.Model):
    title = models.CharField(max_length=400,name="Instruction Title")
    pub_date = models.DateField()
    instruction_text = models.TextField(help_text="Writeing text Instruction ...",name="Instruction Text")
    youtube_url = models.URLField(name="YOUTUBE URL")
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




    


    