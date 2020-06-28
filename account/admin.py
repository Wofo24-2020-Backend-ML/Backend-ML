from django.contrib import admin
from .models import Professional, Category, SubCategory, UploadImage, RequestVerification, Package


# Register your models here.
class RequestVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'timestamp')
    search_fields = ('status',)

admin.site.register(Professional)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(UploadImage)
admin.site.register(RequestVerification, RequestVerificationAdmin)
admin.site.register(Package)
