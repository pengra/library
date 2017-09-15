from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'dashboard/students/$', views.DashboardStudentView.as_view(), name='dashboard-student'),
    url(r'dashboard/students/logout/$', views.DashboardStudentLogout.as_view(), name='dashboard-student-logout'),
    url(r'dashboard/students/search/$', views.DashboardStudentSearch.as_view(), name='dashboard-student-search'),
    url(r'dashboard/students/edit/$', views.DashboardStudentEdit.as_view(), name='dashboard-student-edit'),
    url(r'dashboard/students/edit/(?P<student>[0-9]+)/$', views.DashboardStudentEdit.as_view(), name='dashboard-student-edit'),
    url(r'dashboard/kiosk/$', views.DashboardKioskView.as_view(), name='dashboard-kiosk'),
    url(r'dashboard/poll/$', views.DashboardPollView.as_view(), name='dashboard-poll'),
    # Dead
    url(r'dashboard/report/$', views.DashboardReportsView.as_view(), name='dashboard-reports'),
    url(r'dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'dashboard/export/sessions/today/$', views.DashboardExportView.as_view(), name='dashboard-export'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/$', views.KioskView.as_view(), name='kiosk-page'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/poll/$', views.KioskPollView.as_view(), name='kiosk-poll'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/ping/$', views.kiosk_ping_json, name='kiosk-ping'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/image/$', views.kiosk_image_json, name='kiosk-image'),
    url(r'help/report/$', views.BugSplatView.as_view(), name='bugsplat'),
    url(r'^$', views.CoverView.as_view(), name='index'),
]
