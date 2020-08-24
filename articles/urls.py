from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleByIdAPIView, GenericApiView, ArticleViewSet
from rest_framework.routers import DefaultRouter
from articles.views import ArticleGenericViewSet, ArticleModelViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('generic/articles', ArticleGenericViewSet, basename='generic-article')
router.register('model/articles', ArticleModelViewSet, basename='model-article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('func-base/articles', article_list),
    path('func-base/articles/<int:pk>', article_detail),
    path('class-based/articles', ArticleAPIView.as_view()),
    path('class-based/articles/<int:id>', ArticleByIdAPIView.as_view()),
    path('generic/articles/<int:id>', GenericApiView.as_view()),
    path('generic/articles', GenericApiView.as_view()),
]
