import numpy as np
from hashlib import sha256

with open("name_list.txt", "r") as f:
    name_list = f.read().splitlines()

np.random.shuffle(name_list)
shift = np.random.randint(0, len(name_list))

sha256(name_list[0].encode()).hexdigest()
