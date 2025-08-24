def calculateMean(arr: list[float]):
    res : int = 0
    for i in arr:
        res += i
    return res / len(arr)


def getQuartile(list1: list[float], list2: list[float], _len: int):
    med_index = int(len(list1) / 2)
    print(list1)
    print(list2)
    print(list1[med_index - 1])
    print(list1[med_index])
    if _len % 4 == 0:
        print(f"quartile : {[float((list1[med_index - 1] + list1[med_index]) / 2), float((list2[med_index - 1] + list2[med_index]) / 2)]}")
    else:
        print(f"quartile : {[float(list1[med_index]), float(list2[med_index -1])]}")

def ft_statistics(*args, **kwargs) -> None:
   for val in kwargs.values():
        if len(args) == 0:
            print("ERROR")
        elif val == "mean":
            print(f"mean : {calculateMean(args)}")
        elif val == "median":
            med_index = int(len(args) / 2)
            _sorted = sorted(args)
            if len(args) % 2 == 0:
                print(f"median : {(_sorted[med_index - 1] + _sorted[med_index]) / 2}")
            else:
                print(f"median : {_sorted[med_index]}")
        elif val == "quartile":
            med_index = int(len(args) / 2)
            _sorted = sorted(args)
            if len(args) % 2 == 0:
                getQuartile(_sorted[0 : med_index], _sorted[med_index: len(args)], len(args))
            else:
                getQuartile(_sorted[0 : med_index], _sorted[med_index + 1: len(args)], len(args))


    

