from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sneaker(models.Model):

 # Condition choices
    CONDITION_CHOICES = [
        ('NEW', 'New/Deadstock'),
        ('LIKE_NEW', 'Like New'),
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'),
        ('POOR', 'Poor'),
    ]
    
    # Size type choices
    SIZE_TYPE_CHOICES = [
        ('US', 'US'),
        ('UK', 'UK'),
        ('EU', 'EU'),
    ]

    #Brand details
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="sneakers")
    image = models.ImageField(upload_to='sneakers/', null=True, blank=True) #add pillow for image processing
    description = models.TextField()
    model_name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=50)
    release_year = models.IntegerField()

    # Sizing
    size = models.DecimalField(max_digits=4, decimal_places=1)
    size_type = models.CharField(max_length=2, choices=SIZE_TYPE_CHOICES, default='US')

    # Condition and Pricing
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Status
    is_sold = models.BooleanField(default=False)
    date_listed = models.DateTimeField(auto_now_add=True)
    date_sold = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.brand_name} {self.model_name} - {self.colorway}" #Nike Air Jordans - Navy-blue
    
    class Meta: #The Meta class should be after all the field definitions, not before.
        ordering = ['-date_listed', 'model_name']
