from athletes.models import Athlete, ClubForAthlete
from django.contrib import admin
from races.models import Result


class ResultInline(admin.TabularInline):
    model = Result
    fields = ('position', 'record', 'extra')
    readonly_fields = ('position', 'record')
    extra = 1

class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')
    inlines = (ResultInline,)


# Register your models here.
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(ClubForAthlete)
