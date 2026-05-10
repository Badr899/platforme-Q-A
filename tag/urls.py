from django.urls import path
from .views import tag_detail, manage_tags, delete_tag, update_tag

urlpatterns = [
    path('admin/tags/', manage_tags, name='manage_tags'),
    path('admin/tags/delete/<int:id>/', delete_tag, name='delete_tag'),
    path('admin/tags/update/<int:id>/', update_tag, name='update_tag'),
    path('<int:id>/', tag_detail, name='tag_detail'),
]