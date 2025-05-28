from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "24347380"
    API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
    # the name to display in your alive message
    ALIVE_NAME = "FO"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://jokir20:jokir20@localhost:5432/jokir20"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1AZWarzIAUKfUulQzQjAnR_K1yNcfujowVpUi21alxnyFcAKwGk4_tLAStFNOru2t4nAL-YlsT9WRkxxgOds2x8ohyxHs3ypCqDQQ8hcKnQtJDA3YaUuRMPkaXXvS8BesQrk_ihvOqrAdIiDgPACbvp8ICSgkAgFdGNLQZiBirXM9mKS5PB8f26UmwVNbK7RzUGvck_2MHUqmsg8x9TSuqQalMhL1g6fL08WxJtWANCAH0B97SL1wbvEbD-jzZ4SX_wmUh_xrLe0uKTB50kEIrXslCD3z1Tzhnz1uvWQ9n3n1roH__x5dg-ujZvGU8ERQ8Pd5EQhRH2N89JSvNiWTUSw_jh1D0G8="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "8104058835:AAF9USA2bhHkzSgTC0VYx9qTzRquiGxa93E"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
