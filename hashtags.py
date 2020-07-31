from csv_ops import get_hashtags
from csv_ops import write_hashtags

import instagram
import linkedin

# instagram.login(
#     username = "metrospeedy",
#     password = "Summer2017!"
# )

# instagram_values = instagram.search_query(
#     search_list = get_hashtags()
# )

linkedin.login(
    email = "rachlin440@gmail.com",
    password = "purpleepix4"
)

linkedin_values = linkedin.search_query(
    search_list = get_hashtags()
)

print(linkedin_values)
# write_hashtags(
#     instagram_values = instagram_values,
#     linkedin_values = linkedin_values
# )




