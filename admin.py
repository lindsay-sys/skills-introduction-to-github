from django.contrib import admin
from .models import Category, Vendor, Tender, Bid

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

class VendorAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'phone', 'address', 'created_at')  
  search_fields = ('name', 'email')
  list_filter = ('created_at',)


class TenderAdmin(admin.ModelAdmin):
  list_display = ('reference_no', 'title', 'status', 'opening_date', 'created_at', 'closing_date')
  search_fields = ('reference_no', 'title')
  list_filter = ('status', 'category', 'created_at')


class BidAdmin(admin.ModelAdmin):
  list_display = ('vendor', 'tender', 'amount', 'submitted_at', 'status', 'proposal')
  search_fields = ('vendor__name', 'tender__title')
  list_filter = ('tender', 'vendor', 'status')  


admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Tender, TenderAdmin)
admin.site.register(Bid, BidAdmin)  

