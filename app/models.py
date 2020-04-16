from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.urls import reverse

User = get_user_model()


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user_name, filename)


class FormFill(models.Model):
    genderChoice = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )
    user_id = models.AutoField(primary_key=True)
    user_name = models.OneToOneField(User, models.CASCADE, unique=True, blank=True)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=255)
    dob = models.DateField('Date of Birth')
    gender = models.CharField(max_length=10, choices=genderChoice, )
    address = models.TextField()

    percent1 = models.CharField(max_length=3, default='0')
    board1 = models.CharField(max_length=255, default='')
    passing_year1 = models.CharField(max_length=4, verbose_name='Passing Year', default='')
    college1 = models.CharField(max_length=255, verbose_name='College/University', default='')

    percent2 = models.CharField(max_length=3, default='0')
    board2 = models.CharField(max_length=255, default='')
    passing_year2 = models.CharField(max_length=4, verbose_name='Passing Year', default='')
    college2 = models.CharField(max_length=255, verbose_name='College/University', default='')

    percent3 = models.CharField(max_length=3, blank=True, default='0')
    board3 = models.CharField(max_length=255, blank=True, default='')
    passing_year3 = models.CharField(max_length=4, verbose_name='Passing Year', blank=True, default='')
    college3 = models.CharField(max_length=255, verbose_name='College/University', blank=True, default='')

    profile_pic = models.ImageField('Profile Picture', upload_to=user_directory_path, )
    doc_1 = models.ImageField('10th Marksheet', upload_to=user_directory_path, )
    doc_2 = models.ImageField('12th Marksheet', upload_to=user_directory_path, )
    doc_3 = models.ImageField('Bachelor Marksheet', upload_to=user_directory_path, )

    courseChoice = (
        ('ba', 'Bachelor of Arts'),
        ('bcom', 'Bachelor of commerce'),
        ('bsc', 'Bachelor of Science'),
        ('bca', 'Bachelor of Computer Application'),
        ('bba', 'Bachelor of Business Administration'),
        ('blis', 'Bachelor of Library Science'),
        ('ma', 'Master of Arts'),
        ('mcom', 'Master of commerce'),
        ('msc', 'Master of Science'),
        ('mca', 'Master of Computer Application'),
        ('mba', 'Master of Business Administration'),
        ('mlis', 'Master of Library Science')
    )
    collegeChoice = (
        ('mgc', 'M. G. College'),
        ('bnc', 'B. N. College'),
        ('nc', 'Nawab College'),
        ('gmc', 'G. M. College'),
        ('hc', 'Hindu College'),
        ('lsc', 'Lalan singh College'),
        ('akc', 'Abdul Kalam College'),
        ('lc', 'Lohia College'),
        ('ac', 'Anugrah College'),
        ('mc', 'Manas College'),
        ('snc', 'S. N. College')
    )

    select_course1 = models.CharField(max_length=50, choices=courseChoice, default='Select Course')
    select_college1 = models.CharField(max_length=50, choices=collegeChoice, default='Select College')

    select_course2 = models.CharField(max_length=50, choices=courseChoice, default='Select Course')
    select_college2 = models.CharField(max_length=50, choices=collegeChoice, default='Select College')

    select_course3 = models.CharField(max_length=50, choices=courseChoice, default='Select Course')
    select_college3 = models.CharField(max_length=50, choices=collegeChoice, default='Select College')

    def __str__(self):
        return str(self.user_name)

    def get_absolute_url(self):
        return reverse('login-page')
