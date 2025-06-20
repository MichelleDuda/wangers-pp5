import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from menu.models import MenuItem, Sauce, AddOn
from profiles.models import UserProfile


class Order(models.Model):
    DELIVERY_METHODS = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    delivery_method = models.CharField(
        max_length=10,
        choices=DELIVERY_METHODS,
        default='delivery',
    )
    postcode = models.CharField(max_length=5, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='',
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        Code taken from Boutique Ado Walkthrough
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update order_total & grand_total
        Accounts for delivery cost if delivery method is selected
        """
        self.order_total = self.lineitems.aggregate(
            total=Sum('lineitem_total'))['total'] or 0

        if self.delivery_method == 'delivery':
            if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
                self.delivery_cost = (
                    self.order_total
                    * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
                    / 100
                )
            else:
                self.delivery_cost = Decimal('0.00')
        else:
            self.delivery_cost = Decimal('0.00')

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    menu_item = models.ForeignKey(
        MenuItem,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=1)
    sauce = models.ForeignKey(
        Sauce,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    addons = models.ManyToManyField(AddOn, blank=True)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """Calculate the lineitem total including add-ons."""
        base_price = self.menu_item.price * self.quantity
        addons_total = 0

        if self.pk:
            addons_total = sum(
                addon.price for addon in self.addons.all()
            )

        self.lineitem_total = base_price + addons_total
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'{self.quantity} x {self.menu_item.name} on order '
            f'{self.order.order_number}'
        )
