from loguru import logger

from pydantic import BaseModel, Field  # noqa
from pydantic_settings import BaseSettings


class LoadEnvFile(BaseSettings):
    model_config = {
        'env_file': '.env',
        'extra': 'allow',
        'env_file_encoding': 'utf-8',
    }


class Config(BaseModel):
    mysql: Mysql = None
    jwt: JWT = None
    redis: Redis = None

    def model_post_init(self, __context):
        load_env_file = LoadEnvFile()  # noqa
        # self.mysql = Mysql(**load_env_file.model_dump())
        # self.jwt = JWT(**load_env_file.model_dump())
        # self.redis = Redis(**load_env_file.model_dump())


# singleton leitura unica do .env
config = Config()


logger.add(
    'logs/app.log',
    # level='WARNING', # -> trigger event LEVEL for register.
    rotation='2 MB',
    compression='zip',
    retention='1 week',
    format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message} | {file} | {function} | {line}',
)


if __name__ == '__main__':
    logger.info('Config loaded')
    logger.info(f'Config: {config}')
