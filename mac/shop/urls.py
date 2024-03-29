from django.urls import path
from shop import views

urlpatterns = [
    path("home",views.home),
    path("productView/<int:id>",views.productView),
    path("cart",views.cart),
    path("contact",views.contact),
    path("checkout/<int:belong>/<int:id>",views.checkout),
    path("paymenthandler",views.paymenthandler),
    path("paymentsuccess",views.paymentsuccess),
    path("paymentfail",views.paymentfail),
    path("tracker",views.tracker),
    path("login",views.handleLogin),
    path("signup",views.handleSignup),
    path("logout",views.handleLogout),
    path("headerView/<int:titleNumber>",views.headerView),
]
