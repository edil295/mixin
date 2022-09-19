from django.contrib import admin
from django.urls import path, include
from book import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.CategoryGenericsViewSet, basename='category')
router.register('book', views.BookGenericsViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('create/', views.CategoryCreateAPIView.as_view()),




    # path('', views.CategoryGenericsViewSet.as_view({
    #     'get':'list',
    #     'post':'create'
    # })),
    #
    # path('<int:pk>/', views.CategoryGenericsViewSet.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'delete':'destroy'
    # }))

    # path('update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    # path('retrieve/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),

]
