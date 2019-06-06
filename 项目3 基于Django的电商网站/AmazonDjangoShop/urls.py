from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from shop import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app_views.home, name='home'),
    url(r'^(?P<cat_slug>[-\w]+)/(?P<asin>[-\w]{10})/$', app_views.product_page, name='product_page'),
    url(r'^(?P<slug>[-\w]+)/$', app_views.category_view, name='category_view'),
    url(r'^page/(?P<slug>[-\w]+)/$', app_views.static_page, name='static_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
