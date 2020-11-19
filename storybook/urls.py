from django.urls import path
from storybook.views import StoryListView, StoryCreate, StoryUpdate, StoryDelete

urlpatterns = [
    path('', StoryListView.as_view(), name='story-list'),
    path('add/', StoryCreate.as_view(), name='story-add'),
    path('edit/<int:pk>', StoryUpdate.as_view(), name='story-edit'),
    path('delete/<int:pk>', StoryDelete.as_view(), name='story-delete'),
]
