from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Ensure this value contains only letters, numbers, and underscore.'

        self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not value.isalnum():
            raise ValidationError(self.message)