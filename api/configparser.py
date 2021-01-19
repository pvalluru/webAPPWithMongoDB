import yaml

def getTokenExpairTime():
    default_TOKEN_EXPIRY_TIME = 15
    try:
        with open("Config/config.yml", "r") as ymlfile:
            cfgfile = yaml.load(ymlfile)
        return cfgfile['TOKEN_EXPIRY_TIME'] if cfgfile['TOKEN_EXPIRY_TIME'] else default_TOKEN_EXPIRY_TIME
    except Exception as e:
        print("Caught Exception using default fetch time.")
        return default_TOKEN_EXPIRY_TIME
