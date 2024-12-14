def all_thing_is_obj(object: any) -> int:

    list = ["list", "tuple", "set", "dict"]

    if (type(object).__qualname__ in list):
        print(type(object).__qualname__.capitalize(), ":", type(object))

    elif (type(object).__qualname__ == "str"):
        print(object, "is in the kitchen :", type(object))

    else:
            print("Type not found")
            
    return 42
