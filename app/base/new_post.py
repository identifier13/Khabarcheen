from base.scarping_sites import *
import json


async def is_new(bot, channel):
    with open('db/db.json', 'r') as f:
        datadb = json.load(f)

    newdata = {
        '9to5linux' : nineto5linux(),
        'omglinux' : omg_linux(),
        'itsfoss' : itsfoss(),
        'omgubuntu' : omg_ubuntu()
    }
    
    for i in newdata.keys():
        if newdata[i][0] != datadb[i]['url_post']:
            await bot.send_photo(
                channel,
                newdata[i][-1],
                caption=f'[{newdata[i][1]}]({newdata[i][0]})\n\n@{channel}'
            )
            
            datadb[i]['url_post'] = newdata[i][0]
            datadb[i]['text'] = newdata[i][1]
            datadb[i]['image'] = newdata[i][-1]
    
    with open('db/db.json','w') as f:
        json.dump(datadb,f,indent=2)
    
            
            
