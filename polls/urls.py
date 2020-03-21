from django.urls import path
from .views import IndexView, AnalyzeView
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')

]