from statistics import mode
from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    hostel_name=models.CharField(max_length=50)
    room_no=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='uploads/products/',null=True,blank=True)
    lostItem=models.ImageField(upload_to='uploads/lostItems/',null=True,blank=True)
    #   lostItem = models.ImageField(upload_to='uploads/lostItems/', null=True, blank=True)
    item_name=models.CharField(max_length=50,null=True)
    information_about_item=models.CharField(max_length=100,null=True,blank=True)



    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(email):
        try:
          return Student.objects.get(email=email)
        except:
            return False
            
    
    def isExists(self):
        if Student.objects.filter(email=self.email):
            return True
        
        return False