from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView

# -27- Задаем имя пространства имен для приложения users
app_name = UsersConfig.name

urlpatterns = [
    # -27- Добавляем маршрут для страницы регистрации
    path('register/', RegisterView.as_view(), name='register'),
]
