from django.conf import settings

EMAIL_FIELD_NAME = getattr(settings, 'PASSWORD_RESET_EMAIL_FIELD_NAME', 'email')
SECOND_EMAIL_FIELD_NAME = getattr(settings, 'PASSWORD_RESET_SECOND_EMAIL_FIELD_NAME', None)
