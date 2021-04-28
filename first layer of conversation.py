counter = 0
tweet_id = []
layers = []

for tweet in reversed(tweetlist):
    counter -= 1
    for thread in reversed(layers):
        if tweet['id_str'] == thread[2]:
            if tweet['in_reply_to_status_id_str'] == None:
                thread.append(tweet['text'])
                print(f'Tweet:{thread[3]}\nReply:{thread[0]}\n')
                layers.remove(thread)
            #                 for i in thread:
            #                     print(i)
            #                 print('\n\n')
            #                 print(f"{tweet['text']}\n{tweet['id']}\n{thread[0]}\n{thread[1]}\n\n")
            else:
                #                 thread.append(tweet['text'])
                thread.append(tweet['in_reply_to_status_id_str'])
                thread.append(tweet['text'])
    #                 print(tweet['text'], tweet['id'])
    if tweet['in_reply_to_status_id_str'] == None:
        continue
    else:
        layers.append([tweet['text'], tweet['id'], tweet['in_reply_to_status_id_str']])
