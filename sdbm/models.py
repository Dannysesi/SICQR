from django.db import models
import qrcode
import os
from PIL import Image
import uuid
from io import BytesIO
from django.core.files import File
from datetime import date

class Student(models.Model):
    state = (
        ('abia', 'Abia State'),
        ('adamawa', 'Adamawa State'),
        ('akwa_ibom', 'Akwa Ibom State'),
        ('anambra', 'Anambra State'),
        ('bauchi', 'Bauchi State'),
        ('bayelsa', 'Bayelsa State'),
        ('benue', 'Benue State'),
        ('borno', 'Borno State'),
        ('cross_river', 'Cross River State'),
        ('delta', 'Delta State'),
        ('ebonyi', 'Ebonyi State'),
        ('edo', 'Edo State'),
        ('ekiti', 'Ekiti State'),
        ('enugu', 'Enugu State'),
        ('gombe', 'Gombe State'),
        ('imo', 'Imo State'),
        ('jigawa', 'Jigawa State'),
        ('kaduna', 'Kaduna State'),
        ('kano', 'Kano State'),
        ('katsina', 'Katsina State'),
        ('kebbi', 'Kebbi State'),
        ('kogi', 'Kogi State'),
        ('kwara', 'Kwara State'),
        ('lagos', 'Lagos State'),
        ('nasarawa', 'Nasarawa State'),
        ('niger', 'Niger State'),
        ('ogun', 'Ogun State'),
        ('ondo', 'Ondo State'),
        ('osun', 'Osun State'),
        ('oyo', 'Oyo State'),
        ('plateau', 'Plateau State'),
        ('rivers', 'Rivers State'),
        ('sokoto', 'Sokoto State'),
        ('taraba', 'Taraba State'),
        ('yobe', 'Yobe State'),
        ('zamfara', 'Zamfara State'),
        ('fct', 'Federal Capital Territory'),
    )

    medical = (
        ('HEALTHY', 'healthy'),
        ('NOT HEALTHY', 'not healthy'),
    )
    
    lev = (
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
    )

    stat = (
        ('ACTIVE', 'active'),
        ('INACTIVE', 'inactive'),
        ('GRADUATED', 'graduated'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(default=date.today)
    state_of_origin = models.CharField(verbose_name='State of Origin', choices=state, max_length=20)
    matric_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    email = models.EmailField(help_text='Student Email')
    phone = models.CharField(max_length=20)
    home_address = models.CharField(max_length=100)
    emeConName = models.CharField(verbose_name='Emergency contact name', max_length=30)
    emeconPhone = models.CharField(max_length=20)
    guardian_name = models.CharField(verbose_name='Guardian Full Name', max_length=50)
    relationship_to_student = models.CharField(max_length=20)
    guardian_email = models.EmailField(help_text='Guardian Email Address')
    guardian_phone = models.CharField(max_length=20)
    guardian_add = models.CharField(verbose_name='Guardian Home Address', max_length=50, null=True, blank=True)
    next_of_kin_name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=20)
    next_of_kin_email = models.EmailField(help_text='Next of Kin emaill address', null=True, blank=True)
    next_of_kin_phone = models.CharField(max_length=20, null=True, blank=True)
    next_of_kin_address = models.CharField(max_length=50, null=True, blank=True)
    medical_condition = models.CharField(verbose_name='Medical Condition', choices=medical, max_length=20)
    if_not_healthy = models.CharField(help_text='If not healthy kindly state the aligment', max_length=20, null=True, blank=True)
    level = models.CharField(verbose_name='Level', choices=lev, max_length=20)
    enrollment_date = models.DateField(default=date.today)
    graduation_date = models.DateField(default=date.today)
    status = models.CharField(verbose_name='Student Status', choices=stat, max_length=20)
    image = models.ImageField(upload_to='qr_codes', null=True, blank=True)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"http://192.168.101.62:3030/student_detail/{self.id}/")
        qr.make(fit=True)

        # Ensure 'media/qr_codes' directory exists
        qr_code_directory = 'media/qr_codes'
        os.makedirs(qr_code_directory, exist_ok=True)

        img = qr.make_image(fill_color="black", back_color="white")
        file_path = f"{qr_code_directory}/{self.id}.png"
        img.save(file_path)

    def __str__(self):
        return self.first_name


