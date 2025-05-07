from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    SPICE_LEVEL_CHOICES = [
        ('none', 'None'),
        ('mild', 'Mild'),
        ('medium', 'Medium'),
        ('hot', 'Hot'),
        ('extra-hot', 'Extra Hot'),
    ]
     
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    spice_level = models.CharField(max_length=20, choices=SPICE_LEVEL_CHOICES, default='none')

    def __str__(self):
        return self.name


class DietaryRestriction(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    TYPE_CHOICES = [
        ('bone-in', 'Bone-In Wings'),
        ('boneless', 'Boneless Wings'),
        ('plant-based', 'Plant-Based Wings'),
        ('sandwich', 'Chicken Sandwich'),
        ('wrap', 'Chicken Wrap'),
        ('side', 'Side Item'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sauces = models.ManyToManyField(Sauce, blank=True)
    dietary_restriction = models.ManyToManyField(DietaryRestriction, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField( blank=True, null=True)

    def __str__(self):
        return self.name

class AddOn(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    applicable_items = models.ManyToManyField(MenuItem, related_name='add_ons', blank=True)

    def __str__(self):
        return f"{self.name} (+${self.price})"