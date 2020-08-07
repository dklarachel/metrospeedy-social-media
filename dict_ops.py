def sort_dict_nums (dict, reverse):
    '''
    takes in dictionary, sorts using values, returns list of sorted keys \n
    numbers may be strings 
    '''
    # convert numbers in dictionary into int DT
    for key in dict:
        dict[key] =  int(float(dict[key]))

    # sort dictionary by values, return as list of tuples 
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=reverse)
    return sorted_dict

def keys_from_tuple (list):
    '''takes list of tuples representing key-value pairs, and returns list of the keys'''
    key_list = []
    for pair in list:
        key = pair[0]
        key_list.append(key)
    return key_list




