from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Vendor(models.Model):
  name= models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=20,blank=True)
  address = models.CharField(max_length=255,blank=True)
  rating= models.DecimalField(max_digits=3,decimal_places=2, default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name  


class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
    return self.name


class Tender(models.Model):
  class Status(models.TextChoices):
    DRAFT = "DRAFT","Draft"
    OPEN = "OPEN","Open"
    CLOSED = "CLOSED","Closed"
    AWARDED = "AWARDED","Awarded"
    CANCELLED = "CANCELLED","Cancelled"

  reference_no = models.CharField(max_length=50, unique=True)
  title = models.CharField(max_length=200)
  category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, related_name="tenders")
  description = models.TextField(blank=True)
  opening_date = models.DateTimeField()
  closing_date = models.DateTimeField()
  budget_min = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
  budget_max = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
  status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)   

  class Meta:
    ordering = ["-created_at"]

  def __str__(self):
    return f"{self.reference_no} -{self.title}"


class Bid(models.Model):
  class Status(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


  tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name="bids")
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="bids")
  amount = models.DecimalField(max_digits=12, decimal_places=2)
  proposal = models.TextField(blank=True)
  status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
  submitted_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ("tender","vendor")
    ordering = ["-submitted_at"]

  def __str__(self):
    return f"Bid by {self.vendor} on {self.tender}"                

