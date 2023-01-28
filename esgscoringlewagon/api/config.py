from pydantic import BaseSettings

class AppConfig(BaseSettings):
    api_url: str
    api_port : int
    interface_url : str
    interface_port : int
    dataset_path : str
    db_path : str
    db_name : str
    db_extension : str
    class Config:
        env_file = ".env"
        