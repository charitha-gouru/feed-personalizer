from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_version_check():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["model_version"] == "1.0.0"

def test_rank_feed():
    payload = {
  "user_id": "stu_9999",
  "posts": [
    {
      "post_id": "p1",
      "author_id": "stu_1010",
      "tags": ["ai"],
      "content_type": "text",
      "karma": 90,
      "created_at": "2025-05-27T07:30:00Z"
    },
    {
      "post_id": "p2",
      "author_id": "stu_2020",
      "tags": ["ml"],
      "content_type": "image",
      "karma": 80,
      "created_at": "2025-05-27T14:00:00Z"
    },
    {
      "post_id": "p3",
      "author_id": "stu_1010",
      "tags": ["coding"],
      "content_type": "text",
      "karma": 5,
      "created_at": "2025-05-27T21:00:00Z"
    },
    {
      "post_id": "p4",
      "author_id": "stu_2020",
      "tags": ["events"],
      "content_type": "video",
      "karma": 95,
      "created_at": "2025-05-27T21:30:00Z"
    },
    {
      "post_id": "p5",
      "author_id": "stu_3030",
      "tags": ["fest"],
      "content_type": "text",
      "karma": 2,
      "created_at": "2025-05-27T15:00:00Z"
    },
    {
      "post_id": "p6",
      "author_id": "stu_4040",
      "tags": ["python"],
      "content_type": "image",
      "karma": 85,
      "created_at": "2025-05-27T08:30:00Z"
    },
    {
      "post_id": "p7",
      "author_id": "stu_4041",
      "tags": ["ml"],
      "content_type": "text",
      "karma": 1,
      "created_at": "2025-05-27T12:00:00Z"
    },
    {
      "post_id": "p8",
      "author_id": "stu_5050",
      "tags": ["travel"],
      "content_type": "text",
      "karma": 90,
      "created_at": "2025-05-27T20:30:00Z"
    },
    {
      "post_id": "p9",
      "author_id": "stu_5051",
      "tags": ["food"],
      "content_type": "image",
      "karma": 3,
      "created_at": "2025-05-27T13:30:00Z"
    },
    {
      "post_id": "p10",
      "author_id": "stu_6060",
      "tags": ["sports"],
      "content_type": "video",
      "karma": 15,
      "created_at": "2025-05-27T18:00:00Z"
    },
    {
      "post_id": "p11",
      "author_id": "stu_1010",
      "tags": ["coding"],
      "content_type": "image",
      "karma": 50,
      "created_at": "2025-05-27T20:00:00Z"
    },
    {
      "post_id": "p12",
      "author_id": "stu_2020",
      "tags": ["python"],
      "content_type": "text",
      "karma": 75,
      "created_at": "2025-05-27T07:15:00Z"
    },
    {
      "post_id": "p13",
      "author_id": "stu_4040",
      "tags": ["python"],
      "content_type": "text",
      "karma": 25,
      "created_at": "2025-05-27T22:15:00Z"
    },
    {
      "post_id": "p14",
      "author_id": "stu_2020",
      "tags": ["ds"],
      "content_type": "image",
      "karma": 70,
      "created_at": "2025-05-27T08:00:00Z"
    },
    {
      "post_id": "p15",
      "author_id": "stu_5050",
      "tags": ["coding"],
      "content_type": "video",
      "karma": 65,
      "created_at": "2025-05-27T10:00:00Z"
    },
    {
      "post_id": "p16",
      "author_id": "stu_2020",
      "tags": ["random"],
      "content_type": "text",
      "karma": 60,
      "created_at": "2025-05-27T06:00:00Z"
    },
    {
      "post_id": "p17",
      "author_id": "stu_1010",
      "tags": ["ai"],
      "content_type": "text",
      "karma": 95,
      "created_at": "2025-05-27T21:15:00Z"
    },
    {
      "post_id": "p18",
      "author_id": "stu_1010",
      "tags": ["ai"],
      "content_type": "image",
      "karma": 10,
      "created_at": "2025-05-27T10:30:00Z"
    },
    {
      "post_id": "p19",
      "author_id": "stu_3030",
      "tags": ["python"],
      "content_type": "video",
      "karma": 80,
      "created_at": "2025-05-27T23:00:00Z"
    },
    {
      "post_id": "p20",
      "author_id": "stu_4041",
      "tags": ["ml"],
      "content_type": "text",
      "karma": 0,
      "created_at": "2025-05-27T05:00:00Z"
    },
    {
      "post_id": "p21",
      "author_id": "stu_6060",
      "tags": ["ml"],
      "content_type": "image",
      "karma": 45,
      "created_at": "2025-05-27T20:30:00Z"
    },
    {
      "post_id": "p22",
      "author_id": "stu_2020",
      "tags": ["fest"],
      "content_type": "text",
      "karma": 15,
      "created_at": "2025-05-27T07:00:00Z"
    },
    {
      "post_id": "p23",
      "author_id": "stu_7070",
      "tags": ["coding"],
      "content_type": "text",
      "karma": 70,
      "created_at": "2025-05-27T21:45:00Z"
    },
    {
      "post_id": "p24",
      "author_id": "stu_8080",
      "tags": ["python"],
      "content_type": "image",
      "karma": 30,
      "created_at": "2025-05-27T10:00:00Z"
    },
    {
      "post_id": "p25",
      "author_id": "stu_1010",
      "tags": ["ai"],
      "content_type": "video",
      "karma": 100,
      "created_at": "2025-05-27T08:00:00Z"
    },
    {
      "post_id": "p26",
      "author_id": "stu_2020",
      "tags": ["travel"],
      "content_type": "image",
      "karma": 50,
      "created_at": "2025-05-27T08:00:00Z"
    },
    {
      "post_id": "p27",
      "author_id": "stu_3030",
      "tags": ["startups"],
      "content_type": "text",
      "karma": 80,
      "created_at": "2025-05-27T23:30:00Z"
    },
    {
      "post_id": "p28",
      "author_id": "stu_4040",
      "tags": ["python"],
      "content_type": "video",
      "karma": 85,
      "created_at": "2025-05-27T09:30:00Z"
    },
    {
      "post_id": "p29",
      "author_id": "stu_5050",
      "tags": ["ai"],
      "content_type": "text",
      "karma": 90,
      "created_at": "2025-05-27T07:45:00Z"
    },
    {
      "post_id": "p30",
      "author_id": "stu_6060",
      "tags": ["food"],
      "content_type": "text",
      "karma": 20,
      "created_at": "2025-05-27T19:00:00Z"
    },
    {
      "post_id": "p31",
      "author_id": "stu_1025",
      "tags": ["ai", "projects"],
      "content_type": "text",
      "karma": 65,
      "created_at": "2025-06-01T10:30:00Z"
    }
  ],
  "user_profile": {
    "branches_of_interest": ["AI", "DS"],
    "tags_followed": ["coding", "python", "ai", "ml"],
    "buddies": ["stu_1010", "stu_2020", "stu_3030"],
    "active_hours": ["07:00-09:00", "20:00-23:00"]
  }
}

    response = client.post("/rank-feed", json=payload)
    assert response.status_code == 200
    result = response.json()

    assert result["status"] == "ranked"
    assert result["user_id"] == payload["user_id"]
    assert len(result["ranked_posts"]) == len(payload["posts"])
    assert result["ranked_posts"][0]["score"] >= result["ranked_posts"][1]["score"]
