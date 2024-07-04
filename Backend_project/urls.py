
from django.contrib import admin
from django.urls import path, include
from Backend_app import views


# new form to do the routerization with RESTFramework
# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers 

# create a router object 
router = routers.DefaultRouter()

#register the router
router.register(r'tasks',views.TodoView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    
]
