from enum import OrderedDict, unique


######################################################################################
#  COMMON ENUM
######################################################################################


# DAYS
class Day(OrderedDict):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )


# PAYMENT METHODS
class PaymentMethodChoice(OrderedDict):
    VISA = 1
    MASTERCARD = 2
    PAYPAL = 3
    CASH = 4

    PAYMENT_METHOD_CHOICES = (
        (VISA, 'Visa'),
        (MASTERCARD, 'Mastercard'),
        (PAYPAL, 'Paypal'),
        (CASH, 'Cash'),
    )


# IMMERSION CATEGORIES
class ImmersionCategories(OrderedDict):

    ACTIVITIESWITHLOCALS = 1
    BARISTA = 2
    BEERTASTING = 3
    CHOCOLATETASTING = 4
    PUBCRAWL = 5
    FOODTASTING = 6
    DANCECLASS = 7

    IMMERSION_CHOICES = (
        (ACTIVITIESWITHLOCALS, 'Games and activities with local'),
        (BARISTA, 'Coffee tasting experience'),
        (BEERTASTING, 'Beer tasting experience'),
        (CHOCOLATETASTING, 'Chocolate tasting experience'),
        (PUBCRAWL, 'Pub crawl'),
        (FOODTASTING, 'Local food tasting'),
        (DANCECLASS, 'Local dance class'),
    )


# SCHOOL AMENITIES
class AmenitiesSchoolCategories(OrderedDict):

    WIRELESSINTERNET = 1
    LAPTOPWORKSPACE = 2
    AIRCONDITIONING = 3
    HEATING = 4
    BREAKFAST = 5
    LUNCH = 6
    DINNER = 7
    SNACK = 8
    COFFEE = 9
    TEA = 10
    HAMMOCKS = 11
    CLASSROOMS = 12
    COMPUTERSROOM = 13
    VIDEOPROJECTOR = 14
    LOUNGEAREA = 15

    AMENITIES_SCHOOL_CHOICES = (
        (WIRELESSINTERNET, 'Wireless Internet'),
        (LAPTOPWORKSPACE, 'Laptop friendly workspace'),
        (AIRCONDITIONING, 'Air conditioning'),
        (HEATING, 'Heating'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACK, 'Snack'),
        (COFFEE, 'Coffee'),
        (TEA, 'Tea'),
        (HAMMOCKS, 'Hammocks'),
        (CLASSROOMS, 'Classrooms'),
        (COMPUTERSROOM, 'Computers room'),
        (VIDEOPROJECTOR, 'Video projector'),
        (LOUNGEAREA, 'Lounge area'),
    )


# ACCOMMODATION AMENITIES
class AmenitiesAccommodationCategories(OrderedDict):

    PRIVATEROOM = 1
    SHAREDROOM = 2
    PRIVATEBATHROOM = 3
    BREAKFAST = 4
    LUNCH = 5
    DINNER = 6
    SNACK = 7
    COFFEE = 8
    TEA = 9
    WIRELESSINTERNET = 10
    CLOSETOSCHOOL = 11
    WASHER = 12
    CABLETV = 13
    TV = 14
    KITCHEN = 15

    AMENITIES_ACCOMMODATION_CHOICES = (
        (PRIVATEROOM, 'Private room'),
        (SHAREDROOM, 'Shared room'),
        (PRIVATEBATHROOM, 'Private bathroom'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACK, 'Snack'),
        (COFFEE, 'Coffee'),
        (TEA, 'Tea'),
        (WIRELESSINTERNET, 'Wireless Internet'),
        (CLOSETOSCHOOL, 'Close to school'),
        (WASHER, 'Washer'),
        (CABLETV, 'Cable TV'),
        (TV, 'TV'),
        (KITCHEN, 'Kitchen'),
    )


# ACCOMMODATION CATEGORY
class AccommodationCategories(OrderedDict):

    HOMESTAY = 1
    LOCALHOST = 2
    HOSTEL = 3
    SHAREDAPARTMENT = 4
    PRIVATEAPARTMENT = 5

    ACCOMMODATION_CHOICES = (
        (HOMESTAY, 'Homestay'),
        (LOCALHOST, 'Live with a local host'),
        (HOSTEL, 'Hostel'),
        (SHAREDAPARTMENT, 'Shared Apartment'),
        (PRIVATEAPARTMENT, 'Private Apartment'),
    )


# WORK EXCHANGES OPTIONS
class WorkExchangesOptions(OrderedDict):
    ACCOMMODATION = 1
    DISCOUNTINCLASSES = 2

    HOSTEL = 3
    SHAREDAPARTMENT = 4
    PRIVATEAPARTMENT = 5
    BREAKFAST = 6
    LUNCH = 7
    DINNER = 8

    WORK_EXCHANGE_CHOICES = (
        (ACCOMMODATION, 'Accommodation'),
        (DISCOUNTINCLASSES, 'Discount in classes'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
