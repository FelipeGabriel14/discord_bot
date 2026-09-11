import discord
import math
import os
from discord.ext import commands
from dotenv import load_dotenv
#Recebendo o Token !
load_dotenv()
token = os.getenv("TOKEN")
#funções
def adicao(num1,num2):
    return num1 + num2
def subtracao(num1,num2):
    return num1 - num2
def multiplicar(num1,num2):
    return num1 * num2
def raiz(num):
    return math.sqrt(num)
def divisao(num1, num2):
    return num1 / num2
#Bot
permissoes = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=permissoes)

@bot.command()
async def cal(ctx:commands.Context, num1:float,operador, num2:float):
    user = ctx.author.display_name
    match operador:
        case "+":
            res = adicao(num1,num2)
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            if res.is_integer():
                res = int(res)
            await ctx.reply(f"{user} a soma de {num1} + {num2} é {res}")
        case "-":
            res = subtracao(num1,num2)
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            if res.is_integer():
                res = int(res)
            await ctx.reply(f"{user} a subtração de {num1} - {num2} é {res}")
        case "*":
            res = multiplicar(num1,num2)
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            if res.is_integer():
                res = int(res)
            await ctx.reply(f"{user} a Multiplicação de {num1} * {num2} é {res}")
        case "/":
            if num1 == 0 or num2 == 0:
                await ctx.reply(f"{user} não posso dividir por Zero, Beta")
                return 
            
                
            await ctx.reply(f"{user} a divisão de {num1} + {num2} é {divisao(num1,num2)}")
@bot.command()
async def cal2(ctx:commands.Context,op:str,num:float):
 user = ctx.author.display_name   
 match op:
    case "raiz":
     res = round(raiz(num), 3)
     if res.is_integer():
      res = int(res)
     if num.is_integer():
      num = int(num)
     await ctx.reply(f"{user} a raiz de {num} é {res}")
@bot.event
async def on_ready():
    print("Estou rodando My Lord !")

# Iniciando Bot !
bot.run(token)