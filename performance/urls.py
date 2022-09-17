from django.urls import path
from .views import *
urlpatterns= [
    path('random_revenue/',randomRevenue.as_view(),name="random_revenue"),
    path('slow_iteration/',slowIteration.as_view(),name="slow_iteration"),
    path('genertaeRandomData/',genertaeRandomData.as_view(),name="genertaeRandomData"),


    
]