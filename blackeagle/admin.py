from django.contrib import admin
from .models import Education, Experience, Projects, About, Badge, Other, Extras, Contact


class EductionAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute', 'year')


class OtherAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute', 'year')


class ExtrasAdmin(admin.ModelAdmin):
    list_display = ('activity', 'year')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject')


admin.site.register(Education, EductionAdmin)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(About)
admin.site.register(Badge)
admin.site.register(Other, OtherAdmin)
admin.site.register(Extras, ExtrasAdmin)
admin.site.register(Contact, ContactAdmin)



