import numpy as np
from hashlib import sha256

with open("name_list.txt", "r") as f:
    name_list = f.read().splitlines()

name_with_numbers = np.asarray(
    [
        name + str(np.random.randint(100000, 1000000)) for name in name_list
    ]
)

shuffled_names = name_with_numbers.copy()
while np.any(shuffled_names == name_with_numbers):
    np.random.shuffle(shuffled_names)
# Remove numbers from the names
shuffled_names = [name[:-6] for name in shuffled_names]
hash_list = [sha256(name.encode()).hexdigest() for name in name_with_numbers]

with open("hash_list.txt", "w") as f:
    f.write("\n".join([h + " " + n for h, n in zip(hash_list, shuffled_names)]))

for name in name_with_numbers:
    print(f"https://t.me/sams_secret_santa_bot?start={name}")

h_dict = dict(zip(hash_list, shuffled_names))

for name in name_with_numbers:
    print(name, h_dict[sha256(name.encode()).hexdigest()])
