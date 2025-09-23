from fastapi import FastAPI

from api.routes.pipeline import router as pipeline_router


app = FastAPI(title="Topic-to-Video Pipeline API")


app.include_router(pipeline_router, prefix="/api")

