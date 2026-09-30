
from django.urls import include, path
from . import views
urlpatterns = [
    path('create/',views.create),
    path('display/',views.display),
    path('getstudents/',views.getStudent.as_view()),
    path('crud/',views.crudOperation.as_view()),
    path('data/<int:id>',views.getData.as_view())

]
