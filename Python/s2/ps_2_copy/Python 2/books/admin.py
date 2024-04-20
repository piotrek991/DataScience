from django.utils import timezone
from django.contrib import admin
from books.models import Book, Author, Event
class BookAdmin(admin.ModelAdmin):
    # list_display = ('')
    # search_fields = ('')
    # list_filter = ('')
    # date_hierarchy = ''
    # fieldsets = ()
    # readonly_fields = ('')
    raw_id_fields = ('author',)
    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user

class EventAdmin(admin.ModelAdmin):
    list_filter = ("country", "city","start_date", "end_date","authors")
    search_fields = ("name", "country", "city", "street")
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.start_date < timezone.now():
            return False
        else:
            return True

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Event, EventAdmin)

# Register your models here.