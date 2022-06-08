from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.db import models
  
# Create your models here.

class Current_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Our_User")
    voted_position_1 = models.BooleanField(default=False, null=True)
    voted_position_2 = models.BooleanField(default=False, null=True)
    voted_position_3 = models.BooleanField(default=False, null=True)
    voted_position_4 = models.BooleanField(default=False, null=True)
    voted_position_5 = models.BooleanField(default=False, null=True)
    voted_position_6 = models.BooleanField(default=False, null=True)
    voted_position_7 = models.BooleanField(default=False, null=True)
    id = models.CharField(default="User", primary_key=True,  editable=False, max_length=255)

  
  
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
  
    def __str__(self):
        return self.question_text
  
  
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
  
    def __str__(self):
        return self.choice_text