
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHomePage"),
    path("about/", views.about, name= "AboutUs"),
    path("contact/", views.contact, name= "ContactUs"),
    path("tracker/", views.tracker, name= "TrackingStatus"),
    path("search/", views.search, name= "Search"),
    path("products/<int:myid>", views.productviews, name= "ProductViews"),
    path("checkout/", views.checkout, name= "checkout"),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup")


]
