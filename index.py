import random
"""In JavaScript, the Array object has numerous useful methods.
It does not, however, contain a method that will randomize
the order of an array’s elements. Let’s create shuffle(arr),
to efficiently shuffle a given array’s values. Work in-place,
naturally. Do you need to return anything from your function?"""

def shuffle(list):
    for i in range(len(list)):
        random_index = random.randint(0, i)
        temp = list[i]
        list[i] = list[random_index]
        list[random_index] = temp
    return list
# print(shuffle([1,2,3,4,5]))

"""Lovely Burbank has a breathtaking view of the Los Angeles skyline.
Let’s say you are given an array with heights of consecutive buildings,
starting closest to you and extending away. Array [-1,7,3] would
represent three buildings: first is actually out of view below street
level, behind it is second at 7 stories high, third is 3 stories high
(hidden behind the 7-story). You are situated at street level.
Return array containing heights of buildings you can see, in order.
Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4].
As always with challenges, do not use built-in array functions such as unshift()."""

def visible_buildings(list):
    visible = []
    current_height = 0
    for height in list:
        if height > current_height:
            current_height = height
            visible.append(height)
    return visible
# print(visible_buildings([-1,1,1,7,3]))
# print(visible_buildings([0,4]))

"""Create a standalone function that accepts two arrays and combines their
values sequentially into a new array. Extra values from either array should
be included afterward. Given [4,15,100] and [10,20,30,40],
return new array containing [4,10,15,20,30,40,100]."""

def combine_lists(list_one, list_two):
    new_list = []
    for value in list_one:
        new_list.append(value)
    for value in list_two:
        new_list.append(value)
    return sorted(new_list)
# print(combine_lists([4,15,100], [10,20,30,40]))
