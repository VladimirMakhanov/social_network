from rest_framework import routers
from django.urls import path
from social_network.views import UserView, PostView, BearerTokenObtainPairView, BearerTokenRefreshView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)

urlpatterns = router.urls

urlpatterns += [
    path('token/', BearerTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', BearerTokenRefreshView.as_view(), name='token_refresh'),
]