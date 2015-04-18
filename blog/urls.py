from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.articles,name = 'articles'),
	url(r'^article/(?P<article_id>\d+)/$',views.article,name = 'article_deatil'),
        url(r'^search/$', views.search,name = 'search'),
      #  url(r'^search-form/$', views.search_return,name = 'search_form'),
        
]
