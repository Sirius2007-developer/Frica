from django.contrib import admin
from .models import Custom, Wedding, B_cake, Category, Newsletter, Team, Testimonial, Contact
# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Contact)

@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(B_cake)
class B_cakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
