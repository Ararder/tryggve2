from django.urls import path
from tryggve import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="tryggve/tryggve.html"), name="tryggve-view"),
    path('about/', TemplateView.as_view(template_name="tryggve/about.html"), name="about-view"),
    path('news/', TemplateView.as_view(template_name="tryggve/news.html"), name="news-view"),
    path('participating-countries/', TemplateView.as_view(template_name="tryggve/participating_countries.html"), name="participating-view"),
    path('infrastructure/', TemplateView.as_view(template_name="tryggve/infrastructure.html"), name="infrastructure-view"),
    path('funding/', TemplateView.as_view(template_name="tryggve/funding.html"), name="funding-view"),
    path('projects/', TemplateView.as_view(template_name="tryggve/projects.html"), name="projects-view"),
    path('test/', TemplateView.as_view(template_name="tryggve/test.html"), name="test-view"),
    path('resources/', TemplateView.as_view(template_name="tryggve/resources.html"), name="resources-view"),
    
    
    path('swe/', TemplateView.as_view(template_name="tryggve/sweden.html"), name="sweden-view"),
    path('den/', TemplateView.as_view(template_name="tryggve/denmark.html"), name="denmark-view"),
    path('nor/', TemplateView.as_view(template_name="tryggve/norway.html"), name="norway-view"),
    path('est/', TemplateView.as_view(template_name="tryggve/estonia.html"), name="estonia-view"),
    

]