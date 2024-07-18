import re

print(dir(re))
print(len(dir(re)))

x = 'Dev. Akin uses setup.py file'
y = re.findall('s', x)
print(y)

for i in y:
    print(i)
    

#intro = 'My name is dev. Mojjam'
#prompt = input('Enter a search name: ')

#result = re.search(prompt, intro)

#if prompt in intro:
    #print(f"'{prompt}' is present!")
#else:
    #print(f"'{prompt}' is not present!")

#txt = "76543254698"

#x = re.sub('\S', '*', 3)
#print(x)

txt = "76543254698"
y = txt.replace(txt[6:], '****')
print(y)