from environs import Env

env = Env()
env.read_env()
login = env('DB_LOGIN')
password = env('DB_PASSWORD')
db_name = env('DB_NAME')
