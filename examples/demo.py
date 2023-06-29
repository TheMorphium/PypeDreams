import random
from PypeDreams import pype_dreamer

string = ''
i = 0
while i < 100:
  string += f'{random.randint(0,9)}'
  i += 1

print(pype_dreamer(string))