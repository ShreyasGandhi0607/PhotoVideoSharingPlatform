## FastAPI Photo and Video Sharing Application
This is a simple photo and video sharing application built using FastAPI. It allows users to upload media files, view a feed of posts, and delete posts.
## Features
- Upload photos and videos
- View a feed of uploaded posts
- Delete posts by ID
## Technologies Used
- FastAPI
- SQLAlchemy (with Async support)
- ImageKit for media storage
- SQLite (or any other database supported by SQLAlchemy)
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ShreyasGandhi0607/PhotoVideoSharingPlatform.git
    ```
2. Change into the project directory:
    ```bash
    cd FastAPIPhotoVideoSharing
    ```
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Running the Application
1. Start the FastAPI application:
    ```bash
    uvicorn src.app:app --reload
    ```
2. Open your browser and navigate to `http://localhost:8000/docs` to access the API documentation.  
## API Endpoints
- `POST /upload/` : Upload a photo or video file with an optional caption.
- `GET /feed` : Retrieve a feed of all uploaded posts.
- `DELETE /post/{post_id}` : Delete a post by its ID.