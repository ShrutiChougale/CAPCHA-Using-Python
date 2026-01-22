from captcha.image import ImageCaptcha
import random
import string

# Create captcha generator
image = ImageCaptcha(width=280, height=90)

# Generate random text
captcha_text = ''.join(
    random.choices(string.ascii_uppercase + string.digits, k=5)
)

# Save captcha image
image.write(captcha_text, "captcha.png")

print("CAPTCHA text:", captcha_text)
print("CAPTCHA image saved as captcha.png")
