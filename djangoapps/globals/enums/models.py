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


# COUNTRIES LIST
class CountriesList(OrderedDict):

    AF = 'AF'
    AX = 'AX'
    AL = 'AL'
    DZ = 'DZ'
    AS = 'AS'
    AD = 'AD'
    AO = 'AO'
    AI = 'AI'
    AG = 'AG'
    AR = 'AR'
    AM = 'AM'
    AW = 'AW'
    AU = 'AU'
    AT = 'AT'
    AZ = 'AZ'
    BS = 'BS'
    BH = 'BH'
    BD = 'BD'
    BB = 'BB'
    BY = 'BY'
    BE = 'BE'
    BZ = 'BZ'
    BJ = 'BJ'
    BM = 'BM'
    BT = 'BT'
    BO = 'BO'
    BA = 'BA'
    BW = 'BW'
    BR = 'BR'
    IO = 'IO'
    VG = 'VG'
    BN = 'BN'
    BG = 'BG'
    BF = 'BF'
    BI = 'BI'
    KH = 'KH'
    CM = 'CM'
    CA = 'CA'
    CV = 'CV'
    BQ = 'BQ'
    KY = 'KY'
    CF = 'CF'
    TD = 'TD'
    CL = 'CL'
    CN = 'CN'
    CX = 'CX'
    CC = 'CC'
    CO = 'CO'
    KM = 'KM'
    CG = 'CG'
    CK = 'CK'
    CR = 'CR'
    HR = 'HR'
    CU = 'CU'
    CW = 'CW'
    CY = 'CY'
    CZ = 'CZ'
    CD = 'CD'
    DK = 'DK'
    DJ = 'DJ'
    DM = 'DM'
    DO = 'DO'
    TL = 'TL'
    EC = 'EC'
    EG = 'EG'
    SV = 'SV'
    GQ = 'GQ'
    ER = 'ER'
    EE = 'EE'
    ET = 'ET'
    FK = 'FK'
    FO = 'FO'
    FJ = 'FJ'
    FI = 'FI'
    FR = 'FR'
    GF = 'GF'
    PF = 'PF'
    GA = 'GA'
    GM = 'GM'
    GE = 'GE'
    DE = 'DE'
    GH = 'GH'
    GI = 'GI'
    GR = 'GR'
    GL = 'GL'
    GD = 'GD'
    GP = 'GP'
    GU = 'GU'
    GT = 'GT'
    GG = 'GG'
    GN = 'GN'
    GW = 'GW'
    GY = 'GY'
    HT = 'HT'
    HN = 'HN'
    HK = 'HK'
    HU = 'HU'
    IS = 'IS'
    IN = 'IN'
    ID = 'ID'
    IQ = 'IQ'
    IE = 'IE'
    IM = 'IM'
    IL = 'IL'
    IT = 'IT'
    CI = 'CI'
    JM = 'JM'
    JP = 'JP'
    JE = 'JE'
    JO = 'JO'
    KZ = 'KZ'
    KE = 'KE'
    KI = 'KI'
    KW = 'KW'
    KG = 'KG'
    LA = 'LA'
    LV = 'LV'
    LB = 'LB'
    LS = 'LS'
    LR = 'LR'
    LY = 'LY'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    MO = 'MO'
    MK = 'MK'
    MG = 'MG'
    MW = 'MW'
    MY = 'MY'
    MV = 'MV'
    ML = 'ML'
    MT = 'MT'
    MH = 'MH'
    MQ = 'MQ'
    MR = 'MR'
    MU = 'MU'
    YT = 'YT'
    MX = 'MX'
    FM = 'FM'
    MD = 'MD'
    MC = 'MC'
    MN = 'MN'
    ME = 'ME'
    MS = 'MS'
    MA = 'MA'
    MZ = 'MZ'
    MM = 'MM'
    NA = 'NA'
    NR = 'NR'
    NP = 'NP'
    NL = 'NL'
    NC = 'NC'
    NZ = 'NZ'
    NI = 'NI'
    NE = 'NE'
    NG = 'NG'
    NU = 'NU'
    NF = 'NF'
    MP = 'MP'
    NO = 'NO'
    OM = 'OM'
    PK = 'PK'
    PW = 'PW'
    PS = 'PS'
    PA = 'PA'
    PG = 'PG'
    PY = 'PY'
    PE = 'PE'
    PH = 'PH'
    PN = 'PN'
    PL = 'PL'
    PT = 'PT'
    PR = 'PR'
    QA = 'QA'
    RE = 'RE'
    RO = 'RO'
    RU = 'RU'
    RW = 'RW'
    BL = 'BL'
    SH = 'SH'
    KN = 'KN'
    LC = 'LC'
    MF = 'MF'
    PM = 'PM'
    VC = 'VC'
    WS = 'WS'
    SM = 'SM'
    ST = 'ST'
    SA = 'SA'
    SN = 'SN'
    RS = 'RS'
    SC = 'SC'
    SL = 'SL'
    SG = 'SG'
    SX = 'SX'
    SK = 'SK'
    SI = 'SI'
    SB = 'SB'
    SO = 'SO'
    ZA = 'ZA'
    GS = 'GS'
    KR = 'KR'
    SS = 'SS'
    ES = 'ES'
    LK = 'LK'
    SR = 'SR'
    SJ = 'SJ'
    SZ = 'SZ'
    SE = 'SE'
    CH = 'CH'
    TW = 'TW'
    TJ = 'TJ'
    TZ = 'TZ'
    TH = 'TH'
    TG = 'TG'
    TK = 'TK'
    TO = 'TO'
    TT = 'TT'
    TN = 'TN'
    TR = 'TR'
    TM = 'TM'
    TC = 'TC'
    TV = 'TV'
    VI = 'VI'
    UG = 'UG'
    UA = 'UA'
    AE = 'AE'
    GB = 'GB'
    US = 'US'
    UY = 'UY'
    UZ = 'UZ'
    VU = 'VU'
    VA = 'VA'
    VE = 'VE'
    VN = 'VN'
    WF = 'WF'
    EH = 'EH'
    YE = 'YE'
    ZM = 'ZM'
    ZW = 'ZW'

    COUNTRIESLIST_CHOICES = (
        (AF, 'Afghanistan'),
        (AX, 'Åland Islands'),
        (AL, 'Albania'),
        (DZ, 'Algeria'),
        (AS, 'American Samoa'),
        (AD, 'Andorra'),
        (AO, 'Angola'),
        (AI, 'Anguilla'),
        (AG, 'Antigua and Barbuda'),
        (AR, 'Argentina'),
        (AM, 'Armenia'),
        (AW, 'Aruba'),
        (AU, 'Australia'),
        (AT, 'Austria'),
        (AZ, 'Azerbaijan'),
        (BS, 'Bahamas'),
        (BH, 'Bahrain'),
        (BD, 'Bangladesh'),
        (BB, 'Barbados'),
        (BY, 'Belarus'),
        (BE, 'Belgium'),
        (BZ, 'Belize'),
        (BJ, 'Benin'),
        (BM, 'Bermuda'),
        (BT, 'Bhutan'),
        (BO, 'Bolivia'),
        (BA, 'Bosnia and Herzegovina'),
        (BW, 'Botswana'),
        (BR, 'Brazil'),
        (IO, 'British Indian Ocean Territory'),
        (VG, 'British Virgin Islands'),
        (BN, 'Brunei'),
        (BG, 'Bulgaria'),
        (BF, 'Burkina Faso'),
        (BI, 'Burundi'),
        (KH, 'Cambodia'),
        (CM, 'Cameroon'),
        (CA, 'Canada'),
        (CV, 'Cape Verde'),
        (BQ, 'Caribbean Netherlands'),
        (KY, 'Cayman Islands'),
        (CF, 'Central African Republic'),
        (TD, 'Chad'),
        (CL, 'Chile'),
        (CN, 'China'),
        (CX, 'Christmas Island'),
        (CC, 'Cocos [Keeling] Islands'),
        (CO, 'Colombia'),
        (KM, 'Comoros'),
        (CG, 'Congo'),
        (CK, 'Cook Islands'),
        (CR, 'Costa Rica'),
        (HR, 'Croatia'),
        (CU, 'Cuba'),
        (CW, 'Curaçao'),
        (CY, 'Cyprus'),
        (CZ, 'Czech Republic'),
        (CD, 'Democratic Republic of the Congo'),
        (DK, 'Denmark'),
        (DJ, 'Djibouti'),
        (DM, 'Dominica'),
        (DO, 'Dominican Republic'),
        (TL, 'East Timor'),
        (EC, 'Ecuador'),
        (EG, 'Egypt'),
        (SV, 'El Salvador'),
        (GQ, 'Equatorial Guinea'),
        (ER, 'Eritrea'),
        (EE, 'Estonia'),
        (ET, 'Ethiopia'),
        (FK, 'Falkland Islands [Islas Malvinas]'),
        (FO, 'Faroe Islands'),
        (FJ, 'Fiji'),
        (FI, 'Finland'),
        (FR, 'France'),
        (GF, 'French Guiana'),
        (PF, 'French Polynesia'),
        (GA, 'Gabon'),
        (GM, 'Gambia'),
        (GE, 'Georgia'),
        (DE, 'Germany'),
        (GH, 'Ghana'),
        (GI, 'Gibraltar'),
        (GR, 'Greece'),
        (GL, 'Greenland'),
        (GD, 'Grenada'),
        (GP, 'Guadeloupe'),
        (GU, 'Guam'),
        (GT, 'Guatemala'),
        (GG, 'Guernsey'),
        (GN, 'Guinea'),
        (GW, 'Guinea-Bissau'),
        (GY, 'Guyana'),
        (HT, 'Haiti'),
        (HN, 'Honduras'),
        (HK, 'Hong Kong'),
        (HU, 'Hungary'),
        (IS, 'Iceland'),
        (IN, 'India'),
        (ID, 'Indonesia'),
        (IQ, 'Iraq'),
        (IE, 'Ireland'),
        (IM, 'Isle of Man'),
        (IL, 'Israel'),
        (IT, 'Italy'),
        (CI, 'Ivory Coast'),
        (JM, 'Jamaica'),
        (JP, 'Japan'),
        (JE, 'Jersey'),
        (JO, 'Jordan'),
        (KZ, 'Kazakhstan'),
        (KE, 'Kenya'),
        (KI, 'Kiribati'),
        (KW, 'Kuwait'),
        (KG, 'Kyrgyzstan'),
        (LA, 'Laos'),
        (LV, 'Latvia'),
        (LB, 'Lebanon'),
        (LS, 'Lesotho'),
        (LR, 'Liberia'),
        (LY, 'Libya'),
        (LI, 'Liechtenstein'),
        (LT, 'Lithuania'),
        (LU, 'Luxembourg'),
        (MO, 'Macau'),
        (MK, 'Macedonia'),
        (MG, 'Madagascar'),
        (MW, 'Malawi'),
        (MY, 'Malaysia'),
        (MV, 'Maldives'),
        (ML, 'Mali'),
        (MT, 'Malta'),
        (MH, 'Marshall Islands'),
        (MQ, 'Martinique'),
        (MR, 'Mauritania'),
        (MU, 'Mauritius'),
        (YT, 'Mayotte'),
        (MX, 'Mexico'),
        (FM, 'Micronesia'),
        (MD, 'Moldova'),
        (MC, 'Monaco'),
        (MN, 'Mongolia'),
        (ME, 'Montenegro'),
        (MS, 'Montserrat'),
        (MA, 'Morocco'),
        (MZ, 'Mozambique'),
        (MM, 'Myanmar [Burma]'),
        (NA, 'Namibia'),
        (NR, 'Nauru'),
        (NP, 'Nepal'),
        (NL, 'Netherlands'),
        (NC, 'New Caledonia'),
        (NZ, 'New Zealand'),
        (NI, 'Nicaragua'),
        (NE, 'Niger'),
        (NG, 'Nigeria'),
        (NU, 'Niue'),
        (NF, 'Norfolk Island'),
        (MP, 'Northern Mariana Islands'),
        (NO, 'Norway'),
        (OM, 'Oman'),
        (PK, 'Pakistan'),
        (PW, 'Palau'),
        (PS, 'Palestinian Territories'),
        (PA, 'Panama'),
        (PG, 'Papua New Guinea'),
        (PY, 'Paraguay'),
        (PE, 'Peru'),
        (PH, 'Philippines'),
        (PN, 'Pitcairn Islands'),
        (PL, 'Poland'),
        (PT, 'Portugal'),
        (PR, 'Puerto Rico'),
        (QA, 'Qatar'),
        (RE, 'Réunion'),
        (RO, 'Romania'),
        (RU, 'Russia'),
        (RW, 'Rwanda'),
        (BL, 'Saint Barthélemy'),
        (SH, 'Saint Helena'),
        (KN, 'Saint Kitts and Nevis'),
        (LC, 'Saint Lucia'),
        (MF, 'Saint Martin'),
        (PM, 'Saint Pierre and Miquelon'),
        (VC, 'Saint Vincent and the Grenadines'),
        (WS, 'Samoa'),
        (SM, 'San Marino'),
        (ST, 'São Tomé and Príncipe'),
        (SA, 'Saudi Arabia'),
        (SN, 'Senegal'),
        (RS, 'Serbia'),
        (SC, 'Seychelles'),
        (SL, 'Sierra Leone'),
        (SG, 'Singapore'),
        (SX, 'Sint Maarten'),
        (SK, 'Slovakia'),
        (SI, 'Slovenia'),
        (SB, 'Solomon Islands'),
        (SO, 'Somalia'),
        (ZA, 'South Africa'),
        (GS, 'South Georgia and the South Sandwich Islands'),
        (KR, 'South Korea'),
        (SS, 'South Sudan'),
        (ES, 'Spain'),
        (LK, 'Sri Lanka'),
        (SR, 'Suriname'),
        (SJ, 'Svalbard and Jan Mayen'),
        (SZ, 'Swaziland'),
        (SE, 'Sweden'),
        (CH, 'Switzerland'),
        (TW, 'Taiwan'),
        (TJ, 'Tajikistan'),
        (TZ, 'Tanzania'),
        (TH, 'Thailand'),
        (TG, 'Togo'),
        (TK, 'Tokelau'),
        (TO, 'Tonga'),
        (TT, 'Trinidad and Tobago'),
        (TN, 'Tunisia'),
        (TR, 'Turkey'),
        (TM, 'Turkmenistan'),
        (TC, 'Turks and Caicos Islands'),
        (TV, 'Tuvalu'),
        (VI, 'U.S. Virgin Islands'),
        (UG, 'Uganda'),
        (UA, 'Ukraine'),
        (AE, 'United Arab Emirates'),
        (GB, 'United Kingdom'),
        (US, 'United States'),
        (UY, 'Uruguay'),
        (UZ, 'Uzbekistan'),
        (VU, 'Vanuatu'),
        (VA, 'Vatican City'),
        (VE, 'Venezuela'),
        (VN, 'Vietnam'),
        (WF, 'Wallis and Futuna'),
        (EH, 'Western Sahara'),
        (YE, 'Yemen'),
        (ZM, 'Zambia'),
        (ZW, 'Zimbabwe'),
    )


# LANGUAGES LIST
class LanguagesList(OrderedDict):
    BAHASAINDONESIA = 1
    BAHASAMALAYSIA = 2
    BENGALI = 3
    DANISH = 4
    DEUTSCH = 5
    ENGLISH = 6
    ESPANOL = 7
    FRANCAIS = 8
    HINDI = 9
    ITALIANO = 10
    HUNGARIAN = 11
    NEDERLANDS = 12
    NORWEGIAN = 13
    POLISH = 14
    PORTUGUES = 15
    PUNJABI = 16
    SIGNLANGUAGE = 17
    FINNISH = 18
    SWEDISH = 19
    TAGALOG = 20
    TURKISH = 21
    CZECH = 22
    GREEK = 23
    RUSSIAN = 24
    UKRAINIAN = 25
    HEBREW = 26
    ARABIC = 27
    THAILANGUAGE = 28
    CHINESE = 29
    JAPANESE = 30
    KOREAN = 31

    LANGUAGE_CHOICES = (
        (BAHASAINDONESIA, 'Bahasa Indonesia'),
        (BAHASAMALAYSIA, 'Bahasa Malaysia'),
        (BENGALI, 'Bengali'),
        (DANISH, 'Dansk'),
        (DEUTSCH, 'Deutsch'),
        (ENGLISH, 'English'),
        (ESPANOL, 'Español'),
        (FRANCAIS, 'Français'),
        (HINDI, 'Hindi'),
        (ITALIANO, 'Italiano'),
        (HUNGARIAN, 'Magyar'),
        (NEDERLANDS, 'Nederlands'),
        (NORWEGIAN, 'Norsk'),
        (POLISH, 'Polski'),
        (PORTUGUES, 'Português'),
        (PUNJABI, 'Punjabi'),
        (SIGNLANGUAGE, 'Sign Language'),
        (FINNISH, 'Suomi'),
        (SWEDISH, 'Svenska'),
        (TAGALOG, 'Tagalog'),
        (TURKISH, 'Türkçe'),
        (CZECH, 'Čeština'),
        (GREEK, 'Ελληνικά'),
        (RUSSIAN, 'Русский'),
        (UKRAINIAN, 'українська'),
        (HEBREW, 'עברית'),
        (ARABIC, 'العربية'),
        (THAILANGUAGE, 'ภาษาไทย'),
        (CHINESE, '中文'),
        (JAPANESE, '日本語'),
        (KOREAN, '한국어'),
    )


# PAYMENT METHODS
class PaymentMethodChoice(OrderedDict):
    VISA = 1
    MASTERCARD = 2
    AMERICANEXPRESS = 3
    PAYPAL = 4
    CASH = 5

    PAYMENT_METHOD_CHOICES = (
        (VISA, 'Visa'),
        (MASTERCARD, 'Mastercard'),
        (AMERICANEXPRESS, 'American Express'),
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
    COOKINGLOCALFOOD = 8
    LOCALMOVIESNIGHT = 9

    IMMERSION_CHOICES = (
        (ACTIVITIESWITHLOCALS, 'Games and activities with local'),
        (BARISTA, 'Coffee tasting experience'),
        (BEERTASTING, 'Beer tasting experience'),
        (CHOCOLATETASTING, 'Chocolate tasting experience'),
        (PUBCRAWL, 'Pub crawl'),
        (FOODTASTING, 'Local food tasting'),
        (DANCECLASS, 'Local dance class'),
        (COOKINGLOCALFOOD, 'Cooking Local Food'),
        (LOCALMOVIESNIGHT, 'Local Movies Night'),
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
    POOL = 16

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
        (POOL, 'Pool'),
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
    POOL = 16

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
        (POOL, 'Pool'),
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
    BREAKFAST = 3
    LUNCH = 4
    DINNER = 5

    WORK_EXCHANGE_CHOICES = (
        (ACCOMMODATION, 'Accommodation'),
        (DISCOUNTINCLASSES, 'Discount in classes'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
