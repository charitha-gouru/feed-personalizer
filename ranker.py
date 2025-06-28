import joblib
import json
from features import extract_features

with open('config.json') as f:
    config = json.load(f)

model = joblib.load(config['model_path'])

def score_and_rank(posts, user_profile):
    features = extract_features(posts, user_profile)
    scores = model.predict(features)
    ranked = []
    for i, post in enumerate(posts):
        tie_breaker = ((hash(post.post_id) % 10000) / 10000.0) * 0.0001  # small tiebreaker
        ranked.append({
            "post_id": post.post_id,
            "score": float(scores[i]+tie_breaker) # Rounded for clean output
        })

    return sorted(ranked, key=lambda x: x["score"], reverse=True)
