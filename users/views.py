from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from users.forms import UserRegisterForm


class RegisterView(CreateView):
    # -27- Указываем нашу кастомную форму регистрации
    form_class = UserRegisterForm
    # -27- Путь к HTML-шаблону, который мы создадим на следующем шаге
    template_name = 'users/register.html'
    # -27- Перенаправление пользователя на страницу входа после успешной регистрации
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # -27- Сохраняем пользователя в базу данных
        user = form.save()

        # -27- Формируем приветственное письмо согласно ТЗ
        subject = 'Добро пожаловать!'
        message = f'Вы успешно зарегистрировались на нашем сайте интернет-магазина.\nВаш логин (email): {user.email}'
        # -27- Берем email отправителя из настроек или ставим дефолтный
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost')
        recipient_list = [user.email]

        try:
            # -27- Отправляем письмо. fail_silently=False поможет увидеть ошибку, если что-то пойдет не так
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            # -27- Если почта не отправилась (например, нет сети), проект не должен падать с ошибкой
            print(f"Ошибка при отправке приветственного email: {e}")

        return super().form_valid(form)
