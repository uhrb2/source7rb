from .utils.extdl import install_pip

try:
    import randomstuff
except ModuleNotFoundError:
    install_pip("randomstuff.py")
    import randomstuff

from ..Config import Config
import asyncio

def get_rs_client():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return randomstuff.AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")

rs_client = get_rs_client()