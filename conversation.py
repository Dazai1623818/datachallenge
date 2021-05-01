def get_convo(tweetlist):
    counter = 0
    tweet_id = []
    layers = []
    count = {}

    for tweet in reversed(tweetlist):
        if tweet['in_reply_to_status_id_str'] != None:
            layers.append([tweet['id'], tweet['text'], tweet['in_reply_to_status_id_str']])

    for tweet in reversed(tweetlist):
        for thread in layers:
            if tweet['id_str'] == thread[-1]:
                if tweet['in_reply_to_status_id_str'] == None:
                    thread.append(tweet['text'])
                else:
                    thread.append(tweet['text'])
                    thread.append(tweet['in_reply_to_status_id_str'])
                    if tweet['in_reply_to_status_id_str'] not in count.keys():
                        count[tweet['in_reply_to_status_id_str']] = 1
                    else:
                        count[tweet['in_reply_to_status_id_str']] += 1

    f = open(f"Conversations.txt", 'w', encoding="utf8")
    for thread in layers:
        f.write(f"{thread} '\n'")
    f.close()


get_convo(tweetlist)