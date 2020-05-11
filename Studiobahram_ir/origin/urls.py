from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('api/', views.post_api, name='post_api'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('bots.html', views.bots, name='bots'),
    path('about.html', views.about, name='about'),
    path('index-fa.html', views.fa_index, name='fa_index'),
    path('bots-fa.html', views.fa_bots, name='fa_bots'),
    path('about-fa.html', views.fa_about, name='fa_about'),
    path('posts/', views.posts, name='posts'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
'''