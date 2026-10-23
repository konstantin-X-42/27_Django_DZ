from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # -27- Указываем email и остальные три поля из ТЗ
        fields = ('email', 'phone', 'country', 'avatar')

        # -27- Стилизуем дополнительные поля формы крупными классами Bootstrap
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@mail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '+7...'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Страна'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -27- Стилизуем поля паролей крупными классами Bootstrap и добавляем подсказку про 8 символов
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите пароль не менее 8 символов'
            })
            self.fields['password1'].label = 'Пароль'

        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Повторите пароль'
            })
            self.fields['password2'].label = 'Подтверждение пароля'


# -27- Форма для редактирования профиля пользователя (также увеличиваем поля)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }



#-------27-----рабочий мелко
#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from users.models import User
#
#
# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         # -27- Указываем email и остальные три поля из ТЗ.
#         # Поля для паролей (password1 и password2) добавятся автоматически из UserCreationForm!
#         fields = ('email', 'phone', 'country', 'avatar')
#
#         # -27- Стилизуем дополнительные поля формы с помощью Bootstrap классов
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7...'}),
#             'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Страна'}),
#             'avatar': forms.FileInput(attrs={'class': 'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # -27- Стилизуем и переименовываем два стандартных поля паролей, которые предоставляет Django
#         if 'password1' in self.fields:
#             self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите пароль'})
#             self.fields['password1'].label = 'Пароль'
#         if 'password2' in self.fields:
#             self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})
#             self.fields['password2'].label = 'Подтверждение пароля'
#
#
# # -27- Форма для редактирования профиля пользователя (оставляем без изменений)
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # -27- Поля, доступные пользователю для изменения в профиле
#         fields = ('email', 'phone', 'country', 'avatar')
#
#         # -27- Стилизуем поля формы с помощью Bootstrap классов
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'country': forms.TextInput(attrs={'class': 'form-control'}),
#             'avatar': forms.FileInput(attrs={'class': 'form-control'}),
#         }



#-------27-----рабочий

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
# from users.models import User
#
#
# class UserRegisterForm(UserCreationForm):
#     # -27- Добавляем отдельное поле для подтверждения пароля
#     password_confirm = forms.CharField(
#         label='Подтверждение пароля',
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'})
#     )
#
#     class Meta:
#         model = User
#         # -27- Указываем поля, которые пользователь будет заполнять при регистрации
#         fields = ('email', 'phone', 'country', 'avatar')
#
#         # -27- Стилизуем поля формы с помощью Bootstrap классов
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7...'}),
#             'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Страна'}),
#             'avatar': forms.FileInput(attrs={'class': 'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # -27- Добавляем Bootstrap класс для стандартных полей паролей из UserCreationForm
#         if 'password1' in self.fields:
#             self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})
#         if 'password2' in self.fields:
#             self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})
#
#     def clean(self):
#         cleaned_data = super().clean()
#         # -27- Django стандартно сохраняет первый пароль в поле 'password1' внутри UserCreationForm
#         password = cleaned_data.get("password1")
#         password_confirm = cleaned_data.get("password_confirm")
#
#         # -27- Проверяем совпадение паролей для обработки потенциальных ошибок
#         if password and password_confirm and password != password_confirm:
#             raise ValidationError("Пароли не совпадают!")
#
#         return cleaned_data
#
#
# # -27- Форма для редактирования профиля пользователя
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # -27- Поля, доступные пользователю для изменения в профиле
#         fields = ('email', 'phone', 'country', 'avatar')
#
#         # -27- Стилизуем поля формы с помощью Bootstrap классов
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'country': forms.TextInput(attrs={'class': 'form-control'}),
#             'avatar': forms.FileInput(attrs={'class': 'form-control'}),
#         }
