from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.db import models


class Transaction(models.Model):
    source_bank = models.CharField('Banco de origem', max_length=100)
    origin_agency = models.CharField('Agencia de origem', max_length=4)
    origin_account = models.CharField('Agencia de origem', max_length=7)
    destination_bank = models.CharField('Banco de origem', max_length=100)
    destination_agency = models.CharField('Agencia de origem', max_length=4)
    destination_account = models.CharField('Banco de origem', max_length=100)
    transaction_amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    transaction_datetime = models.DateTimeField('Date e Hora')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Register(models.Model):
    created_at = models.DateTimeField('Data de importação', auto_now_add=True)
    date = models.DateField('Data da transação')


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email username must be set')

        username = username # TODO: Normalizar
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.email_user('Senha aleatoria', f'Sua senha é : {password}', 'minhaaplicao@emial.com')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        if password is None:
            password = self.make_random_password(length=6, allowed_chars="0123456789")
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    App base User class.
    Username and password are required. Other fields are optional.
    """

    username = models.CharField(_('user name'), max_length=150, blank=True, unique=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
