from pyrogram import Client 
from config.config import getdata
from base.new_post import is_new
import aiocron


api_id, api_hash, bot_token, channel_id = getdata()


bot = Client(
    name='config/apibot',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@aiocron.crontab('*/15 * * * *')
async def work():
    await is_new(bot,channel_id)


if  __name__ == '__main__':
    work.start()
    bot.run()