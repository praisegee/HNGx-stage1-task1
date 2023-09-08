import os
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, Request

# instantiate fastapi
app = FastAPI()


# handle request
@app.get("/api")
def index(request: Request):
    today = datetime.now(timezone.utc)

    # response body
    data = {
        "slack_name": request.query_params.get("slack_name", ""),
        "current_day": today.strftime("%A"),
        "utc_time": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": request.query_params.get("track", ""),
        "github_file_url": "https://github.com/praisegee/HNGx-stage1-task1/blob/main/main.py",
        "github_repo_url": "https://github.com/praisegee/HNGx-stage1-task1",
        "status_code": 200,
    }

    return data


# run app
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=os.getenv("PORT", default=5000),
        log_level="info",
    )
