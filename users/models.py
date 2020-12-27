from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    contact = models.CharField(max_length=12,null=True,blank=True)


    def __str__(self):
        return self.user.username


class Institute(models.Model):
    inst_code = models.CharField(unique=True,max_length=10,default=None)
    inst_name = models.CharField(max_length=150)

    def __str__(self):
        return self.inst_name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=10)
    birthdate = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False, null=True)
    position = models.CharField(default=None,blank=True,max_length=10)
    institute = models.CharField(max_length=256)

    def __str__(self):
        return self.user.username
#
# @staticmethod
# def get_institute(inst):
#     return Institute.objects.get(inst_code=inst)




class Notes(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/notes/')

class Question_Papers(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/question_papers/')

class Model_Papers(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/model_papers/')

class Quiz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    question = models.CharField(max_length=250)
    opt1 = models.CharField(max_length=80)
    opt2 = models.CharField(max_length=80)
    opt3 = models.CharField(max_length=80)
    opt4 = models.CharField(max_length=80)
    ans = models.CharField(max_length=80)
    marks = models.SmallIntegerField()
    obtain_marks = models.IntegerField()
    total_marks = models.IntegerField()

