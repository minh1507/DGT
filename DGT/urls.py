from django.urls import path, include
from swagger import swaggerRouter

urlpatterns = [
    path('apis/', include(swaggerRouter)), 
    # path('api/', include(
    #     ethnicRouter + 
    #     userRouter + 
    #     authRouter + 
    #     actionRouter + 
    #     resourceRouter +
    #     deviceRouter +
    #     clientRouter
    # )), 
]