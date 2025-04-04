from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "24347380"
    API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
    # the name to display in your alive message
    ALIVE_NAME = "سهَم"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://jokeer501:jokeer501@localhost:5432/jokeer501"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu6OZCl1sMuEwEI80KKBo0kw2msTnPzgZw7TjhpPAVXY9FcjR3OxJL55iHeYp67MzvwGWZTWD71GoagnN49_SGDim4M49Ittq6EgEC5jAH0EaeXVwfWnqHVgIqDd1WhE7ZCKihhJGTSyIUexM9H1T6eFNbsHtg5VM17i3y_LMfckBjM6j_Ff5Kb5r2-InS5akR668KuzKEesBW9ru6B7y6o_wFz8Ph80zpm20AjdgoS4OQtNNhYToluzfu2PlRPKdkMVyvydo6v5_sfKh_6hWASBXc07rI0FOtu1wEz0r8tsEE6WoyWSxWV0u5EP65FlPBtSYvHUrPAMp0j1uu8sbfwc="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7653315118:AAFeXKbMtax9EtvGelN5_I-4cOfRCgvtrgo"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."