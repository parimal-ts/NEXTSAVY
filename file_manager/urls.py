from django.urls import path, include
from .views import upload, file_list, GetFileListView

urlpatterns = [
    path('views', file_list, name="file-list"),
    path('upload', upload, name="upload"),
    path('view/<str:pk>/', GetFileListView.as_view(), name="view-file")
]