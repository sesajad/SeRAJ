from django.urls import include, path
from django.contrib import admin
from django.conf.urls import handler404, handler500, handler403

from users.views.users import error_403, error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('rooms.urls')),
    path('', include('reservation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


handler404 = error_404
handler403 = error_403