# -*-encoding:utf-8-*-

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView


urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info")
]