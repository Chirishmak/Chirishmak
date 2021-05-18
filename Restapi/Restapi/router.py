from Resume.models import resume
from Resume.viewset import resumeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('resume',resumeViewSet)