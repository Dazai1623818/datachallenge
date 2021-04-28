# main program
import os
import json
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

directory = os.fsencode(r"D:\data")
dfx = pd.DataFrame([])

total_files = len([name for name in os.listdir('D:\data')])
counter = 0

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        counter += 1
        tweetlist = []
        with open(r'D:\data\{}'.format(filename)) as f:
            for line in f:
                if 'Exceeded connection limit for user' in line:
                    continue
                else:
                    tweetDict = json.loads(line)
                    if 'delete' in tweetDict.keys():
                        continue
                    else:
                        tweetlist.append(tweetDict)

            dfx = dfx.append((pd.DataFrame(tweetlist)).dropna(subset=["id", "created_at"]))

            progress = (counter / total_files) * 100
            print(f"{round(progress, 2)}%")
        continue


    else:
        continue

print(len(tweetlist))

# Dropping columns, datetime and new columns
x_dlt = [
    "geo", "display_text_range", "coordinates",
    "timestamp_ms", "contributors", "withheld_in_countries",
    "quote_count", "reply_count", "retweet_count", "favorite_count",
    ""

]

dfx.drop(x_dlt, axis='columns', inplace=True)

#Convert
dfx['created_at'] = pd.to_datetime(dfx['created_at'])
dfx.set_index(["created_at"], inplace=True)

dfx["Month"] = dfx.index.month.fillna(0.0).astype(int)
dfx["Day"] = dfx.index.day.fillna(0.0).astype(int)
dfx["DayOfYear"] = dfx.index.dayofyear.fillna(0.0).astype(int)
dfx["Year"] = dfx.index.year.fillna(0.0).astype(int)

dfu = pd.json_normalize(dfx["user"].values)
# dlt: Attributes to be deleted
users_dlt = [
    'url', "notifications", "follow_request_sent", "following", "lang",
    "time_zone", "utc_offset", "default_profile", "default_profile_image",
    "profile_link_color", "profile_sidebar_border_color", "profile_sidebar_fill_color",
    "profile_text_color", "profile_background_tile", "profile_background_color",
    "is_translator", "contributors_enabled", "profile_background_image_url",
    "profile_background_image_url_https", "profile_use_background_image", "profile_image_url",
    "profile_image_url_https", "translator_type", "protected", "profile_banner_url"
]
df_users = dfu[(dfu["friends_count"] > 5) & (dfu["default_profile_image"] == False)].drop(users_dlt, axis=1)
