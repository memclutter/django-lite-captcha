# Django Lite Captcha

[![Language Python](https://img.shields.io/badge/language-python-blue.svg)](https://img.shields.io/badge/language-python-blue.svg)
[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)](https://github.com/memclutter/django-lite-captcha)

Lite captcha for django projects. This package don't use database for store captcha.

Detailed documentation is in the "docs" directory.

## Quick start

0. Install package

```
pip install lite_captcha
```

1. Add "lite_captcha" to your INSTALLED_APPS setting like this::

```python

INSTALLED_APPS = [
    # ...
    'lite_captcha',
]

```
2. Configure `MEDIA_URL` and `MEDIA_ROOT`:
3. Use form field in your forms:
```python
from django import forms
from lite_captcha.forms import LiteCaptchaField


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=Textarea)
    captcha = LiteCaptchaField(required=True)
```
4. Set session instance in views
```python
    # ... in some views

    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.fields['captcha'].session = request.session
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        form.fields['captcha'].session = request.session

    # ...
```
5. Override templates or use default.
