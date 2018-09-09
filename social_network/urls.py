from rest_framework import routers
from social_network.views import UserView, PostView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)

# urlpatterns = [
#     path('user/', UserView.as_view()),
# ]

urlpatterns = router.urls

