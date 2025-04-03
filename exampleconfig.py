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
    STRING_SESSION = "1BJWap1sBuxgBXENph0jevvyZwuQZ2NTnJBIBg6pDO0g65BTB6XvNiMFkzlh9ZuYw0YiqTXk6W6LT3N8W0ya2VZu28tKmFPAKt5Syel1a3gkgxzbKciUBB4MGY4IWIOqxsMzSX7qRaeMAcJi_NMz8dHPt1kRkdx9gw-Oo1ugTUA1I_onZ_sRN4tMfyi_ia5iUMM9Gm4GRdLYtxmNLCAF2cZsMph2OL9Q4igP5F4z2_Sn8qYNcjo-dnhtWoCSSI_rZCLSjrb0Ue3z6kKQEEOesbJwLudTjiY4S_JMhAiJZi7y4mtH3sa-f1K4iuZ2euW724h0st-eqfuIYjGH-zHP-wbOXGnrHGnU="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7653315118:AAFeXKbMtax9EtvGelN5_I-4cOfRCgvtrgo"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."