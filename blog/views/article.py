from django.contrib.auth.decorators import permission_required
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from blog.models import Article
from blog.serializers.article import ArticleSerializer


@method_decorator(name="create", decorator=permission_required("blog_api.add_article"))
@method_decorator(name="retrieve", decorator=permission_required("blog_api.add_article"))
@method_decorator(
    name="partial_update", decorator=permission_required("blog_api.change_article")
)
@method_decorator(name="update", decorator=permission_required("blog_api.change_article"))
@method_decorator(
    name="destroy", decorator=permission_required("blog_api.delete_article")
)

class ArticleViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        print(request)

