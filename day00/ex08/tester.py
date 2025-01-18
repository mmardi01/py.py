from time import sleep
from Loading import ft_tqdm
from tqdm import tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)

print(tqdm.__doc__)
for elem in tqdm(range(333)):
    sleep(0.005)
