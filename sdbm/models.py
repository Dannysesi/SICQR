from django.db import models
import qrcode
import os
from PIL import Image
import uuid
from io import BytesIO
from django.core.files import File

class Student(models.Model):
    name = models.CharField(max_length=100)
    matric_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    home_address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='qr_codes', null=True, blank=True)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"http://localhost:3030/student_detail/{self.id}/")
        qr.make(fit=True)

        # Ensure 'media/qr_codes' directory exists
        qr_code_directory = 'media/qr_codes'
        os.makedirs(qr_code_directory, exist_ok=True)

        img = qr.make_image(fill_color="black", back_color="white")
        file_path = f"{qr_code_directory}/{self.id}.png"
        img.save(file_path)

    def __str__(self):
        return self.name


