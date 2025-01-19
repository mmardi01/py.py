

def count_in_list(lst: list, el):

    '''
    ags: list, element to count in the list
    return the count of el in the list
    '''

    count = 0
    for x in lst:
        if x == el:
            count += 1
    return count
