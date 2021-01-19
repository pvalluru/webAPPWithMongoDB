import yaml

def getTokenExpairTime():
    default_TOKEN_EXPAIR_TIME = 15
    try:
        with open("Config/config.yml", "r") as ymlfile:
            cfgfile = yaml.load(ymlfile)
        return cfgfile['TOKEN_EXPAIR_TIME'] if cfgfile['TOKEN_EXPAIR_TIME'] else default_TOKEN_EXPAIR_TIME
    except Exception as e:
        print("Caught Exception using default fetch time.")
        return default_TOKEN_EXPAIR_TIME
