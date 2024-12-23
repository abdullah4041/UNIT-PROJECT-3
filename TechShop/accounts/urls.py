from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('signin/', views.sign_in, name="sign_in"),
    path('logout/', views.log_out, name="log_out"),
    path('profile/update/', views.update_user_profile, name="update_user_profile"),
    path('profile/<str:user_name>/', views.user_profile, name='user_profile'),
    path('cart/', views.view_cart, name='view_cart'),
    path("cart/add/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),


]