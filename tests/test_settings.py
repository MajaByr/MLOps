import os
import yaml
from dotenv import load_dotenv
from settings import Settings


def test_settings():

    env_file = "config/.env.test"
    secrets = "tests/secrets.yaml"

    if not os.path.isfile(env_file):
        raise FileNotFoundError(f"Environment file not found: {env_file}")

    load_dotenv(env_file, override=True)

    if not os.path.isfile(secrets):
        raise FileNotFoundError(f"Secrets file not found: {secrets}")

    with open(secrets, "r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file) or {}

    for key, value in secrets.items():
        if value is not None:
            os.environ[key] = str(value)

    settings = Settings()

    assert settings.APP_NAME == "TestApp"
    assert settings.ENVIRONMENT == "test"
    assert settings.DUMMY_KEY == "test_key"
