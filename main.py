# main program
import os
import json
import pandas as pd
import numpy as np
from test import clean_main
from test import df_to_formatted_json

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

directory = os.fsencode(r"/work/data")


def output(df):
    date = df['created_at']
    with open(f"{date.min()[4:10]}{date.min()[-5:]}-{date.max()[4:10]}{date.max()[-5:]}.json", 'w') as outfile:
        json.dump(df_to_formatted_json(clean_main(df)), outfile)


def main(directory):
    dfx = pd.DataFrame([])
    tweetlist = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            with open('/work/data/{}'.format(filename)) as f:
                for line in f:
                    if "\"text\":\"RT " in line:
                        continue
                    elif 'Exceeded connection limit for user' in line:
                        continue
                    else:
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
            continue

        else:
            continue

    dfx = dfx.append(pd.DataFrame(tweetlist))
    output(dfx)


    return None


if __name__ == "__main__":
    main()

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
