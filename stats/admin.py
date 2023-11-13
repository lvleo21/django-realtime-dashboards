from django.contrib import admin
from stats.models import (Statistic, DataItem)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    pass


@admin.register(DataItem)
class DataItemAdmin(admin.ModelAdmin):
    pass
