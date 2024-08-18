# from .views import avtomobilViewSet,testimonital,sevicewivs,home,aloqa,boking,aboutwivs,malumot
# from rest_framework.routers import SimpleRouter
# from django.urls import path
# from django.contrib import admin
#
# router=SimpleRouter()
#
# router.register("maket",avtomobilViewSet,basename='narsa')
#
#
# urlpatterns=router.urls
#
#
# urlpatterns=[
#     path('',home,name='saxifa'),
#     path('aloqa/',aloqa,name='alo'),
#     path('aloqa/',testimonital,name='alo'),
#     path('aloqa/',sevicewivs,name='alo'),
#     path('aloqa/',boking,name='alo'),
#     path('aloqa/',aboutwivs,name='alo'),
#     path('aloqa/',malumot,name='alo'),
#
# ]


from django.urls import path
from django.urls import include
from rest_framework.routers import SimpleRouter

from .views import avtomobilViewSet, home, aloqa, testimonital, sevicewivs, boking, aboutwivs, malumot

# Router yaratish
router = SimpleRouter()
router.register("maket", avtomobilViewSet, basename='narsa')

# urlpatterns ro'yxatiga yo'llarni qo'shish
urlpatterns = [
    # API yo'llari
    path('api/', include(router.urls)),
    # Dastur yo'llari
    path('', home, name='saxifa'),
    path('contact.html/', aloqa, name='aloqa'),
    path('testimonial.html/', testimonital, name='testimonital'),
    path('service.html/', sevicewivs, name='service'),
    path('booking.html/', boking, name='boking'),
    path('about.html/', aboutwivs, name='about'),
    path('404.html/', malumot, name='malumot'),
]
