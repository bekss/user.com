from django import forms
from .models import Man

SERIAL_CHOICES = (
    ('1', 'ID'),
    ('2', 'AN'),
    ('3', 'AC')
)


class Date(forms.DateInput):
    input_type = 'date'


class NewMann(forms.ModelForm):
    class Meta:
        model = Man
        fields = (
            'number', 'fname', 'name', 'lname', 'address', 'birtday', 'passport', 'number_pass', 'body_pass', 'pin',
            'file','role')
        widgets = {
            'number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'placeholder': '996XXXXXXXXX','pattern':'^996\d{9}$','title':'номериңизди ушул форматта жазыңыз 996123456789'}),
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамиля','pattern':'^(([А-Я]{1}[а-я]+$)|([А-Я]{1}[а-я]+\s$))','title':'Баш тамга менен баштап кирилица турундө жазыңыз' }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя','pattern':'^(([А-Я]{1}[а-я]+$)|([А-Я]{1}[а-я]+\s$))','title':'Баш тамга менен баштап кирилица турундө жазыңыз'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество','pattern':'^(([А-Я]{1}[а-я]+$)|([А-Я]{1}[а-я]+\s$))','title':' Баш тамга менен баштап кирилица турундө жазыңыз'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адресс'}),
            'birtday': forms.TextInput(attrs={'class': 'form-control'}),
            'passport': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
            'role': forms.Select(attrs={'class': 'custom-select mb-4'}),
            'number_pass': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'паспортунуздун номери','pattern':'^((\w{7}$)|(\w{7}\s$))','title':'паспорттун номерин жазыңыз сандарды гана'}),
            'body_pass': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Паспортту берген мекеме'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Паролунуз','pattern':'^((\d{4,8})|(\d{4,8}\s))','title':'сыр сөзуңузду жазыңыз сан турунндө'}),
            'birtday': Date(attrs={'class': 'form-control'})

        }





# number = forms.CharField('Номер телефона', max_length=20)
    # fname = forms.CharField('Фамиля', max_length=25)
    # name = forms.CharField('Имя', max_length=25)
    # lname = forms.CharField('Отчество', max_length=25)
    # address = forms.CharField('Адресс', max_length=50) ,'pattern':'^((\w+$)|(\w+\s$))','title':'напишите Адресс правильно'
    # birtday = forms.DateField('Дата рождения')
    # passport = forms.CharField('Серия паспорта (ID,AC,AN)', max_length=2)
    # number_pass = forms.CharField('Номер паспорта', max_length=20)
    # body_pass = forms.CharField('Орган, который дал паспорт', max_length=3)#[A-Z]{1,5}
    # pin = forms.CharField('Пароль', max_length=6)
    # file = forms.FileField('Ваше изображение')
    # role = forms.CharField('Роль', max_length=11)