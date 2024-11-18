from django.db import models


# Create your models here.

class UserInfo(models.Model):
    Name=models.CharField(max_length=300)
    Image=models.ImageField(upload_to='userinfo_image')
    def __str__(self):
        return self.Name
    

class Experience(models.Model):
    date=models.CharField( max_length=300)
    skil=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    description=models.TextField()
    class Meta:
        verbose_name_plural=("Experience")
    def __str__(self):
        return self.skil
    
    

class Education(models.Model):
    date=models.CharField(max_length=300)
    collagename=models.CharField(max_length=300)
    name=models.CharField(max_length=300,null=True,blank=True)
    skill=models.CharField(max_length=300,null=True,blank=True)
    address=models.CharField(max_length=300)
    description=models.TextField()

    class Meta:
        verbose_name_plural=("Education")
        
    def __str__(self):
        return self.collagename
    
    
class ContactInfo(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField()
    Phone_number=models.CharField(max_length=14,null=True,blank=True)
    Massage=models.TextField()
    
    class Meta:
       verbose_name_plural=("ContactInfos") 
    def __str__(self):
        return self.Name
    
class Resume(models.Model):
    name = models.CharField(max_length=300)
    resume_file = models.FileField(upload_to='user_directory_path',blank=True,null=True)
    
    class Meta:
       verbose_name_plural=("Resume") 
    def __str__(self):
        return self.name
    
    