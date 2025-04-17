"""
            Data stracture in Python:
1)- List: daynamic array
        declaration:
            Name_list = [] --> declaration list empty
            Name_list = [1,'y',14.5,"hello"] --> declaration and
            inslisation
            Name_list = list() --> just declaratin a list
            Name_list = [0] * 3 --> declaration and inslisation
              by 0 [0,0,0]
        Function:
            Name_list.append(x) : this function add element to end
            for list;
            Name_list.extend(x) : Extend the list by appending all
            the items from the iterable. Similar to a[len(a):] =
              iterable
            Name_list.insert(pos, x) : add element to a postion;
            Name_list.remove(x): remove first element in list;
            Name_list.pop([i]): remove element in position;
            Name_list.clear(): remeove all list;
            Name_list.index(x[, start[, end]]) : Return zero-based
            index in the list of the first item whose value is equal to x.
            Raises a ValueError if there is no such item.
            Name_list.count(x) : Return the number of times x appears in
            the list.
            Name_list.sort(*, key=None, reverse=False): Sort the items of the
            list in place (the arguments can be used for sort
            customization, see sorted() for their explanation).
            Name_list.reverse(): Reverse the elements of the list in place.
            Name_list.copy(): Return a shallow copy of the list.
            Similar to a[:].


2)- Set: like List but no duplicate elements;

3)-Tuples:like List but Tuple:
        Feature	        List	            Tuple

        Mutable	        ✅ Yes	            ❌ No
        Syntax	        [ ]	( )
        Speed	        Slower	            Faster
        Use case	    Dynamic data	Fixed data
        Methods	Many	Few

4)- Dictionary: Data structer Key-Value:

        Declaratin:
            Name_dict = {
                "name": "Youssef",
                "age": 25,
                "country": "Morocco"
            } : declaration and inslization;
            Name_dict = {} : eclaration empty dict;


        Method	        Description

        .keys()	        Returns all keys
        .values()	    Returns all values
        .items()	    Returns key-value pairs
        .get(key)	    Safe way to get a value
        .pop(key)	    Removes key and returns value
        .update(dict2)	Merge another dictionary

"""

""" print() : function for disply in stdout;
    input() : function for read in stdin;
"""
ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Morocco!")
ft_set = {"Hello", "Ben Guerir!"}
ft_dict = {"Hello": "1337!"}

# your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
