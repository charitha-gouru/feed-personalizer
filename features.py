import pandas as pd
import json
from datetime import datetime
import random

with open('config.json') as f:
    config = json.load(f)

def time_match_score(post_time, active_hours):
    post_hour = datetime.fromisoformat(post_time.replace("Z", "+00:00")).hour
    for window in active_hours:
        start, end = window.split("-")
        if int(start.split(":")[0]) <= post_hour <= int(end.split(":")[0]):
            return 1.0
    return 0.0

def extract_features(posts, user_profile):
    rows = []
    for post in posts:
        tag_overlap_count = sum(tag in user_profile.tags_followed for tag in post.tags)
        row = {
            "user_follows_tag": any(tag in user_profile.tags_followed for tag in post.tags),
            "is_buddy_post": post.author_id in user_profile.buddies,
            "post_karma": post.karma,
            "karma_squared": (post.karma/100)**2,
            "content_type_text": 1 if post.content_type == "text" else 0,
            "content_type_image": 1 if post.content_type == "image" else 0,
            "time_match_score": time_match_score(post.created_at, user_profile.active_hours),
            "author_branch_similarity": 0,
            "tag_overlap_count": tag_overlap_count,
            "noise": 0.0,
            "post_id_noise": ((hash(post.post_id) % 10000) / 10000.0)
            
        }
        row["noise"] = random.uniform(0, 0.00001)
        rows.append(row)

    df = pd.DataFrame(rows)

    for feature in config['features']:
        if feature not in df.columns:
            df[feature] = 0

    return df[config['features']]
