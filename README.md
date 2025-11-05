# 📸 FastAPI Photo and Video Sharing Application

A simple and modern **photo & video sharing** platform built using **FastAPI**.
It allows users to **upload media**, **view a feed**, and **delete posts**, with async database handling and **ImageKit** integration for media storage.

---

## 🚀 Features

* 📤 Upload photos and videos
* 📰 View a feed of uploaded posts
* 🗑️ Delete posts by ID
* ⚡ Built with async FastAPI + SQLAlchemy

---

## 🛠️ Technologies Used

* **FastAPI** — backend framework
* **SQLAlchemy (Async)** — ORM for database interaction
* **ImageKit** — cloud media storage
* **SQLite** — local database (easily replaceable)
* **uv** — environment & dependency management

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/ShreyasGandhi0607/PhotoVideoSharingPlatform.git
   ```

2. **Change into the project directory**

   ```bash
   cd FastAPIPhotoVideoSharing
   ```

3. **Create a virtual environment**

   ```bash
   uv venv
   ```

4. **Activate the virtual environment**

   * On **Windows**:

     ```bash
     .venv\Scripts\activate
     ```
   * On **macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

5. **Install dependencies using pyproject.toml**

   ```bash
   uv sync
   ```

---

## ▶️ Running the Application

1. **Start the FastAPI app**

   ```bash
   uv run main.py
   ```

2. **Open your browser** and go to:
   👉 [http://localhost:8000/docs](http://localhost:8000/docs)
   to explore the interactive **Swagger API documentation**.

---

## 📡 API Endpoints

| Method   | Endpoint          | Description                                     |
| -------- | ----------------- | ----------------------------------------------- |
| `POST`   | `/upload/`        | Upload a photo or video (with optional caption) |
| `GET`    | `/feed`           | Retrieve all uploaded posts                     |
| `DELETE` | `/post/{post_id}` | Delete a post by its ID                         |

---

## 📁 Project Structure

```
├─ src/
│  ├─ __pycache__/           # Compiled Python files
│  ├─ app.py                 # FastAPI app initialization
│  ├─ db.py                  # Database connection & models
│  ├─ image.py               # ImageKit upload & handling logic
│  ├─ posts.json             # Local data storage (temporary)
│  ├─ schema.py              # Pydantic models for request/response
│  └─ users.py               # User-related functionality
│
├─ .env                      # Environment variables (API keys, DB URL)
├─ .gitignore                # Ignored files for Git
├─ .python-version           # Python version management
├─ frontend.py               # Optional frontend logic (CLI/UI helper)
├─ main.py                   # Entry point (if needed)
├─ pyproject.toml            # Project metadata & dependencies
├─ README.md                 # Project documentation
├─ test.db                   # SQLite database
└─ uv.lock                   # uv dependency lock file
```

---
