from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
        STUDENT = "ST"
        PARENT = "PT" 	
        # STUDENT/PARENT kan me kon qysh ruhen n'databaz a "Student" "Parent" 
        # kan me kon qysh dalin n'admin
        account_type_options = (
                        (STUDENT,"Student"),
                        (PARENT,"Parent"),
                )
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        account_type = models.CharField(max_length=2,
                                        choices=account_type_options)
        def __str__(self):
                string = "{} {} ".format(self.user.first_name,
                                         self.user.last_name)
                if self.account_type == STUDENT:
                        return string + "Student"
                else:
                        return string + "Parent"
