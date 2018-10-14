from django import forms
from django.core.exceptions import ValidationError

from .helpers import generate_captcha


class LiteCaptchaWidget(forms.Widget):
    input_type = 'text'
    template_name = 'lite_captcha/forms/widgets/input.html'

    def __init__(self, attrs=None):
        self.path = None
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['path'] = self.path
        return context


class LiteCaptchaField(forms.Field):
    def __init__(self, *, required=True, widget=None, label=None, initial=None, help_text='', error_messages=None,
                 show_hidden_initial=False, validators=(), localize=False, disabled=False, label_suffix=None):
        self.path = None
        self.letters = None
        self.session = None
        self.widget = LiteCaptchaWidget()
        super().__init__(required=required, widget=widget, label=label, initial=initial, help_text=help_text,
                         error_messages=error_messages, show_hidden_initial=show_hidden_initial, validators=validators,
                         localize=localize, disabled=disabled, label_suffix=label_suffix)

    def validate(self, value):
        super().validate(value)

        captcha = self.session.get('captcha', None)
        if captcha is None:
            raise ValidationError('Invalid captcha code')

        if value != captcha:
            raise ValidationError('Invalid captcha code')

    def get_bound_field(self, form, field_name):
        self.letters, self.path = generate_captcha()
        self.session['captcha'] = self.letters
        self.widget.path = self.path
        return super().get_bound_field(form, field_name)
