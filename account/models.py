from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self,email,password=None,is_active=True,is_student = False, is_teacher = False,is_principal = False ,is_staff=False, is_admin= False):
        if not email:
            raise ValueError("User must have a valid email address")
        if not password:
            raise ValueError("User must have a password")

        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_student = is_student
        user_obj.is_teacher = is_teacher
        user_obj.is_principal = is_principal
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.save(using=self._db)
        return  user_obj


    def create_staffuser(self,email,password):
        user = self.create_user(
            email,
            password,
            is_staff=True
        )
        return user


    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password,
            is_admin=True,
            is_staff=True
        )

        return user


class User(AbstractBaseUser):
    email = models.EmailField(

        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return  self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

#to record the ongoing session :::: 2021-2022
class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return str(self.start_year) + " - " + str(self.end_year)


# to record the course name :::: Maths-6, English-5
class Course(models.Model):
    SUBJECT = (("MATH", "Mathematics"), ("ENG", "English"),
                  ("HINDI", "Hindi"), ("SCI", "Science"))

    name = models.TextField(default=1,choices=SUBJECT)
    class_no = models.IntegerField()

    def __str__(self):
        return str(self.name) +"_"+str(self.class_no)


# to record the batch details :::: Class-6, Class-5
class Batch(models.Model):
    in_class = models.IntegerField(default=None)
    section = models.CharField(max_length=1, default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.in_class) + "-" + self.section



#to store all necessary details of a student
class StudentProfile(models.Model):
    GENDER = (('M','MALE'),('F','FEMALE'))
    # DEPARTMENT = ((1, "Computer Science and Engineering"), (2, "Electronics and Communications Engineering"),
    #               (3, "Electrical Engineering"), (4, "Mechanical Engineering"))

    student = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(default='M',choices=GENDER, max_length=1)
    student_batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # department = models.IntegerField(default=1,choices=DEPARTMENT)
    phone = models.IntegerField()
    dob = models.DateField()




    def __str__(self):
        return self.first_name


# to store all necessary details of a teacher
class TeacherProfile(models.Model):

    GENDER = (('M','MALE'),('F','FEMALE'))
    SUBJECT = (("MATH", "Mathematics"), ("ENG", "English"),
                  ("HINDI", "Hindi"), ("SCI", "Science"))

    department = models.TextField(default=1,choices=SUBJECT)

    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(default='M',choices=GENDER, max_length=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    phone = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.first_name

# making principal account
class Principal(models.Model):
    principal = models.OneToOneField(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.principal.first_name


#to store the courses which a particular batch :::: Class-6:Maths-6
class BatchCourse(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.batch) + " - " + str(self.course.name)


#to connect teacher with a particular BatchCourse :::: Alpa - Class-6 - Maths-6
class TeacherBatchCourse(models.Model):

    teacher_details = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    batchcourse = models.OneToOneField(BatchCourse, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.teacher_details) + " - " + str(self.batchcourse)

# to store unit details of a course :::: Addition
class Unit(models.Model):
    unit_no = models.IntegerField()
    name = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ideallecture = models.IntegerField(default=5)
    def __str__(self):
        return str(self.name)+ " - " + str(self.course.name)


# this will maintain record of completed units of coursebatch

class TrackProgressBatchCourse(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    batchcourse = models.ForeignKey(BatchCourse, on_delete=models.CASCADE,null=True)

    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    students_polled = models.IntegerField(default=0)
    lecture_taken=models.IntegerField(default=0)

    class Meta:
        unique_together = ('unit', 'batchcourse')
    def __str__(self):
        return str(self.unit)+ " - " + str(self.batchcourse)
