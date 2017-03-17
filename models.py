from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

# Create your models here.
class Spgateway(models.Model):
    member_unified = models.CharField(unique=True, max_length=10)
    timestamp = models.DateTimeField(default=timezone.now)
    idcard_year = models.CharField(max_length=3, blank=True, null=True, verbose_name=u'ID card year')
    idcard_month = models.CharField(max_length=2, blank=True, null=True, verbose_name=u'ID card month')
    idcard_date = models.CharField(max_length=2, blank=True, null=True, verbose_name=u'ID card date')
    idcard_place = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'ID card place')
    member_name = models.CharField(max_length=20)
    member_phone = models.CharField(max_length=13)

    manager_name = models.CharField(max_length=10)
    manager_name_en = models.CharField(max_length=20)
    login_account = models.CharField(max_length=20)
    manager_mobile = models.CharField(max_length=10)
    manager_email = models.EmailField(max_length=40)

    merchant_id = models.CharField(default='HBX0000', max_length=15, unique=True)
    merchant_name = models.CharField(max_length=20)
    merchant_name_en = models.CharField(max_length=100)
    merchant_weburl = models.URLField(max_length=100)
    merchant_addr_city = models.CharField(max_length=5)
    merchant_addr_area = models.CharField(max_length=5)
    merchant_addr_code = models.CharField(max_length=3)
    merchant_addr = models.CharField(max_length=60)
    national_en = models.CharField(max_length=20)
    city_en = models.CharField(max_length=20)

    MERCHANT_TYPE_CHOICES = (
        (1, u'實體商品'),
        (2, u'服務'),
        (3, u'虛擬商品'),
        (4, u'票劵'),
    )
    
    merchant_type = models.IntegerField(default=2, choices=MERCHANT_TYPE_CHOICES)
    business_type = models.CharField(default='7999', max_length=4)
    merchant_desc = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=3)
    subbank_code = models.CharField(max_length=4)
    bank_account = models.CharField(max_length=30)

    CREDIT_TYPE_CHOICES = (
    	(0, u'手動請款'),
    	(1, u'自動請款')
    )
    credit_autotype = models.IntegerField(choices=CREDIT_TYPE_CHOICES, default=1, null=True, blank=True)
    credit_limit = models.IntegerField(null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    agreed_fee = models.CharField(max_length=255, blank=True)
    agreed_day = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}'.format(self.merchant_name)

    class Meta:
        verbose_name = _('Spgateway')
        verbose_name_plural = verbose_name








