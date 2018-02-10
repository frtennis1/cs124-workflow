import numpy as np

x, y = np.random.randint(100), np.random.randint(100)

with open('tests/input3.txt', 'w') as f:
    f.write('%i %i' % (x,y))

with open('tests/output3.txt', 'w') as f:
    f.write('%i' % (x+y))
