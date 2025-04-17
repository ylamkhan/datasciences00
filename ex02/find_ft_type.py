"""
function in python is scop for instructions



"""


def all_thing_is_obj(obj: any) -> int:
    if type(obj) is list:
        print("List : <class 'list'>")
    elif type(obj) is tuple:
        print("Tuple : <class 'tuple'>")
    elif type(obj) is set:
        print("Set : <class 'set'>")
    elif type(obj) is dict:
        print("Dict : <class 'dict'>")
    elif type(obj) is str:
        print(f"{obj} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42
