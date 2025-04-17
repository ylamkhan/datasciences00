"""
"""
# form filterstring import filterstring


# print(filter.__doc__)

def ft_filter(function, iterable):
    """
        - function: A function that returns either True or False.

        - iterable: The sequence to filter (like a list, tuple
            or string).

        - Returns a filter object, which is an iterator — you
            can convert it to a list or tuple.
    """
    if iterable is None:
        raise TypeError("'NoneType' object is not iterable")

    for item in iterable:
        if function is None:
            if item:
                yield item
        else:
            if function(item):
                yield item


# def is_even(n):
#     return n % 2 == 0
#     # print("hhhg")

# nums = "1 2 5"

# # print("filter")
# # result = filter(is_even, nums)
# # print(list(result))
# print("my filter")
# result = ft_filter(is_even, nums)
# print(list(result))
