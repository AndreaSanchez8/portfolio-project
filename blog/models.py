from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=200)
    imagefun = models.ImageField(upload_to='images/')
    

#create a blog models
# title
# publication date pub_date 
# body
# image 

# add the blog app to the settings

#create a migration

# migrate

#add to the admin
