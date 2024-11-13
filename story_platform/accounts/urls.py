from django.urls import path
from .views import RegisterView, LoginView, StoryDetailView, GenerateFourDigitCodeView
from .views import ProfileDetailView, MyStoriesView, AllStoriesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('edit-profile/', ProfileDetailView.as_view(), name='edit-profile'),
    path('my-stories/', MyStoriesView.as_view(), name='my-stories'),
    path('all-stories/', AllStoriesView.as_view(), name='all-stories'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('generate-code/', GenerateFourDigitCodeView.as_view(), name='generate-code'),
]


