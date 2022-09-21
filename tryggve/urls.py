from django.urls import path
from tryggve import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="tryggve/index.html"), name="index-view"),
    path('about/', TemplateView.as_view(template_name="tryggve/about.html"), name="about-view"),
    path('news/', TemplateView.as_view(template_name="tryggve/news.html"), name="news-view"),
    path('swe/', TemplateView.as_view(template_name="tryggve/sweden.html"), name="sweden-view"),
    

]