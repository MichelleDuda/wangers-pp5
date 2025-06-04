from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from menu.models import MenuItem
from django.utils import timezone


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def total_likes(self):
        return self.likes.count()

    def has_liked(self, user):
        if not user.is_authenticated:
            return False
        return self.likes.filter(user=user).exists()

    def __str__(self):
        return f"{self.title} by {self.user.username} - {self.rating} stars"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')

    def __str__(self):
        return f"{self.user.username} likes Review {self.review.id}"
