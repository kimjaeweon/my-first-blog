from django.conf.urls import include, url
from django.contrib import admin

from mysite.views import HomeView
#from bookmark.views import BookmarkLV, BookmarkDV

app_name='bookmark'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', HomeView.as_view(), name='home'),

    # Class-based views for Bookmark app
    #url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]