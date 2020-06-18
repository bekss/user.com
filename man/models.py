from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Man(models.Model):
    SERIAL_CHOICES = (
        ('ID', 'ID'),
        ('AC', 'AC'),
        ('AN', 'AN')
    )
    number = models.CharField('Телефон номериниз', max_length=12, unique=True,
                              validators=[RegexValidator(regex='996[0-9]{9}$|996[0-9]{9}$\s')],
                              error_messages={'invalid': 'Номерди туура жазыңыз'})
    fname = models.CharField('Фамиля', max_length=25,
                             validators=[RegexValidator(regex='[А-Я]{1}[а-я]+$|[А-Я]{1}[а-я]+\s$')],
                             error_messages={'invalid': 'Фамилянызды баш тамга менен баштаңыз'})
    name = models.CharField('Имя', max_length=25,
                            validators=[RegexValidator(regex='[А-Я]{1}[а-я]+$|[А-Я]{1}[а-я]+\s$')],
                            error_messages={'invalid': 'Атыңызды баш тамга менен баштаңыз'})
    lname = models.CharField('Отчество', max_length=25)
    address = models.CharField('Адресс', max_length=50, unique=True)
    birtday = models.DateField('Туулган жылы')
    passport = models.CharField('Паспортуңуздун сериясы (ID,AC,AN)', max_length=2, choices=SERIAL_CHOICES)
    number_pass = models.CharField('Паспорт номери', max_length=7, unique=True)
    body_pass = models.CharField('Паспортту берген мекеме', max_length=12,
                                 validators=[RegexValidator(regex='[A-Z]{2,4}\s\d{2,4}-\d{2,4}$|[A-Z]{2,4}\s\d{2,8}$')],
                                 error_messages={'invalid': 'Берген мекемени туура жазыңыз'})
    pin = models.CharField('Пароль', max_length=6)
    file = models.FileField('Сиздин сурөтуңуз', upload_to='media/')
    role = models.CharField('Роль', max_length=11,
                            choices=(('Инструктор', 'Инструктор'), ('Координатор', 'Координатор'),
                                     ('Регистратор', 'Регистратор')))
    qrcode = models.ImageField(upload_to='media/users/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.generate_qr_code()
        super(Man, self).save(*args, **kwargs)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=2
        )
        data = 'users/%s' % self.number
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()
        buffer = BytesIO()
        img.save(buffer)
        filename = 'qrcode-%s.png' % self.number
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.tell(), None
        )
        self.qrcode.save(filename, filebuffer, save=False)

        # def save(self):
        #     self.generate_qr_code()
        # super(Man, self).save()

        # def get_absolute_url(self):
        #     return reverse('users', args=[self.id])

        # def get_url(self):
        #     return reverse('users', args=[str(self.id)])

        # @receiver(post_save, sender=Man)
        # def set_agreement_number(sender, instance, created=False, **kwargs):
        #     instance.generate_qr_code
        #     instance.save()

# def rex(val):
#     if not re.match('([A-Z]{2,4}\s\d{2,4}-\d{2,4}$)|([A-Z]{2,4}\s\d{2,8}$)', val):
#         raise ValidationError('Введите правильное значение ')


# ,validators=[validators.RegexValidator(regex=r'^\d[9]{1} \d[9]{1} \d[6]{1} \d[0-9]{9}$',code="Не правильный номер")]
#                               ,error_messages={'invalid':'Неправильный номер телефона'}
#
# ,validators=[RegexValidator(pin,message='Пароль должен состоять из 6 цифр')]
# ,validators=[RegexValidator(num_pass,message='Введите пожалуйста только цифры')],
# validators=[RegexValidator(num_validate, message='номер должен начинаться с 996XXXXXXXXX', code='Не правильный номер')],error_messages={'invalid': 'Неправильный номер телефона'},
# ,validators=[RegexValidator(fname_validate,message='Фамиля дожно начинаться с главной буквы')]
# ,validators=[RegexValidator(name_validate,message='Имя дожно начинаться с главной буквы')]
# ,validators=[RegexValidator(fname_validate,message='Отчество дожно начинаться с главной буквы')]
# ,validators=[RegexValidator(fname_validate,message='Адресс должно начинаться с главной буквы')]
