from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from beauty import views as beautyViews
from masters import views as masterViews
from accounts import views as accountViews
from zapis import views as zapisViews

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', beautyViews.signup, name = 'signup'),
    path('', beautyViews.home, name='home'),
    path('about/', beautyViews.about, name = 'about'),
    path('uslugi/', include('beauty.urls')),
    path('masters/', masterViews.masters, name='masters'),
    path('masters/', include('masters.urls')),
    path('reviews/', beautyViews.allreviews, name = 'allreviews'),
    path('accounts/', include('accounts.urls')),
    path('works/', beautyViews.allworks, name = 'allworks'),
    path('zapis/', zapisViews.chooseType, name = 'zapis'),
    path('zapis/', include('zapis.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)