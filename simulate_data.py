import csv
import random

random.seed(42)

with open("training_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "post_karma", "user_follows_tag", "is_buddy_post", "time_match_score",
        "content_type_text", "content_type_image", "author_branch_similarity", "karma_squared", "noise", "tag_overlap_count", "post_id_noise", "label"
    ])

    for _ in range(1000):
        karma = random.randint(0, 100)+random.uniform(-0.5,0.5)
        karma=max(0,min(100,karma))
        karma_normalized = karma / 100.0
        follows_tag = random.choices([0, 1],weights=[0.3,0.7])[0]
        is_buddy = random.choices([0, 1],weights=[0.4,0.6])[0]
        time_score = round(random.uniform(0, 1), 2)
        content_type = random.choice(["text", "image","video"])
        content_type_text = 1 if content_type == "text" else 0
        content_type_image = 1 if content_type == "image" else 0
        author_branch_sim = random.choices([0, 1],weights=[0.5,0.5])[0]
        karma_squared = (karma / 100) ** 2
        tag_overlap_count = random.randint(0, 5)+random.uniform(0,0.5)
        noise = random.gauss(0, 0.005)
        post_id_noise = random.uniform(0, 0.0001)

        # Manual deterministic label
        label = (
            0.01 * karma +
            0.3 * follows_tag +
            0.25 * is_buddy +
            0.2 * time_score +
            0.15 * author_branch_sim +
            0.02 * tag_overlap_count +
            0.03 * karma_squared +
            noise
            #random.uniform(0, 0.005)
        )
        label += random.gauss(0, 0.005)  # subtle randomness
        label = min(1.0, max(0.0, label))
        noise = random.uniform(0, 0.001)

        writer.writerow([
            karma, follows_tag, is_buddy, time_score,
            content_type_text, content_type_image, author_branch_sim, karma_squared, tag_overlap_count, noise, post_id_noise, label
        ])
