from loguru import logger

from pydantic import BaseModel, Field  # noqa
from pydantic_settings import BaseSettings


def _clean(v):
    if not isinstance(v, str):
        return v
    s = v.strip()
    if s.startswith("\\'") and s.endswith("\\'"):
        s = s[2:-2]
    elif s.startswith("'") and s.endswith("'"):
        s = s[1:-1]
    elif s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s

class LoadEnvFile(BaseSettings):
    model_config = {
        #'env_file': '.env',
        #'extra': 'allow',
        'env_file_encoding': 'utf-8',
    }
class Config(BaseModel):
    _config_model_variable: BaseModel = None

    def model_post_init(self, __context):
        import os, json

        if os.getenv('APP_CONFIG'):
            # carrega a env lendo como json
            json_config = json.loads(os.getenv('APP_CONFIG'))
            env_dict = {k.lower(): _clean(v) for k, v in json_config.items()}
        else:
            env_dict = {k.lower(): _clean(v) for k, v in os.environ.items()}


# singleton leitura unica do .env
config = Config()


logger.add(
    #'logs/app.log',
    # level='WARNING', # -> trigger event LEVEL for register.
    #rotation='2 MB',
    #compression='zip',
    #retention='1 week',
    format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message} | {file} | {function} | {line}',
)


if __name__ == '__main__':
    logger.info('Config loaded')
    logger.info(f'Config: {config}')
