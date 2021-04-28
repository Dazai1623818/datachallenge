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
                        print('test')
                        continue
                    else:
                        tweetlist.append(tweetDict)

            dfx = dfx.append(pd.DataFrame(tweetlist))

            progress = (counter / total_files) * 100
            print(f"{round(progress, 2)}%")
        continue


    else:
        continue

print(len(tweetlist))
