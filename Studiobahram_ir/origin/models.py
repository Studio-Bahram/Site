from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=400)
    picture = models.ImageField(upload_to="posts/pics/%Y/%m/%d/",default="posts/pics/%Y/%m/%d/img.jpg")
    file_post = models.FileField(upload_to="posts/files/%Y/%m/%d/",default="posts/files/%Y/%m/%d/file")
    about_post = models.TextField(help_text="Writeing about post ...")
    github_url = models.URLField(max_length=300,default="https://github.com/")

    def __str__(self):
        return self.title