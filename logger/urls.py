from django.conf.urls import url, include
from rest_framework import routers
from logger import api
from logger import views

router = routers.DefaultRouter()
router.register(r'sessions', api.StudentSessionViewSet, base_name='session')
router.register(r'kiosks', api.KioskViewSet)
router.register(r'poll-questions', api.PollQuestionViewSet)
router.register(r'poll-choices', api.PollChoiceViewSet)
router.register(r'imagecards', api.ImageCardViewSet)


urlpatterns = [
    url(r'^$', views.OverviewView.as_view(), name='index'),
    url(r'^kiosk/$', views.KioskView.as_view(), name='kiosk'),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api/v1/export/$', views.ReportExportView.as_view(), name='export'),
]