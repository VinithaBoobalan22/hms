from django.urls import path,include

urlpatterns = [
    path('hos',include('Hospital.urls'))
]
