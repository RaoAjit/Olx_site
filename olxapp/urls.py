from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('registration',views.Registration,name='Registration'),
    path('login',views.mylogin,name='mylogin'),
    path('logout',views.mylogout,name='mylogout'),
    path('sell',views.sell,name='sellform'),
    path('sellcart',views.sellcart,name='sellcart'),
    path('add_cart/<int:id>',views.addcart,name='addcart'),
    path('byu/<int:id>',views.buy,name='buy'),
    path('ordered',views.ordered,name='ordered'),
    path('orderes',views.orders,name='orders'),
    path('deleted/<int:id>',views.deleted,name='deletesellpd'),
    path('deletecart/<int:id>',views.deletecart,name='deletecart'),
    path('search',views.search,name='search'),
    path('checkout_session',views.checkout_session,name='checkout_session'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel,name='cancel'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
