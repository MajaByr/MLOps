import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"

    if not os.path.isfile(env_file):
        raise FileNotFoundError(f"Environment file not found: {env_file}")

    load_dotenv(env_file, override=True)


def export_secrets(secrets: str = "secrets.yaml") -> None:
    if not os.path.isfile(secrets):
        raise FileNotFoundError(f"Secrets file not found: {secrets}")

    with open(secrets, "r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file) or {}

    for key, value in secrets.items():
        if value is not None:
            os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("DUMMY_KEY: ", settings.DUMMY_KEY)
