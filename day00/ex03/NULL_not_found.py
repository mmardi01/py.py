def NULL_not_found(object: any) -> int:

    if(object == None):
        print("Nothing: None", type(object))
    elif(type(object) == float and object.__str__() == "nan"):
        print("Cheese: nan", type(object))
    elif(object == 0 and type(object) == int):
        print("Zero: 0", type(object))
    elif(object == ""):
        print("Empty:", type(object))
    elif(object == False):
        print("Fake: False", type(object))
    else:
        print("Type not Found")
        return 1
    return 0