from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from locations.models import Location
from early.models import Early


class PrivatePriceDetail(models.Model):
    """ Private Classes Price Detail Model """
    uid = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    hour_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.hour_price)


class GroupPriceDetail(models.Model):
    """ Group Classes Price Detail Model """
    uid = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    hour_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.hour_price)


class Price(models.Model):
    """ Price Model """
    uid = models.CharField(max_length=200)
    private_class = models.ForeignKey(PrivatePriceDetail, related_name='private_class', null=True, blank=True)
    group_class = models.ForeignKey(GroupPriceDetail, related_name='group_class', null=True, blank=True)

    def __str__(self):
        return "Price " + str(self.id)


class Language(models.Model):
    """ Language Model """

    uid = models.CharField(max_length=200)
    native = ArrayField(models.CharField(max_length=200), blank=True)
    learn = ArrayField(models.CharField(max_length=200), blank=True)
    teach = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return "Language " + str(self.id)


class Immersion(models.Model):
    """ Immersion Model """

    uid = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    other_category = models.TextField(max_length=5000, blank=True)
    category = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return "Immersion " + str(self.id)


class Teacher(models.Model):
    """ Teacher Model """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    TYPE_CHOICES = (
        ('H', 'Community Tutor'),
        ('P', 'Professional Teacher'),
    )

    NEW = 'NW'
    VALIDATED = 'VA'
    VERIFIED = 'VE'

    STATUSES_CHOICES = (
        (NEW, 'new'),
        (VALIDATED, 'validated'),
        (VERIFIED, 'verified'),
    )

    uid = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=STATUSES_CHOICES, default=NEW)
    recommended = models.IntegerField(null=True, default=0)

    """ Basic Information """
    location = models.ForeignKey(Location, null=True, blank=True)
    languages = models.ForeignKey(Language, null=True, blank=True)
    immersion = models.ForeignKey(Immersion, blank=True)
    price = models.ForeignKey(Price, null=True, blank=True)

    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(max_length=50)
    born = models.CharField(max_length=200)
    about = models.TextField(max_length=10000, blank=True, null=True)
    avatar = models.TextField(max_length=5000, blank=True)

    type = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True, null=True)
    teacher_since = models.CharField(max_length=4, blank=True, null=True)
    methodology = models.TextField(max_length=10000, blank=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Experience(models.Model):
    """ Experience Model """

    uid = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    position = models.CharField(max_length=510, null=True, blank=True)
    company = models.CharField(max_length=510, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=2, blank=True)
    date_start = models.CharField(max_length=4, blank=True)
    date_finish = models.CharField(max_length=4, blank=True)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return "Experience " + str(self.id)


class Education(models.Model):
    """ Education Model """

    uid = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    school = models.CharField(max_length=510, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    field_study = models.CharField(max_length=510, null=True, blank=True)
    date_start = models.CharField(max_length=4, blank=True)
    date_finish = models.CharField(max_length=4, blank=True)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return "Education " + str(self.id)


class Certificate(models.Model):
    """ Certificate Model """

    uid = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    institution = models.CharField(max_length=510, null=True, blank=True)
    date_received = models.CharField(max_length=4, blank=True)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return "Certificate " + str(self.id)


class Rating(models.Model):
    """ Rating Model """
    """ Cada Rating se relaciona con un solo Teacher """

    uid = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher)
    author = models.ForeignKey(Early)
    methodology_value = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0)
    teaching_value = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0)
    communication_value = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0)
    review = models.TextField(max_length=1000, blank=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['-created_at']

