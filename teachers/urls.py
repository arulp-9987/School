from django.urls import path

from .views import (
    TeacherListView,
    TeacherDetailView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView
)


urlpatterns = [

    path(
        '',
        TeacherListView.as_view(),
        name='teacher_list'
    ),

    path(
        'add/',
        TeacherCreateView.as_view(),
        name='teacher_create'
    ),

    path(
        'view/<int:pk>/',
        TeacherDetailView.as_view(),
        name='teacher_detail'
    ),

    path(
        'edit/<int:pk>/',
        TeacherUpdateView.as_view(),
        name='teacher_update'
    ),

    path(
        'delete/<int:pk>/',
        TeacherDeleteView.as_view(),
        name='teacher_delete'
    ),

]