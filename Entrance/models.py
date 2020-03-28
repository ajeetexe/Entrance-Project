from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class UserInfoModel(models.Model):
    # for choices
    genderChoice = (
        ('m','Male'),
        ('f','Female'),
        ('o','Other'),
    )
    
    # For user Info
    userName = models.CharField('User Name',max_length=20,primary_key=True )
    firstName = models.CharField('First Name',max_length=50)
    lastName = models.CharField('Last Name',max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=genderChoice)
    dob = models.DateField('Date Of Birth')
    fullAddress = models.CharField(max_length=255)

    def __str__(self):
        return str(self.userName)

    def get_absolute_url(self):
        return  reverse('qualify') 
class QualificationModel(models.Model):
    
    degreeChoice = (
        ('mat','Matriculation/10th'),
        ('int','Intermidiate/12th'),
        ('ug','Under Graduate'),
        ('pg','Post Graduate')
    )
    # For Qualification
    userName = models.ForeignKey(UserInfoModel,on_delete=models.CASCADE,)
    degree1 = models.CharField('Degree/Class',max_length=10,choices=degreeChoice)
    percentage1 = models.PositiveSmallIntegerField('Percentage')
    passYear1 = models.PositiveSmallIntegerField('Passing Year')
    university1 = models.CharField('University/College',max_length=50)
    board1 = models.CharField('Board',max_length=50)

    degree2 = models.CharField(max_length=10,choices=degreeChoice)
    percentage2 = models.PositiveSmallIntegerField('Percentage')
    passYear2 = models.PositiveSmallIntegerField('Passing Year')
    university2 = models.CharField('University/College',max_length=50)
    board2 = models.CharField('Board',max_length=50)

    degree3 = models.CharField(max_length=10,choices=degreeChoice)
    percentage3 = models.PositiveSmallIntegerField('Percentage')
    passYear3 = models.PositiveSmallIntegerField('Passing Year')
    university3 = models.CharField('University/College',max_length=50)
    board3 = models.CharField('Board',max_length=50)
    

    def __str__(self):
        return str(self.userName)

    def get_absolute_url(self):
        return  reverse('documentupload')

class DocumentUploadModel(models.Model):
    # for document upload
    userName = models.ForeignKey(UserInfoModel,on_delete=models.CASCADE,)
    pic1 = models.ImageField('Upload Your Picture',upload_to="UserInfoModel.userName")
    pic2 = models.ImageField('10th Marksheet',upload_to="UserInfoModel.userName")
    pic3 = models.ImageField('12th Marksheet',upload_to="UserInfoModel.userName")
    pic4 = models.ImageField('Graduation Marksheet',upload_to="UserInfoModel.userName")
    
    
    def __str__(self):
        return str(self.userName)

    def get_absolute_url(self):
        return  reverse('preference')
class PreferenceModel(models.Model):
    courseChoice = (
        ('ba','Bechelor of Arts'),
        ('bcom','Bechalor of commerce'),
        ('bsc','Bechelor of Science'),
        ('bca','Bechelor of Computer Application'),
        ('bba','Bechelor of Bussiness Administration'),
        ('blis','Bechelor of Library Science'),
        ('ma','Master of Arts'),
        ('mcom','Master of commerce'),
        ('msc','Master of Science'),
        ('mca','Master of Computer Application'),
        ('mba','Master of Bussiness Administration'),
        ('mlis','Master of Library Science')
    )
    collegeChoice = (
        ('mgc','M. G. College'),
        ('bnc','B. N. College'),
        ('nc','Nawab College'),
        ('gmc','G. M. College'),
        ('hc','Hindu College'),
        ('lsc','Lalan singh College'),
        ('akc','Abdul Kalam College'),
        ('lc','Lohia College'),
        ('ac','Anugrah College'),
        ('mc','Manas College'),
        ('snc','S. N. College')
    )
    # for preference selection
    userName = models.ForeignKey(UserInfoModel,on_delete=models.CASCADE,)
    course1 = models.CharField('Course',max_length=10,choices=courseChoice, default=courseChoice[0])
    college1 =models.CharField('College',max_length=20,choices=collegeChoice,default=collegeChoice[0])

    course2 = models.CharField('Course',max_length=10,choices=courseChoice,default=courseChoice[0])
    college2 =models.CharField('College',max_length=20,choices=collegeChoice,default=collegeChoice[0])

    course3 = models.CharField('Course',max_length=10,choices=courseChoice,default=courseChoice[0])
    college3 =models.CharField('College',max_length=20,choices=collegeChoice,default=collegeChoice[0])
    
    def __str__(self):
        return str(self.userName)


    def get_absolute_url(self):
        return  reverse('user_profile')