from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from djangoapps.profiles.models import Profile
from djangoapps.locations.models import Location
from djangoapps.globals.enums.models import Day, PaymentMethodChoice, ImmersionCategories, AmenitiesSchoolCategories, \
    AmenitiesAccommodationCategories, AccommodationCategories, WorkExchangesOptions, LanguagesList
from multiselectfield import MultiSelectField


# COMMON INFO CLASS
class CommonInfo(models.Model):
    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Options')

    class Meta:
        abstract = True


################################################################################################


# SCHOOL IMMERSION CLASS
class Immersion(models.Model):
    """ Immersion Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = MultiSelectField(choices=ImmersionCategories.IMMERSION_CHOICES,
                              verbose_name='Immersion options')
    other_option = models.TextField(max_length=5000, blank=True, verbose_name='Other Immersion')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Immersion " + str(self.id)


# SCHOOL TOUR CLASS
class Tour(models.Model):
    """ Immersion Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Tours Options',
                        help_text='Write each tour option, separated by commas')
    city_tour = models.BooleanField(default=False, verbose_name='City Tour')

    def __str__(self):
        return "Tour " + str(self.id)


# SCHOOL AMENITIES CLASS
class Amenities(models.Model):
    """ Amenities Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = MultiSelectField(choices=AmenitiesSchoolCategories.AMENITIES_SCHOOL_CHOICES,
                              verbose_name='Amenities options')
    other_option = models.TextField(max_length=5000, blank=True, verbose_name='Other Amenities')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Amenities " + str(self.id)


################################################################################################


# SCHOOL ACCOMMODATION CLASS
class Accommodation(models.Model):
    """ Accommodation Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Accommodation " + str(self.id)


# SCHOOL ACCOMMODATION OPTION CLASS
class AccommodationOption(models.Model):
    """ Accommodation Option Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    accommodation = models.ForeignKey(Accommodation, verbose_name='Accommodation Options')
    category = models.IntegerField(choices=AccommodationCategories.ACCOMMODATION_CHOICES, blank=True, default=1,
                                   verbose_name='Type of Accommodation')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Accommodation Price per week (USD)')
    amenities = MultiSelectField(choices=AmenitiesAccommodationCategories.AMENITIES_ACCOMMODATION_CHOICES,
                                 verbose_name='Amenities options')
    other_amenities = models.TextField(max_length=5000, blank=True, verbose_name='Other Amenities')

    terms = models.TextField(max_length=5000, blank=True, verbose_name='Terms, Details or more information')

    def __str__(self):
        return "Accommodation Option " + str(self.id)


################################################################################################


# SCHOOL VOLUNTEERING CLASS
class Volunteering(models.Model):
    """ Volunteering Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Volunteering Options',
                        help_text='Write each volunteering option, separated by commas')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Rating')

    def __str__(self):
        return "Volunteering " + str(self.id)


# SCHOOL WORK EXCHANGE CLASS
class WorkExchange(models.Model):
    """ Work Exchange Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')

    def __str__(self):
        return "Work Exchange " + str(self.id)


# SCHOOL WORK EXCHANGE OPTION CLASS
class WorkExchangeOption(models.Model):
    """ Work Exchange Option Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    work_exchange = models.ForeignKey(WorkExchange, null=True, blank=True, verbose_name='Work Exchange Options')
    category = models.IntegerField(choices=WorkExchangesOptions.WORK_EXCHANGE_CHOICES, blank=True, default=1,
                                   verbose_name='Work Exchange Categories')
    terms = models.TextField(max_length=5000, blank=True, verbose_name='Terms, Details or more information')

    def __str__(self):
        return "Work Exchange Option " + str(self.id)


################################################################################################


# COMMON INFO TYPE PRICES CLASS
class CommonInfoType(models.Model):
    active = models.BooleanField(default=False, verbose_name='YES/NO')
    value = models.PositiveSmallIntegerField(default=0, verbose_name='Price (USD) per week')
    hour = models.PositiveSmallIntegerField(default=0, verbose_name='Hours per week')
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
                         verbose_name='Amount of Student per Group',
                         help_text='Use follow format: minimum value, maximum value', size=2)

    def __str__(self):
        return "Group General Type " + str(self.id)


# GROUP INTENSIVE TYPE PRICES CLASS
class GroupIntensiveType(CommonInfoType):
    """ Group Intensive Type Price Model """

    student = ArrayField(models.PositiveSmallIntegerField(default=0), blank=True,
                         verbose_name='Amount of Student per Group',
                         help_text='Use follow format: minimum value, maximum value', size=2)

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
    private_class = models.OneToOneField(PrivateClass, related_name='private', on_delete=models.CASCADE,
                                         null=True, verbose_name='Private Classes')
    group_class = models.OneToOneField(GroupClass, related_name='group', on_delete=models.CASCADE,
                                       null=True, verbose_name='Group Classes')

    def __str__(self):
        return "Price " + str(self.id)


################################################################################################


# SCHOOL DISCOUNT CLASS
class Discount(models.Model):
    """ Discount Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    option = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Discount Options',
                        help_text='Write each discount option, separated by commas')

    def __str__(self):
        return "Discount " + str(self.id)


################################################################################################


# SCHOOL PACKAGE CLASS
class Package(models.Model):
    """ Package Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')

    def __str__(self):
        return "Package " + str(self.id)


# SCHOOL PACKAGE OPTION CLASS
class PackageOption(models.Model):
    """ Package Option Model """

    active = models.BooleanField(default=False, verbose_name='YES/NO')
    package = models.ForeignKey(Package, verbose_name='Package Options')
    name = models.CharField(max_length=100, default='', verbose_name='Package Name')
    description = models.TextField(max_length=10000, default='', blank=True, verbose_name='Description')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Package Price (USD)')

    def __str__(self):
        return "Package Option " + str(self.id)


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
                               verbose_name='Payment Methods Accepted', )
    other = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Other Payment Methods',
                       help_text='Write each payment method, separated by commas')

    def __str__(self):
        return "Payment Method " + str(self.id)


################################################################################################


# SCHOOL CLASS
class School(models.Model):
    """ School Model """

    NEW = 'NW'
    VALIDATED = 'VA'
    VERIFIED = 'VE'

    STATUSES_CHOICES = (
        (NEW, 'new'),
        (VALIDATED, 'validated'),
        (VERIFIED, 'verified'),
    )

    user = models.ForeignKey(Profile, verbose_name='School Manager')
    status = models.CharField(max_length=2, choices=STATUSES_CHOICES, default=VALIDATED)
    photo = models.TextField(max_length=5000, default='', blank=True, verbose_name='School Photo')
    name = models.CharField(max_length=100, default='', verbose_name='School Name')
    about = models.TextField(max_length=10000, default='', blank=True, verbose_name='About School')
    phone_number = models.CharField(max_length=30, default='', blank=True)
    language_teach = MultiSelectField(choices=LanguagesList.LANGUAGE_CHOICES,
                                      verbose_name='Languages Teach')
    website = models.CharField(max_length=200, default='', blank=True, verbose_name='Website')
    facebook = models.CharField(max_length=200, default='', blank=True, verbose_name='Facebook')
    twitter = models.CharField(max_length=200, default='', blank=True, verbose_name='Twitter')
    instagram = models.CharField(max_length=200, default='', blank=True, verbose_name='Instagram')
    email = models.EmailField(max_length=50, verbose_name='Email', default='', blank=True)
    facebook_group = models.CharField(max_length=200, default='',  blank=True, verbose_name='Group on Facebook')
    meetup_group = models.CharField(max_length=200, default='', blank=True, verbose_name='Group on Meetup.com')

    location = models.OneToOneField(Location, related_name='school_location', on_delete=models.CASCADE, null=True,
                                    verbose_name='School Location')

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

    classes_begin = MultiSelectField(choices=Day.DAY_CHOICES, verbose_name='Classes Begin', blank=True, default='')

    payment_method = models.OneToOneField(PaymentMethod, related_name='payment_method', on_delete=models.CASCADE,
                                          null=True, verbose_name='Payment Methods')

    active = models.BooleanField(default=False, verbose_name='Active')

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

