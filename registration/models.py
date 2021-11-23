from django.db import models

# Create your models here.
class Coursereg(models.Model):
    dateadded = models.DateTimeField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    college = models.TextField()
    dep = models.CharField(max_length=30)
    ystudy = models.CharField(max_length=10)
    contact = models.BigIntegerField()
    mailid = models.EmailField(max_length=200)
    course = models.TextField()
    note = models.TextField()
    cstart = models.DateField(null=True)
    cend = models.DateField(null=True)
    sid = models.CharField(max_length=100,null=True,unique=True)
    chscore = models.IntegerField(default=-1)
    handson = models.IntegerField(default=-1)
    projrepo = models.TextField(null=True)
    
    
    def __str__(self):
        return '{0} from {1} at {2}'.format(self.name,self.college,self.dateadded)