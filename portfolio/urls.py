from django.urls import path
from .views import( homepage, about, projects, contacts)

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('about/', about, name = 'about'),
    path('projects/', projects, name = 'projects'),
    path('contacts/', contacts, name = 'contacts')

]