from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    imagefun = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

#create a blog models
# title
# publication date pub_date 
# body
# image 

# add the blog app to the settings

#create a migration

# migrate

#add to the admin
