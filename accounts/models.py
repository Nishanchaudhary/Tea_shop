from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom User Model
class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)


     # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


# Profile Model for Customers
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Profile Model for Sellers
class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_profile')
    shop_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
