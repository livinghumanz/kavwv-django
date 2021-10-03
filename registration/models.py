from django.db import models

# Create your models here.
class Coursereg(models.Model):
    dateadded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    college = models.TextField()
    dep = models.CharField(max_length=30)
    ystudy = models.CharField(max_length=10)
    contact = models.BigIntegerField()
    mailid = models.EmailField(max_length=200)
    course = models.TextField()
    note = models.TextField()
    
    
    def __str__(self):
        return '{0} from {1}'.format(self.name,self.college)