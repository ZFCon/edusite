from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, user_type, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have an Institution')
		if not user_type:
			raise ValueError('Users must have an Type')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name,
			user_type=user_type,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, user_type, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			first_name=first_name,
			last_name=last_name,
			user_type=user_type,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

SCHOOL = [
    ('HKUST', 'Hong Kong University of Science & Technology'),
    ('HKU', 'University of Hong Kong'),
]


class Account(AbstractBaseUser):
	USER_TYPE_CHOICES = (
		('S', 'Student'),
		('T', 'Teacher'),
		('A', 'Admin'),
  	)
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username		= models.CharField(max_length=10, choices=SCHOOL)
	first_name      = models.CharField(verbose_name="first name", max_length=80, blank=True)
	last_name       = models.CharField(verbose_name="last name", max_length=80, blank=True)
	date_joined		= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	is_staff		= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)
	user_type		= models.CharField(choices=USER_TYPE_CHOICES, max_length=3)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type'] 

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('account-detail', args=[str(self.id)])

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
		

class Student(models.Model):
    user         = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='student_profile')
    student_id   = models.PositiveSmallIntegerField(verbose_name="student id", null=True, blank=True)
    birth_date   = models.DateField(null=True, blank=True)
    first_name   = models.CharField(verbose_name="first name", max_length=80, blank=True)
    last_name    = models.CharField(verbose_name="last name", max_length=80, blank=True)
    institute    = models.ForeignKey('institute.Institute', on_delete=models.SET_NULL, null=True, blank=True, related_name="std_inst")
    school       = models.ForeignKey('school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name="std_sch") 
    department   = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name="std_dpt")
    dptclass     = models.ForeignKey('dptclass.DptClass', on_delete=models.SET_NULL, null=True, blank=True, related_name="std_dptcls")
    status       = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    

class Teacher(models.Model):
    user         = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id      = models.PositiveSmallIntegerField(verbose_name="teacher id", blank=True)
    birth_date      = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.teacher_id)

class OAdmin(models.Model):
    user         = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='admin_profile')
    oadmin_id    = models.PositiveSmallIntegerField(verbose_name="teacher id", blank=True)
    birth_date   = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.user_type == 'S':
            Student.objects.get_or_create(user=instance, first_name=instance.first_name, last_name=instance.last_name)
    elif instance.user_type == 'T':
            Teacher.objects.get_or_create(user=instance)
    else:
            OAdmin.objects.get_or_create(user=instance)
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_account_profile(sender, instance, **kwargs):
    print('-----')
    if instance.user_type == 'S':
            instance.student_profile.save()
    elif instance.user_type == 'T':
            obj, created = Teacher.objects.get_or_ceate(user=instance)
    else:
            OAdmin.objects.get_or_create(user=instance)










