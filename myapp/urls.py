from myapp.modules.users.views import users_APIView
from myapp.modules.users_adress.views import users_adress_APIView
from myapp.modules.users_contact.views import users_contact_APIView 

from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

# Register the UsersViewSet with the router
router.register("users", users_APIView, basename="users")
router.register("users_adress", users_adress_APIView, basename="users_adress")
router.register("users_contact", users_contact_APIView, basename="users_contact")



urlpatterns = [
    # Add other paths as needed
]

# Add the router URLs to the urlpatterns
urlpatterns += router.urls