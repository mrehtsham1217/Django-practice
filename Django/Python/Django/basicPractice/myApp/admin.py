from django.contrib import admin
from .models import Chaivariety, ChaiCertificate, ChaiReviews, Store

# Register your models here.


class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2


class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chaiTypes', 'created_at')
    # Chai has relation with Reviews. One has many reviews. SO we are handling Chai and reviews side by side in database
    inlines = [ChaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variets',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_no')


admin.site.register(Chaivariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
# admin.site.register(ChaiReviews, ChaiReviewInline) # dont show like this because each chai has its own reviews
