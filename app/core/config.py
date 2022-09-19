from starlette.config import Config

config = Config(".env_dev")

DATABASE_URL = "postgresql://root:root@localhost:32700/price_analysis"