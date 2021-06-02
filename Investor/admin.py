from django.contrib import admin
from .models import Investor, Company


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'firm')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'sector', 'stage', 'revenue', 'valuation', 'launch_year')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('sector', 'stage')
