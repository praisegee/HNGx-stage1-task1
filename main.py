import json
import os
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, Request

# instantiate fastapi
app = FastAPI()


# handle request
@app.get("/")
def index(request: Request):
    # get params from the incoming request
    slack_name = request.query_params.get("slack_name", "")
    track = request.query_params.get("track", "")
    today = datetime(timezone.utc)

    print(type(request.query_params))
    return {"name": "PraiseGod"}


# run app
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=os.getenv("PORT", default=5000),
        log_level="info",
    )
