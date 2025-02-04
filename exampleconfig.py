from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "24347380"
    API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
    # the name to display in your alive message
    ALIVE_NAME = "MyrOn"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://jokeer40:jokeer40@localhost:5432/jokeer40"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBuywECXZqYxqEvhDuGJ35Zwxdawq8-MYHvKm5YWhc4RhPwXAsWkQSZexrnMkhWcj2TIiC4FGSiyFU_M-RlDRxfsNO0C-nIPUktMdbB3-kXu9mQzcgNxz7IlectuWvAI0X-QaiJEp4fAH59z8_gipWRtkLr9sWpOGbbNOZ2PIEYEHlqf0Ci7v5r-uNfhPBV2h_5LajcksWx1yQRPb9WxDTWVwOfgPxOE28-2vQnIwddsKbgQLglIuMXothckHvtdq_BDdv41PtHtWSO5fI8ExVleVtYFTBHT2cW9ASGTkEI78LgQ3XfkHLqoHVb0TJRAwpx0rxnQWF6YfQfBBujPBb03o="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7321135092:AAFGB3tJfY0zBw4u2SSx8kZTsp7MKxFyJpQ"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
