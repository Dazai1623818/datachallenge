# main program
import os
import json
import pandas as pd
import numpy as np
from pathlib import Path

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

directory = os.fsencode(r"C:/Users/thepi/OneDrive - TU Eindhoven/Quartile 4/JBG030 Data challenge/test")



def clean(directory):
    os.mkdir("cleaned data")
    dfx = pd.DataFrame([])
    tweetlist = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            with open('{}/{}'.format(directory.decode("utf-8") , filename)) as f:
                print(filename)
                for line in f:
                    if "\"text\":\"RT " in line:
                        continue
                    else:
                        if is_json(line):
                            tweetDict = json.loads(line)
                            if 'delete' in tweetDict.keys():
                                continue
                            else:
                                tweetlist.append(tweetDict)
                                if len(tweetlist) >= 20000:
                                    dfx = dfx.append(pd.DataFrame(tweetlist))
                                    output(dfx)
                                    tweetlist = []
                                    tweetDict = {}
                                    dfx = pd.DataFrame([])
            counter = 0
            continue

        else:
            continue

    dfx = dfx.append(pd.DataFrame(tweetlist))
    output(dfx)

    return None

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True


def output(df):
    date = df['created_at']
    name = f"{date.min()[4:10]}{date.min()[-5:]}-{date.max()[4:10]}{date.max()[-5:]}.json"
    base = Path('Cleaned data')
    jsonpath = base / (f"{date.min()[4:10]}{date.min()[-5:]}-{date.max()[4:10]}{date.max()[-5:]}.json")
    base.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(df_to_formatted_json(clean_main(df))))

    return None


# As docstring says, function is an inverse of pd.json_normalize, converts dataframe to json.
def df_to_formatted_json(df, sep="."):
    """
    The opposite of json_normalize
    """
    result = []
    for idx, row in df.iterrows():
        parsed_row = {}
        for col_label, v in row.items():
            keys = col_label.split(".")

            current = parsed_row
            for i, k in enumerate(keys):
                if i == len(keys) - 1:
                    current[k] = v
                else:
                    if k not in current.keys():
                        current[k] = {}
                    current = current[k]
        # save
        result.append(parsed_row)
    return result


def clean_main(df):
    """"
    Cleans dfx removing unnecessary columns
    """
    df_delete = [
        "geo", "display_text_range", "coordinates",
        "timestamp_ms", "contributors",
        "quote_count", "reply_count", "retweet_count", "favorite_count",
        "filter_level", "quoted_status_permalink", "place",
        "favorited", "retweeted", "possibly_sensitive", "source", "truncated"
    ]

    df.drop(df_delete, axis='columns', inplace=True)

    return df


def clean_users(df):
    """
    Cleans df_users removing unnecessary columns
    """
    users_delete = [
        'url', "notifications", "follow_request_sent", "following", "lang",
        "time_zone", "utc_offset", "default_profile", "default_profile_image",
        "profile_link_color", "profile_sidebar_border_color", "profile_sidebar_fill_color",
        "profile_text_color", "profile_background_tile", "profile_background_color",
        "is_translator", "contributors_enabled", "profile_background_image_url",
        "profile_background_image_url_https", "profile_use_background_image", "profile_image_url",
        "profile_image_url_https", "translator_type", "protected", "profile_banner_url"
    ]

    df.drop(users_delete, axis=1, inplace=True)

    return df



clean(directory)


# Convert
#dfx['created_at'] = pd.to_datetime(dfx['created_at'])
#dfx.set_index(["created_at"], inplace=True)

#dfx["Month"] = dfx.index.month.fillna(0.0).astype(int)
#dfx["Day"] = dfx.index.day.fillna(0.0).astype(int)
#dfx["DayOfYear"] = dfx.index.dayofyear.fillna(0.0).astype(int)
#dfx["Year"] = dfx.index.year.fillna(0.0).astype(int)


# delete: Attributes to be deleted
#dfu = pd.json_normalize(dfx["user"].values)
#df_users = dfu[(dfu["friends_count"] > 5) & (dfu["default_profile_image"] == False)]
