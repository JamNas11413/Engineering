from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# router = SimpleRouter() 
router = DefaultRouter()  # with it we get more features 
router.register('product', views.productViewSet)  # products endpoint should be mange by this view
router.urls()

# urlpatterns = router.urls()

# OR

urlpatterns = [
    path('',include(router.urls)),

]

# urlpatterns = [
#     path('singleobj/<int:pk>/', views.SingleObjectView.as_view()),  # as_view will convert rthis class to a regular function based view, so at the ned of the day there is a functoio under the hood which gets called but while writting the code we write classes and thus we access sll of oops benefits
#     path('listobj/', views.ListObjectView.as_view(), name='list-object'),
# ]

