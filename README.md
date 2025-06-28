# 🧠 Feed Personalization Engine

A machine learning-based microservice that ranks student feed posts based on personalized interests, engagement patterns, and buddy network behavior — built entirely offline using **FastAPI** and **Docker**.

---

## ✨ What This Project Does

This engine takes a **student profile** and a list of **feed posts**, and returns the posts ranked by **how relevant** they are to that student. It mimics platforms like LinkedIn or Instagram but tailored for **college students**.

> ✅ No internet or cloud APIs needed — everything runs offline.

---

## 🔍 Why It Matters

Students are overwhelmed with irrelevant content. This project solves that by using an AI model to surface posts that match:

* Their followed topics (tags)
* Buddy network (friends’ posts)
* Preferred content type (text/image)
* Time of day they're active
* Post popularity (karma)

---

## ⚙️ How It Works

1. **Training phase (offline)**:

   * Simulates 1000+ realistic student-post interactions.
   * Trains a regression model (`RandomForestRegressor`) to predict a "relevance score" between 0 and 1.
2. **Serving phase (FastAPI)**:

   * Accepts new posts + user profile.
   * Extracts features, scores, sorts, and returns ranked results.

---

## 🚀 Key Features

* 🧠 AI model trained on 1000+ engagement samples
* 🎯 Guarantees uniqueness in scores via post_id noise
* ⚡ REST API built using FastAPI + Pydantic
* 🧪 Thorough unit testing with `pytest`
* 🐳 Dockerized and ready for offline deployment
* ✅ All components (model, data, APIs) are cloud-free
* ✅ JSON input/output, runs fully offline

---

## 🧪 API Endpoints

| Method | Endpoint     | Description                                  |
| ------ | ------------ | -------------------------------------------- |
| POST   | `/rank-feed` | Accepts posts + profile, returns ranked list |
| GET    | `/health`    | Health check                                 |
| GET    | `/version`   | Model version info                           |

---

## 🔧 Technologies Used

* **Python 3.11**
* **FastAPI** – API framework
* **Scikit-learn** – ML model
* **Pandas** – Data handling
* **NumPy**
* **Uvicorn** – ASGI server
* **Docker** – Packaging & offline deployment
* **Pytest** – Unit testing

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/feed-personalizer.git
cd feed-personalizer
```

### 2. Train the Model

```bash
python simulate_data.py
python train_model.py
```

### 3. Start the API (Locally)

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker

> Ensure Docker Desktop is running

### Build the Image

```bash
docker build -t feed-personalizer .
```

### Run the Container

```bash
docker run -p 8000:8000 feed-personalizer
```

---

## 🧪 How to Test

### Create and Activate Virtual Environment

```bash
python -m venv venv
# For Windows
.\venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Unit Tests

```bash
pytest test_main.py
```

### Sample Input Format

```json
{
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
```

---

## 📝 Project Highlights

* ✔️ Training data includes engineered uniqueness via `post_id_noise` and Gaussian noise
* ✔️ Model delivers near-perfect relevance consistency (R² ~0.97)
* ✔️ Ranking system avoids score collisions for better UX
* ✔️ Dockerized final build for offline portability

---

## 🎯 Use Cases

* Smart academic feeds for students
* Recommendation engines in learning platforms
* Peer-aware content suggestion models

---

## 📌 Final Notes

This project meets all constraints:

* ✅ Runs fully offline
* ✅ Response time < 2s for 20 posts
* ✅ Inputs/outputs strictly in JSON
* ✅ Dockerized for plug-and-play deployment

## 🧑‍💻 Author
Gouru Charitha - B.Tech Final Year CSE Student at SR University - Intern @Turtil
I built this project as part of my TURTIL Internship Program.
Passionate about machine learning, APIs, and scalable systems.

## 📜 Ownership Note
This project is fully developed by Gouru Charitha for educational and internship purposes.
Reuse of the codebase is permitted with proper credit.
