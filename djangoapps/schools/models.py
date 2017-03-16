from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from enum import OrderedDict, unique
from djangoapps.profiles.models import Profile
from multiselectfield import MultiSelectField


# COMMON ENUM
class Day(OrderedDict):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )


class PaymentMethodChoice(OrderedDict):
    VISA = 0
    MASTERCARD = 1
    PAYPAL = 2
    CASH = 3

    PAYMENT_METHOD_CHOICES = (
        (VISA, 'Visa'),
        (MASTERCARD, 'Mastercard'),
        (PAYPAL, 'Paypal'),
        (CASH, 'Cash'),
    )


# COMMON INFO CLASS
class CommonInfo(models.Model):
    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Options')

    class Meta:
        abstract = True


################################################################################################


# SCHOOL IMMERSION CLASS
class Immersion(CommonInfo):
    """ Immersion Model """

    other_option = models.TextField(max_length=5000, blank=True, verbose_name='Other Immersion')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Immersion " + str(self.id)


# SCHOOL TOUR CLASS
class Tour(CommonInfo):
    """ Immersion Model """

    city_tour = models.BooleanField(default=False, verbose_name='City Tour')

    def __str__(self):
        return "Tour " + str(self.id)


# SCHOOL AMENITIES CLASS
class Amenities(CommonInfo):
    """ Amenities Model """

    other_option = models.TextField(max_length=5000, blank=True, verbose_name='Other Amenities')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Amenities " + str(self.id)


################################################################################################


# SCHOOL ACCOMMODATION OPTION CLASS
class AccommodationOption(models.Model):
    """ Accommodation Option Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    category = models.CharField(max_length=200, blank=True, verbose_name='Type of Accommodation')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Accommodation Price')
    amenities = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Amenities')
    other_amenities = models.TextField(max_length=5000, blank=True, verbose_name='Other Amenities')

    def __str__(self):
        return "Accommodation Option " + str(self.id)


# SCHOOL ACCOMMODATION CLASS
class Accommodation(models.Model):
    """ Accommodation Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = models.ForeignKey(AccommodationOption, verbose_name='Accommodation Options')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Accommodation " + str(self.id)


################################################################################################


# SCHOOL VOLUNTEERING CLASS
class Volunteering(CommonInfo):
    """ Volunteering Model """

    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Volunteering " + str(self.id)


# SCHOOL WORK EXCHANGE OPTION CLASS
class WorkExchangeOption(models.Model):
    """ Work Exchange Option Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    category = models.CharField(max_length=200, blank=True, verbose_name='Work Exchange Categories')
    terms = models.TextField(max_length=5000, blank=True, verbose_name='Terms, Details or more information')

    def __str__(self):
        return "Work Exchange Option " + str(self.id)


# SCHOOL WORK EXCHANGE CLASS
class WorkExchange(models.Model):
    """ Work Exchange Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = models.ForeignKey(WorkExchangeOption, verbose_name='Work Exchange Options')

    def __str__(self):
        return "Work Exchange " + str(self.id)


################################################################################################


# COMMON INFO TYPE PRICES CLASS
class CommonInfoType(models.Model):
    active = models.BooleanField(default=False, verbose_name='YES/NO')
    value = models.PositiveSmallIntegerField(default=0, verbose_name='Price (USD)')
    hour = models.PositiveSmallIntegerField(default=0, verbose_name='Hours')
    terms = models.TextField(max_length=5000, blank=True, verbose_name='Terms, Details or more information')

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

    student = ArrayField(models.PositiveSmallIntegerField(default=0), blank=True,
                         verbose_name='Amount of Student per Group')

    def __str__(self):
        return "Group General Type " + str(self.id)


# GROUP INTENSIVE TYPE PRICES CLASS
class GroupIntensiveType(CommonInfoType):
    """ Group Intensive Type Price Model """

    student = ArrayField(models.PositiveSmallIntegerField(default=0), blank=True,
                         verbose_name='Amount of Student per Group')

    def __str__(self):
        return "Group Intensive Type " + str(self.id)


# SCHOOL PRIVATE CLASSES CLASS
class PrivateClass(models.Model):
    """ Private Class Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    general_type = models.OneToOneField(PrivateGeneralType, related_name='private_general_type', on_delete=models.CASCADE,
                                        null=True, verbose_name='General Classes')
    intensive_type = models.OneToOneField(PrivateIntensiveType, related_name='private_intensive_type', on_delete=models.CASCADE,
                                          null=True, verbose_name='Intensive Classes')

    def __str__(self):
        return "Private Class " + str(self.id)


# SCHOOL GROUP CLASSES CLASS
class GroupClass(models.Model):
    """ Group Class Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    general_type = models.OneToOneField(GroupGeneralType, related_name='general_type', on_delete=models.CASCADE,
                                        null=True, verbose_name='General Classes')
    intensive_type = models.OneToOneField(GroupIntensiveType, related_name='intensive_type', on_delete=models.CASCADE,
                                          null=True, verbose_name='Intensive Classes')

    def __str__(self):
        return "Group Class " + str(self.id)


# SCHOOL PRICE CLASS
class Price(models.Model):
    """ Price Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    private = models.OneToOneField(PrivateClass, related_name='private', on_delete=models.CASCADE,
                                   null=True, verbose_name='Private Classes')
    group = models.OneToOneField(GroupClass, related_name='group', on_delete=models.CASCADE,
                                 null=True, verbose_name='Group Classes')

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

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    name = models.CharField(max_length=100, default='', verbose_name='Package Name')
    description = models.TextField(max_length=10000, default='', blank=True, verbose_name='Description')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Package Price (USD)')

    def __str__(self):
        return "Package Option " + str(self.id)


# SCHOOL PACKAGE CLASS
class Package(models.Model):
    """ Package Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = models.ForeignKey(PackageOption, verbose_name='Package Options')

    def __str__(self):
        return "Package " + str(self.id)


################################################################################################


# SCHOOL BOOKING FEE CLASS
class BookingFee(models.Model):
    """ Booking fee Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Value of Booking Fee (USD)')
    terms = models.TextField(max_length=5000, blank=True, verbose_name='Terms, Details or more information')

    def __str__(self):
        return "Bocking Fee " + str(self.id)


################################################################################################


# SCHOOL PAYMENT METHODS CLASS
class PaymentMethod(models.Model):
    """ Payment method Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    methods = MultiSelectField(choices=PaymentMethodChoice.PAYMENT_METHOD_CHOICES,
                               verbose_name='Payment Methods Accepted')
    other = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Other Payment Methods')

    def __str__(self):
        return "Payment Method " + str(self.id)


################################################################################################


# SCHOOL CLASS
class School(models.Model):
    """ School Model """

    user = models.ForeignKey(Profile, verbose_name='School Manager')
    photo = models.TextField(max_length=5000, default='', blank=True, verbose_name='School Photo')
    name = models.CharField(max_length=100, default='', verbose_name='School Name')
    about = models.TextField(max_length=10000, default='', blank=True, verbose_name='About School')
    language_teach = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Languages Teach')
    website = models.CharField(max_length=200, default='', verbose_name='Website')
    facebook = models.CharField(max_length=200, default='', verbose_name='Facebook')
    twitter = models.CharField(max_length=200, default='', verbose_name='Twitter')
    instagram = models.CharField(max_length=200, default='', verbose_name='Instagram')
    email = models.EmailField(max_length=50, verbose_name='Email')
    facebook_group = models.CharField(max_length=200, default='', verbose_name='Group on Facebook')
    meetup_group = models.CharField(max_length=200, default='', verbose_name='Group on Meetup.com')

    immersion = models.OneToOneField(Immersion, related_name='immersion', on_delete=models.CASCADE, null=True,
                                     verbose_name='Immersion')
    language_exchange = models.BooleanField(default=False, verbose_name='Language Exchange')
    tour = models.OneToOneField(Tour, related_name='tour', on_delete=models.CASCADE, null=True, verbose_name='Tours')

    amenities = models.OneToOneField(Amenities, related_name='amenities', on_delete=models.CASCADE, null=True,
                                     verbose_name='Amenities')
    atmosphere = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Atmosphere')

    accommodation = models.OneToOneField(Accommodation, related_name='accommodation', on_delete=models.CASCADE,
                                         null=True, verbose_name='Accommodation')

    volunteering = models.OneToOneField(Volunteering, related_name='volunteering', on_delete=models.CASCADE,
                                        null=True, verbose_name='Volunteering')

    work_exchange = models.OneToOneField(WorkExchange, related_name='work_exchange', on_delete=models.CASCADE,
                                         null=True, verbose_name='Work Exchange')

    price = models.OneToOneField(Price, related_name='price', on_delete=models.CASCADE,
                                 null=True, verbose_name='Prices')

    discount = models.OneToOneField(Discount, related_name='discount', on_delete=models.CASCADE,
                                    null=True, verbose_name='Discounts')

    package = models.OneToOneField(Package, related_name='package', on_delete=models.CASCADE,
                                   null=True, verbose_name='Packages')

    booking_fee = models.OneToOneField(BookingFee, related_name='booking_fee', on_delete=models.CASCADE,
                                       null=True, verbose_name='Booking Fee')

    classes_begin = MultiSelectField(choices=Day.DAY_CHOICES, verbose_name='Classes Begin')

    payment_method = models.OneToOneField(PaymentMethod, related_name='payment_method', on_delete=models.CASCADE,
                                          null=True, verbose_name='Payment Methods')

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

