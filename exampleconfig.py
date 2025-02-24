from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "24347380"
    API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
    # the name to display in your alive message
    ALIVE_NAME = os.getenv("USER")
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://jokeer55:jokeer55@localhost:5432/jokeer55"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu4305pLu-fiJ0fFG9dWcdP5ObpquvsyvIm1A5zjXAR6kzNilGhNCYD8acnftZRw4SUwKO0MC_MVM3xZXGPCDd3wqC92H7w9TS8vPrgszoyZz4z8XjYWBscZZjerny5U9NJrfyuZBK7VUzfQnCDElTB9ShAW9Wb_Wz4P6kwT8OvYaviYUbeJ21Qt4MNOrrzTuuJiaPhtOD2qSjKu17ScJdYgLd8Y30AG8BE6hwSb15EsA7om-oXPETt8rHwAj14oVc9gX0PX-HZb6tkpVnXsr15dUQerfWHUUVl9LmSlbyVR5gt9BhreB04dxIcIORh7FucNIjOncHSaGeCMTvvoLjeQ="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "6850120038:AAHvK0-MztbWVX9uwXHdAEruIZwWnsoeMKk"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
