from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator

from djangoapps.profiles.models import Profile


# COMMON INFO CLASS
class CommonInfo(models.Model):
    active = models.BooleanField(default=False)
    option = ArrayField(models.CharField(max_length=200), blank=True)

    class Meta:
        abstract = True


################################################################################################


# SCHOOL IMMERSION CLASS
class Immersion(CommonInfo):
    """ Immersion Model """

    other_option = models.TextField(max_length=5000, blank=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    def __str__(self):
        return "Immersion " + str(self.id)


# SCHOOL TOUR CLASS
class Tour(CommonInfo):
    """ Immersion Model """

    city_tour = models.BooleanField(default=False)

    def __str__(self):
        return "Tour " + str(self.id)


# SCHOOL AMENITIES CLASS
class Amenities(CommonInfo):
    """ Amenities Model """

    other_option = models.TextField(max_length=5000, blank=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    def __str__(self):
        return "Amenities " + str(self.id)


################################################################################################


# SCHOOL ACCOMMODATION OPTION CLASS
class AccommodationOption(models.Model):
    """ Accommodation Option Model """

    active = models.BooleanField(default=False)
    category = models.CharField(max_length=200, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    amenities = ArrayField(models.CharField(max_length=200), blank=True)
    other_amenities = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return "Accommodation Option " + str(self.id)


# SCHOOL ACCOMMODATION CLASS
class Accommodation(models.Model):
    """ Accommodation Model """

    active = models.BooleanField(default=False)
    option = models.ForeignKey(AccommodationOption)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    def __str__(self):
        return "Accommodation " + str(self.id)


################################################################################################


# SCHOOL VOLUNTEERING CLASS
class Volunteering(CommonInfo):
    """ Volunteering Model """

    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    def __str__(self):
        return "Volunteering " + str(self.id)


# SCHOOL WORK EXCHANGE OPTION CLASS
class WorkExchangeOption(models.Model):
    """ Work Exchange Option Model """

    active = models.BooleanField(default=False)
    category = models.CharField(max_length=200, blank=True)
    terms = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return "Work Exchange Option " + str(self.id)


# SCHOOL WORK EXCHANGE CLASS
class WorkExchange(models.Model):
    """ Work Exchange Model """

    active = models.BooleanField(default=False)
    option = models.ForeignKey(WorkExchangeOption)

    def __str__(self):
        return "Work Exchange " + str(self.id)


################################################################################################


# COMMON INFO TYPE PRICES CLASS
class CommonInfoType(models.Model):
    active = models.BooleanField(default=False)
    value = models.PositiveSmallIntegerField(default=0)
    hour = models.PositiveSmallIntegerField(default=0)
    terms = models.TextField(max_length=5000, blank=True)

    class Meta:
        abstract = True


# PRIVATE GENERAL TYPE PRICES CLASS
class PrivateGeneralType(CommonInfoType):
    """ Private General Type Price Model """

    def __str__(self):
        return "Private General Type " + str(self.id)


# PRIVATE INTENSIVE TYPE PRICES CLASS
class PrivateIntensiveType(CommonInfoType):
    """ Private Intensive Type Price Model """

    def __str__(self):
        return "Private Intensive Type " + str(self.id)


# GROUP GENERAL TYPE PRICES CLASS
class GroupGeneralType(CommonInfoType):
    """ Group General Type Price Model """

    student = ArrayField(models.PositiveSmallIntegerField(default=0), blank=True)

    def __str__(self):
        return "Group General Type " + str(self.id)


# GROUP INTENSIVE TYPE PRICES CLASS
class GroupIntensiveType(CommonInfoType):
    """ Group Intensive Type Price Model """

    student = ArrayField(models.PositiveSmallIntegerField(default=0), blank=True)

    def __str__(self):
        return "Group Intensive Type " + str(self.id)


# SCHOOL PRIVATE CLASSES CLASS
class PrivateClass(models.Model):
    """ Private Class Model """

    active = models.BooleanField(default=False)
    general_type = models.OneToOneField(PrivateGeneralType, related_name='private_general_type', on_delete=models.CASCADE,
                                        null=True)
    intensive_type = models.OneToOneField(PrivateIntensiveType, related_name='private_intensive_type', on_delete=models.CASCADE,
                                          null=True)

    def __str__(self):
        return "Private Class " + str(self.id)


# SCHOOL GROUP CLASSES CLASS
class GroupClass(models.Model):
    """ Group Class Model """

    active = models.BooleanField(default=False)
    general_type = models.OneToOneField(GroupGeneralType, related_name='general_type', on_delete=models.CASCADE,
                                        null=True)
    intensive_type = models.OneToOneField(GroupIntensiveType, related_name='intensive_type', on_delete=models.CASCADE,
                                          null=True)

    def __str__(self):
        return "Group Class " + str(self.id)


# SCHOOL PRICE CLASS
class Price(models.Model):
    """ Price Model """

    active = models.BooleanField(default=False)
    private = models.OneToOneField(PrivateClass, related_name='private', on_delete=models.CASCADE,
                                   null=True)
    group = models.OneToOneField(GroupClass, related_name='group', on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return "Price " + str(self.id)


################################################################################################


# SCHOOL DISCOUNT CLASS
class Discount(CommonInfo):
    """ Discount Model """

    def __str__(self):
        return "Discount " + str(self.id)


################################################################################################

# SCHOOL PACKAGE OPTION CLASS
class PackageOption(models.Model):
    """ Package Option Model """

    active = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=10000, default='', blank=True)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "Package Option " + str(self.id)


# SCHOOL PACKAGE CLASS
class Package(models.Model):
    """ Package Model """

    active = models.BooleanField(default=False)
    option = models.ForeignKey(PackageOption)

    def __str__(self):
        return "Package " + str(self.id)


################################################################################################


# SCHOOL BOOKING FEE CLASS
class BookingFee(models.Model):
    """ Booking fee Model """

    active = models.BooleanField(default=False)
    price = models.PositiveSmallIntegerField(default=0)
    terms = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return "Bocking Fee " + str(self.id)


################################################################################################


# SCHOOL PAYMENT METHODS CLASS
class PaymentMethod(models.Model):
    """ Payment method Model """

    active = models.BooleanField(default=False)
    methods = ArrayField(models.CharField(max_length=200), blank=True)
    other = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return "Payment Method " + str(self.id)


################################################################################################


# SCHOOL CLASS
class School(models.Model):
    """ School Model """

    user = models.ForeignKey(Profile)
    photo = models.TextField(max_length=5000, default='', blank=True)
    name = models.CharField(max_length=100, default='')
    about = models.TextField(max_length=10000, default='', blank=True)
    language_teach = ArrayField(models.CharField(max_length=200), blank=True)
    website = models.CharField(max_length=200, default='')
    facebook = models.CharField(max_length=200, default='')
    twitter = models.CharField(max_length=200, default='')
    instagram = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=50)
    facebook_group = models.CharField(max_length=200, default='')
    meetup_group = models.CharField(max_length=200, default='')

    immersion = models.OneToOneField(Immersion, related_name='immersion', on_delete=models.CASCADE, null=True)
    language_exchange = models.BooleanField(default=False)
    tour = models.OneToOneField(Tour, related_name='tour', on_delete=models.CASCADE, null=True)

    amenities = models.OneToOneField(Amenities, related_name='amenities', on_delete=models.CASCADE, null=True)
    atmosphere = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    accommodation = models.OneToOneField(Accommodation, related_name='accommodation', on_delete=models.CASCADE,
                                         null=True)

    volunteering = models.OneToOneField(Volunteering, related_name='volunteering', on_delete=models.CASCADE,
                                        null=True)

    work_exchange = models.OneToOneField(WorkExchange, related_name='work_exchange', on_delete=models.CASCADE,
                                         null=True)

    price = models.OneToOneField(Price, related_name='price', on_delete=models.CASCADE,
                                 null=True)

    discount = models.OneToOneField(Discount, related_name='discount', on_delete=models.CASCADE,
                                    null=True)

    package = models.OneToOneField(Package, related_name='package', on_delete=models.CASCADE,
                                   null=True)

    booking_fee = models.OneToOneField(BookingFee, related_name='booking_fee', on_delete=models.CASCADE,
                                       null=True)

    classes_begin = ArrayField(models.CharField(max_length=200), blank=True)

    payment_method = models.OneToOneField(PaymentMethod, related_name='payment_method', on_delete=models.CASCADE,
                                          null=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['-created_at']

