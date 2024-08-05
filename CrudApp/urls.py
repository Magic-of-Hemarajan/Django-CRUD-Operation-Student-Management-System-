from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('read/', views.read, name='read'),
    path('read/deleted/<int:id>/', views.student_deleted, name='student_deleted'),
    path('read/deleted/update/<int:id>/', views.student_update, name='student_update'),
    # path('read/deleted/', views.student_deleted, name='deleted'),
]
