from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = True 
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list[str] = ["http://localhost:5173", 
                               "http://localhost:3000",
                               "http://127.0.0.1:5173",
                                "http://127.0.0.1:3000"
                               ]
    static_files_dir: str = "static"
    image_upload_dir: str = "static/images"
    class Config:
        env_file = ".env"
        
settings = Settings()