from django.db import models
from account.models import StudentProfile
# Create your models here.
class Applicants_CR(models.Model):
    applicant = models.OneToOneField(StudentProfile,on_delete=models.CASCADE)
    dateregisteres= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.applicant)+"_"+str(self.applicant.student_batch)

