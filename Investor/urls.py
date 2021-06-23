from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'Investor'

urlpatterns = [
    path('', views.vc_invest, name="vc_invest"),
    path('create_investor', views.create_investor, name="create_investor"),
    path('find_startup', views.find_startup, name="find_startup"),
    path('startup_list', views.startup_list, name="startup_list"),
    path('about_startup/<slug:slug>', views.about_startup, name="about_startup"),
    path('references', TemplateView.as_view(template_name='../VCTemplate/references.html'), name="references")
]