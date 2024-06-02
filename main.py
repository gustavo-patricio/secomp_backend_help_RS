from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import endpoints, settings

app = FastAPI(title=settings.Settings().PROJECT_NAME)

origins = []

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(endpoints.user_router)
app.include_router(endpoints.login_router)
app.include_router(endpoints.collect_point_router)
app.include_router(endpoints.addres_router)
app.include_router(endpoints.donation_point_router)