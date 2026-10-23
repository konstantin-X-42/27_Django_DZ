from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('catalog.urls', namespace='catalog')),  # Подключение маршрутов приложения catalog

                  # Подключение маршрутов приложения блога (все адреса будут начинаться с blogs/)
                  path('blogs/', include('blog.urls', namespace='blog')),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)  # правильная обработка статических файлов



#---24--

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('catalog.urls', namespace='catalog')),  # Подключение маршрутов приложения catalog
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      # правильная обработка статических файлов
