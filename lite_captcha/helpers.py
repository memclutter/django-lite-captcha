import os
import random
import secrets
import string

from captcha.image import ImageCaptcha
from django.conf import settings


def generate_captcha():
    captchas_dir = os.path.join(settings.MEDIA_ROOT, 'captchas')
    if not os.path.exists(captchas_dir):
        os.mkdir(captchas_dir, 0o777)

    letters = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    filename = 'captcha_' + secrets.token_hex(8) + '.png'
    path = '/'.join([settings.MEDIA_URL.rstrip('/'), 'captchas', filename])
    img = ImageCaptcha().generate_image(letters)
    img.save(os.path.join(captchas_dir, filename))
    return letters, path
