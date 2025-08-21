class calculator:
#your code here
    # decorator
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for i in range(len(V1)):
            res += V1[i] * V2[i]
        print(f"Dot product is: {res}")
    # decorator
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res: list[float] = []
        for i in range(len(V1)):
            res.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {res}")
        
    #your code here
    # decorator
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res: list[float] = []
        for i in range(len(V1)):
            res.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {res}")


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
