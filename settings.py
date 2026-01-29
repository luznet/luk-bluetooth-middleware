from pydantic_settings import BaseSettings

class TreadmillSettings(BaseSettings):
    mac: str
    char_uuid: str

    model_config = {
        "env_prefix": "TREADMILL_",
        "case_sensitive": False
    }

