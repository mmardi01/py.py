import math
import os

def ft_tqdm(lst: range):
    t = len(lst)
    line = []
    columns = os.get_terminal_size().columns - 50
    for i in range(columns):
        line.append(' ')
    for index, val in enumerate(lst, 1):
        per = round(index * (100/t))
        col = math.floor((per / 100) * columns)
        for i in range(col):
            if i != columns - 1:
                line[i] = "="
            else:
                line[i] = ">"
                
        s = f"\r {per}% |{''.join(line)}| {index}/{t}"
        print(s, end="")
        yield index
    print()



