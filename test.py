import os

counter = 300

total_files = len([name for name in os.listdir('D:\data')])
progress = (counter / total_files) * 100

print(f"{round(progress, 2)}%")


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
