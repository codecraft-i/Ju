from django.db import models

# Import the necessary classes
from django.utils.timezone import now
from django.utils.html import format_html

# Create your models here.

class CheckedContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_checked='Yes')

class UncheckedContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_checked='No')

# 'Cantact' model for User
class Contact(models.Model):
    LANGUAGE_CERTIFICATE_CHOICES = [
        ('IELTS', 'IELTS'),
        ('TOPIK', 'TOPIK'),

        ('SAT', 'SAT'),
        ('TOEFL', 'TOEFL'),
        ('PTE', 'PTE'),
        ('GRE', 'GRE'),
        ('GMAT', 'GMAT'),
        ('Duolingo', 'Duolingo'),

        ('KLAT', 'KLAT'),
        ('KIIP', 'KIIP'),
        ('EPS-TOPIK', 'EPS-TOPIK'),

        ('No', 'ENDI OLAMAN'),
    ]
    
    YES_NO_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    language_certificate = models.CharField(
        max_length=11, choices=LANGUAGE_CERTIFICATE_CHOICES, default='No', blank=True
    )

    is_checked = models.CharField(
        max_length=3, choices=YES_NO_CHOICES, default='No'
    )

    objects = models.Manager()
    checked_contacts = CheckedContactManager()
    unchecked_contacts = UncheckedContactManager()

    def __str__(self):
        return f"{self.name} - {self.phone}"
    
    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontaktlar"
    
class CheckedContact(Contact):
    objects = CheckedContactManager()

    class Meta:
        proxy = True
        verbose_name = "Tekshirilgan Kontakt"
        verbose_name_plural = "Tekshitilgan Kontaklar"

class UncheckedContact(Contact):
    objects = UncheckedContactManager()

    class Meta:
        proxy = True
        verbose_name = "Tekshirilmagan Kontakt"
        verbose_name_plural = "Tekshirilmagan Kontaklar"
    
class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    request_count = models.IntegerField(default=1)
    last_request = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ip_address} - {self.request_count} requests"
    
    class Meta:
        verbose_name = "IP Address"
        verbose_name_plural = "IP Address"

class IndexTitle(models.Model):
    title = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk and IndexTitle.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{ self.title }"

class Certificate(models.Model):
    IELTS = models.BooleanField(default=False)
    TOPIK = models.BooleanField(default=False)
    SAT = models.BooleanField(default=False)
    TOEFL = models.BooleanField(default=False)
    PTE = models.BooleanField(default=False)
    GRE = models.BooleanField(default=False)
    GMAT = models.BooleanField(default=False)
    Duolingo = models.BooleanField(default=False)
    KLAT = models.BooleanField(default=False)
    KIIP = models.BooleanField(default=False)
    EPS_TOPIK = models.BooleanField(default=False)

    NO = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk and Certificate.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return ", ".join([name for name, value in self.__dict__.items() if value is True and name != "_state"])
    
class CallNum(models.Model):
    number = models.PositiveBigIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk and CallNum.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{ self.number }"

    class Meta:
        verbose_name = "Menejer raqamlari"
        verbose_name_plural = "Menejer raqamlari"
    
class MaxImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

    class Meta:
        verbose_name = "Desktop Surat"
        verbose_name_plural = "Desktop Suratlar"

class MinImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

    class Meta:
        verbose_name = "Telefon Surat"
        verbose_name_plural = "Telefon Suratlar"

# Succes Page models

class SuccText(models.Model):
    title = models.TextField(max_length=500, blank=True, null=True,
    help_text=format_html(
            'Agar qatorni tugatguvchi bo‘lsangiz <code>&lt;br&gt;</code> yozing.<br>'
            "Agar so‘zni belgilab qo‘ymoqchi bo‘lsangiz <code>&lt;span&gt;</code>Belgilangan so'z<code>&lt/span&gt;</code> ichida yozing."
        ))

    def save(self, *args, **kwargs):
        if not self.pk and SuccText.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{ self.title }"

    class Meta:
        verbose_name = "Ok Page Title"
        verbose_name_plural = "Ok Page Title"

class SuccDocPic(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False, help_text=format_html(
            'Ok Pageni tavsiflovchi suratni kiriting'
        ))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk and SuccDocPic.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

    class Meta:
        verbose_name = "Ok Page Media"
        verbose_name_plural = "Ok Page Suratlari"

class SuccLink(models.Model):
    title = models.CharField(max_length=100, blank=True, help_text=format_html(
            'Button Tugmaning nomini kiriting'
        ))
    address = models.CharField(max_length=100, blank=True, help_text=format_html(
            'Button Tugmaning manzilini kiriting'
        ))

    def save(self, *args, **kwargs):
        if not self.pk and SuccLink.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{ self.title }"

    class Meta:
        verbose_name = "Ok Page Button"
        verbose_name_plural = "Ok Page Button"

class SuccDesc(models.Model):
    title = models.TextField(max_length=100, blank=True, help_text=format_html(
            'Agar qatorni tugatguvchi bo‘lsangiz <code>&lt;br&gt;</code> yozing.<br>'
        ))

    def save(self, *args, **kwargs):
        if not self.pk and SuccDesc.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{ self.title }"

    class Meta:
        verbose_name = "Ok Page Description"
        verbose_name_plural = "Ok Page Description"