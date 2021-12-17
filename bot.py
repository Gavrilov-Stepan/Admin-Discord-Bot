import discord
from discord.ext import commands
import os
import random
import time
import config
import asyncio
from random import randint

from main import clear
from main import BW
from main import bot_commands
from main import addBW
from main import clearBW
from main import on_message
from main import createCh
from main import deleteCh
from main import kick

from gamesms import guess_game
from gamesms import rps
from gamesms import rusgame

from BOt_role_up import on_command_error
from BOt_role_up import on_ready
from BOt_role_up import choose
from BOt_role_up import roll
from BOt_role_up import del_role
from BOt_role_up import create_role
from BOt_role_up import give_role
from BOt_role_up import remove_role
from BOt_role_up import mute

bot_Mess = commands.Bot(commands_prefix = '+') #префиксом команд бота будет +
bot_Mess.remove_command('help') #удаление команды help
TOKEN = open('token.txt', 'r') #в переменную TOKEN записывается берущийся из файла token.txt токен бота
bot_Mess.run(TOKEN) #запускается бот
