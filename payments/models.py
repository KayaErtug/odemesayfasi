# .\payments\models.py
from django.db import models

class PaymentLink(models.Model):
    owner_slug = models.SlugField(max_length=64, db_index=True)  # subdomain => cemyilmaz
    slug = models.SlugField(max_length=96, db_index=True)        # link => konser-2026
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    amount_try = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("owner_slug", "slug")

    def __str__(self) -> str:
        return f"{self.owner_slug}/{self.slug} - {self.title}"
