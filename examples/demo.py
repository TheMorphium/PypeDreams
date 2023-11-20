import random
from PypeDreams import pype_dreamer

string = ''.join(f'{random.randint(0, 9)}' for _ in range(100))
print(pype_dreamer(string))