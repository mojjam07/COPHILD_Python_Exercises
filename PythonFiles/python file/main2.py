from sys import path

path.append('..\\packages')

#import extra.iota
#print(extra.iota.funI())

# -- This is also valid instead line 5 & 6 --
#from extra.iota import funI
#print(funI())

import extra.good.best.sigma
from extra.good.best.tau import funT

# -- Aliasing --
#import extra.good.best.sigma as sig
#from extra.good.alpha as alp

#print(sig.funS())
#print(alp.funA())

print(extra.good.best.sigma.funS())
print(funT())