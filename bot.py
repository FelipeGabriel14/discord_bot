import discord
import os
from dotenv import load_dotenv
#Recebendo o Token !
load_dotenv()
token = os.getenv("TOKEN")


# Iniciando Bot !
bot.run(token)

