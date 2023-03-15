from configparser import ConfigParser


def getdata():
    conf = ConfigParser()
    conf.read('config/config.ini')
    if ('api_id' and 'api_hash' and 'bot_token','channel_id') in conf["Data"]:
        data = conf['Data']
        return int(data['api_id']), data['api_hash'], data['bot_token'], data['channel_id']
    else:
        raise ValueError