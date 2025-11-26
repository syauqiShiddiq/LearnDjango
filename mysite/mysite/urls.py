from django.contrib import admin
from django.urls import include, path  # <--- Pastikan 'include' ada
from django.conf import settings       # <--- Tambahkan ini untuk cek mode DEBUG

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# --- KODE DEBUG TOOLBAR (Gunakan format standar ini) ---
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # Perhatikan kita menggunakan 'include(debug_toolbar.urls)'
        # BUKAN 'debug_toolbar_urls'
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns