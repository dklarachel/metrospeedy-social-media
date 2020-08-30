from csv_ops import get_hashtags, write_hashtags, get_data, get_col, get_col_names, write_data_from_list
from dict_ops import sort_dict_nums, keys_from_tuple

import pprint
import numpy as np
import csv 

import instagram
import linkedin

from settings import IG_USERNAME, IG_PASSWORD, LI_EMAIL, LI_PASSWORD

instagram.login(
    username = IG_USERNAME,
    password = IG_PASSWORD
)

instagram_values = instagram.search_query(
    search_list = get_hashtags()
)

linkedin.login(
    email = LI_EMAIL,
    password = LI_PASSWORD
)

linkedin_values = linkedin.search_query(
    search_list = get_hashtags()
)

write_hashtags(
    instagram_values = instagram_values,
    linkedin_values = linkedin_values
)

'''
get each column of hashtag counts 
sort column from greatest to least
print sorted hashtags 
'''

social_media = get_col_names("./csv/hashtags copy.csv")

def get_ordered_lists ():
    sorted_list = []
    for platform in social_media:
        hashtag_data = get_col(
            file = "./csv/hashtags copy.csv",
            series = "hashtag",
            column = platform
        )
        hashtag_tuple = sort_dict_nums(hashtag_data, True)
        sorted_hashtags = keys_from_tuple(hashtag_tuple)
        hashtag_list = []
        for i in sorted_hashtags:
            hashtag_list.append(i)
        hashtag_list.insert(0, platform)
        sorted_list.append(hashtag_list)
    return sorted_list

data = get_ordered_lists()
data_transposed = np.transpose(data).tolist()

write_data_from_list(
    file = "./csv/hashtags ordered.csv",
    fieldnames = social_media,
    list = data_transposed
)














