from django.db import models

# Create your models here.

CATEGORY=(
    ('3','SPORTS'),
    ('2','NATIONAL'),
    ('1','INTERNATIONAL')
)



class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads')
    category = models.CharField(max_length=1,choices=CATEGORY, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.title)
    


    




