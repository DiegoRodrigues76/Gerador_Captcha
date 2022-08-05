from captcha.image import ImageCaptcha 

image = ImageCaptcha(width = 280, height = 90)

captcha_texto = 'RECAPTCHA'

data = image.generate(captcha_texto)

image.write(captcha_texto, 'captcha.png')
