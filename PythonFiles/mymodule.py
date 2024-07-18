def greeting(name):
    print(name + '','welcome to this module')

mylist = ['Akin', 'Yellow', 'Ruger', 'Girls']
# mylist.append('Me')
# mylist.extend(['Fun', 'Everyone', 'Follow'])
var = input('Enter string: ')
for x in mylist:
    if x == var:
        print(x,'mount')
    else:
        print('nothing')
        break