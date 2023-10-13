"""nsubh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roomselection.views import makoRS, commonsRS, clcRS, leogoodwinRS, farquharRS, foundersRS, vettelRS, rollingRS

# The different URLs for the website
urlpatterns = [
    path('', include('loginpage.urls')),
    path('loginpage/', include('loginpage.urls')),
    path('homepage/', include('homepage.urls')),
    path('register/', include('registrationpage.urls')),
    path('reviewpage/', include('reviewpage.urls')),
    path('completionpage/', include('completionpage.urls')),
    path('makors/', makoRS, name='makoRS'),
    path('commonsrs/', commonsRS, name='commonsRS'),
    path('clcrs/', clcRS, name='clcRS'),
    path('leogoodwinrs/', leogoodwinRS, name='leogoodwinRS'),
    path('farquharrs/', farquharRS, name='farquharRS'),
    path('vettelrs/', vettelRS, name='vettelRS'),
    path('foundersrs/', foundersRS, name='foundersRS'),
    path('rollingrs/', rollingRS, name='rollingRS'),
    path('admin/', admin.site.urls),
]
