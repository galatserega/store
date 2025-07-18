from django import forms
from .models import Order
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше ім’я', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField(
        label='Підтвердіть, що ви не робот',
        error_messages={
            'required': 'Будь ласка, заповніть капчу.',
            'invalid': 'Невірна капча. Спробуйте ще раз.'
        }
    )



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

