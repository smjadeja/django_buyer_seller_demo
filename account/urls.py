from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name = 'home'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('changepass/', views.changepass, name="changepass"),
    path('logout/', views.logout, name='logout'),
    path('productview/', views.productview, name='productview'),
    path('editproduct/<int:id>', views.update_product, name='editproduct'),
    path('buyproduct/<int:id>', views.buyprod, name='buyprod'),
    path('placeorder/<int:id>', views.placeorder, name='placeorder'),
    path('orders/', views.orderhistory, name='orders'),
    path('delete/<int:id>', views.delprod, name = "deleteproduct")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
