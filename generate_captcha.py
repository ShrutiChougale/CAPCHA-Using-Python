from captcha.image import ImageCaptcha

image= ImageCaptcha(width=280, height=90)
captcha_text ="A9K7P"


image.write(captcha_text, 'captcha.png')
print("Captcha generated :", captcha_text)