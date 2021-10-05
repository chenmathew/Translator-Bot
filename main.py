import os
import discord
from google_trans_new import google_translator  


my_secret = os.environ['secret']
translator = google_translator()

client = discord.Client()

#Change tgt to match language
def translate(message, tgt = 'zh-cn'):
	translated = translator.translate(message, lang_tgt=tgt)
	return translated

@client.event
async def on_ready():
    print('BOT IS ONLINE')

@client.event
async def on_message(message):
  if message.author == client.user:
	  return
  if message.content.startswith("!translate"):
	  translated = translate(message.content[11:])
	  auth = str(message.author)
	  msg = await message.channel.send(auth + ": " + translated)

client.run(my_secret)