from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from blog.views.article import ArticleViewSet
from blog.views.login import LogInView
from blog.views.signup import SignupView
from blog.views.user import UserMeView

api_urls = [
    path(r"signup/", SignupView.as_view(), name="signup"),
    path(r"login/", LogInView.as_view(), name="login"),
    path(r"users/me/", UserMeView.as_view(), name="me"),
]

default_router = DefaultRouter()


default_router.register(r"articles", ArticleViewSet, basename="articles")

api_urls += default_router.urls

urlpatterns = [
    re_path(r"api/", include(api_urls)),
]
