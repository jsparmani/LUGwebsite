"""lugwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = 'LINUX USER GROUP'
admin.site.site_title = 'Linux User Group Administration'
admin.site.index_title = 'Linux User Group Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace = 'accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('blog/',include('blog.urls',namespace = 'blog')),
    path('event/',include('event.urls',namespace = 'event')),
    path('emails/',include('emails.urls',namespace = 'emails')),
    path('welcome/',views.WelcomePage.as_view(),name='welcome'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
