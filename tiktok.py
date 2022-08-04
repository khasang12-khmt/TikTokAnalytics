from TikTokApi import TikTokApi
from helpers import process_results
import pandas as pd
import sys

def get_data(hashtag):
    # - Data Crawling
    with TikTokApi(use_test_endpoints=True) as api:
        # Get data by hashtag
        trending = api.hashtag(name=hashtag)
        save = [video.info() for video in trending.videos()]

    # - Data Preprocessing
    data = process_results(save)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    get_data(sys.argv[1])


    