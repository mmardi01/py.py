class calculator:
#your code here
    nums : list[int] = []

    def __init__(self, _nums : list[int]):
        self.nums = _nums

    def __add__(self, object) -> None:
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] + object
        print(self.nums)
    #your code here
    def __mul__(self, object) -> None:
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] * object
        print(self.nums)
    #your code here
    def __sub__(self, object) -> None:
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] - object
        print(self.nums)
#your code here
    def __truediv__(self, object) -> None:
        if object == 0:
            print("can't divide by 0")
            return
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] / object
        print(self.nums)

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 0

