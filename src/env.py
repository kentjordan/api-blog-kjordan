from dotenv import load_dotenv


def init_env():
    load_dotenv('.env.secret')
    load_dotenv('.env.shared')


init_env()
