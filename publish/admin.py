from django.contrib import admin
from publish.models import Publish

class PublishAdmin(admin.ModelAdmin):
    list_display = ('id_pool', 'id_channel', 'initial_date', 'final_date', 'is_active')
    

admin.site.register(Publish, PublishAdmin)

