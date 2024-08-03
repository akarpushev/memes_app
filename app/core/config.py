import os


class Settings:
    PROJECT_NAME: str = "Memes API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/memes_db")
    S3_ENDPOINT: str = os.getenv("S3_ENDPOINT", "http://minio:9000")
    S3_ACCESS_KEY: str = os.getenv("S3_ACCESS_KEY", "minio")
    S3_SECRET_KEY: str = os.getenv("S3_SECRET_KEY", "minio123")
    S3_BUCKET: str = os.getenv("S3_BUCKET", "memes")


settings = Settings()
