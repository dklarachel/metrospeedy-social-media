from csv_ops import get_hashtags
from csv_ops import write_hashtags
from csv_ops import get_data
from csv_ops import get_col
from csv_ops import get_col_names
from csv_ops import write_data_from_list

from dict_ops import sort_dict_nums
from dict_ops import keys_from_tuple

import pprint
import numpy as np
import csv 

# import instagram
# import linkedin

# instagram.login(
#     username = "metrospeedy",
#     password = "Summer2017!"
# )

# instagram_values = instagram.search_query(
#     search_list = get_hashtags()
# )

# linkedin.login(
#     email = "rachlin440@gmail.com",
#     password = "purpleepix4"
# )

# linkedin_values = linkedin.search_query(
#     search_list = get_hashtags()
# )

# write_hashtags(
#     instagram_values = instagram_values,
#     linkedin_values = linkedin_values
# )

'''
get each column of hashtag counts 
sort column from greatest to least
print sorted hashtags 
'''

social_media = get_col_names("hashtags copy.csv")

def get_ordered_lists ():
    sorted_list = []
    for platform in social_media:
        hashtag_data = get_col(
            file = "hashtags copy.csv",
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
    file = "hashtags ordered.csv",
    fieldnames = social_media,
    list = data_transposed
)
















