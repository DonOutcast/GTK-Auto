import os
import logging


def os_getenv(key: str, default=None) -> str:
    """
    Get an enviroment variable, return None if it doesn't exist or empty.

    The optional second argument can specify an alternate default key, and the result ar str.

    :param key:
    :param default:
    :return:
    """
    env_value = os.getenv(key)
    if env_value is None:
        logging.warning(
            f"ENV variable: {key} is set to empty string. Using default value instead ({default})"
        )
        env_value = default
    return env_value
