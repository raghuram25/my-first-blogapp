from django.db import models
from django.conf import settings
from django.utils import timezone
class Post(models.Model):                   #Post Model(It is like a schema where we declare the columns name(variables here) and datatypes)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)            # is equal to  ---> sql/    text varchar(200);
    text = models.TextField()               
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# Above we can see the while defining the Class 'Post' we gave model.Model in () and below all the datatype declarations are in the form "model.xxxx"
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
