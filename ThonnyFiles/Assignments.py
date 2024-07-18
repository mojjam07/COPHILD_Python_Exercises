msg = 'Attention Needed'

uni = []
dup = []

for e in msg:
    print(e)
    if e not in uni:
        
        uni.append(e)
        
    elif e not in dup:
        dup.append(e)
print('Duplicates:', dup)
print('Unique:', uni)

