from csv_ops import get_hashtags
from csv_ops import write_hashtag

from instagram import login
from instagram import search_query

login(
    username = "metrospeedy",
    password = "Summer2017!"
)

search_query(search_list = get_hashtags())
