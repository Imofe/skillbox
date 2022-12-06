def slicer( tuple, element):
    if element in  tuple:
        if tuple.count(element) > 1:
            first_index = tuple.index(element)
            second_index = tuple.index(element, first_index + 1) + 1
            return tuple[first_index:second_index]
        else:
            return tuple[tuple.index(element):]
    else:
        return ()


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
