from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model with role-based access
class User(AbstractUser):
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='farmer')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)  # For seller approval
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def save(self, *args, **kwargs):
        # Auto-approve farmers and admins
        if self.role in ['farmer', 'admin']:
            self.is_approved = True
        super().save(*args, **kwargs)
