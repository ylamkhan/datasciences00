"""
"""


def NULL_not_found(object: any) -> int:
    # print(type(object)
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif type(object) is float and object != object:  # NaN check
        print("Cheese: nan <class 'float'>")
    elif type(object) is int and object == 0:
        print("Zero: 0 <class 'int'>")
    elif type(object) is str and object == '':
        print("Empty: <class 'str'>")
    elif type(object) is bool and object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not found")
        return 1
    return 0


# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
