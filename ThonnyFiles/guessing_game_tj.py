import random

def easyLevel():
    secret_no = random.randrange(1, 10)
    prompt = int(input('Enter a number (from 1-10): '))    
    
    if prompt == secret_no and prompt < 10:
        return f'Yes! it is {prompt}'
    else:
        return f'You\'re wrong! it\'s {secret_no}'
print(easyLevel())


def mediumLevel(secret_no):
    while True:
        prompt = int(input('Enter a number (from 11-100): '))
        secret_no = random.randrange(10, 100)
        
        if prompt == secret_no and prompt > 10:
            return f'Yes! it is {prompt}'
        else:
            return f'You\'re wrong it\'s {secret_no}'
print(mediumLevel("test"))
