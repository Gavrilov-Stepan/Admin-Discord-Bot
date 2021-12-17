import discord
from discord.ext import commands
from discord.utils import get

bot_Mod = commands.Bot(command_prefix='+')

@bot_Mod.event
async def Mod_ready():
    print(f'Бот {bot_Mod.user.name} активирован!Чтобы получить доступ к списку комманд, напишите +MimistCommands')
    print('Чтобы получить доступ к списку комманд, напишите +MimistCommands')
    print(f'Токен бота: {bot_token}')