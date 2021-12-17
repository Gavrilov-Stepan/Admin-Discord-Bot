import discord   # Импортируем библиотеку discord.py
from discord.ext import commands   # Импортируем из discord.ext функцию commands
import os   # Импортируем библиотеку для работы с txt файлами
import asyncio   # Импортируем библиотеку для упрощения использования корутин и футур в асинхронном коде
from random import randint
client = discord.Client()   # Используем функции бибдиотеки discord

client = commands.Bot(command_prefix=('+'))   # Задаем функции client префикс, которым мы будем вызывать команды ии фунции бота.

@client.event   # Запускаем функцию бота в "фоновом" режиме.
async def on_ready():   # Вызываем асинхронную функцию по выводу включения бота.
    print("Bot is ready")   # Выводит, что бот готов и запущен.
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Python"))   # Данная строка

@client.event
async def on_command_error(ctx, error):
    author = ctx.message.author
    await ctx.send(f'{author.name}, sorry, but this command does not exist.')
    print(f'find {error}')

@client.command()
async def choose(ctx, *words):
    i = randint(0,len(words)-1)
    print(words)
    await ctx.send(f'How about this - {words[i]}? From this List{words}')
    await ctx.message.delete()

@client.command()
async def roll(ctx):
    author = ctx.message.author
    Roll = randint(1,100)
    await ctx.send(f'{author.name} Roll: {Roll}')
    await ctx.message.delete()

@client.command()   # Задаем значение функции по команде. Будет выполнятся только если ввести префикс с названием функции.
@commands.has_permissions()
async def del_role(ctx):   # Вызываем асинхронную функцию по удалении роли.   # РАБОТАЕТ+++++++++++++++++++++++++++++++++++++++++++++
    ROLES = []
    try:
        Roles = open('roles.txt', 'r')
    except FileNotFoundError:
        pass
    gg = (ctx.message.content).split(' ')
    for word in Roles:
        if word.strip() != gg[1]:
            ROLES.append(word.strip())
    Roles.close()

    Roles = open('roles.txt', 'w')
    if ROLES != []:
        Roles.write(ROLES[0])
    if len(ROLES) > 1:
        for i in range(1,len(ROLES)):
            Roles.write('\n' + ROLES[i])
    print('Del')

    await ctx.message.delete()

@client.command()   # Задаем значение функции по команде. Будет выполнятся только если ввести префикс с названием функции.
async def create_role(ctx):   # Вызываем асинхронную функцию по создании роли.

        try:   # Будет выполнятся если не None.
            gg = (ctx.message.content).split()   # В переменную записывааем все наше сообщение разделяя про пробелам. Получаем на выходе массив.
            guild = ctx.guild   # Записываем в переменную guild id нашего discord сервера.
            color = int((gg[2][2:]), 16)   # Находит значение
            role = await guild.create_role(name=str(gg[1]), permissions=discord.Permissions(0), colour=discord.Colour(color))
            authour = ctx.message.author
            await authour.add_roles(role)

            try:
                roles = open('roles.txt', 'a')
            except FileNotFoundError:
                roles = open('roles.txt', 'w')
            if os.stat("roles.txt").st_size > 0:
                print(str(gg[1]))
                roles.write('\n' + str(gg[1]))  # добавляет их с новой строки в файл
            else:  # выполняется, если файл с запретными словами пустой, что выполняется, если он был либо только что создан, либо очищен при помощи команды +clearBW
                pass

            await ctx.message.delete()
        except:
            print("Something went wrong")

@client.command()
async def give_role(ctx):

    ROLES = []
    try:
        Roles = open('roles.txt', 'r')
    except FileNotFoundError:
        Roles = open('roles.txt', 'w')
        Roles.close()
        Roles = open('roles.txt', 'r')
    for word in Roles:
        ROLES.append(word.strip())

    for i in range(len(ROLES)):
        if ROLES[i] in ctx.message.content:
                member = ctx.message.author
                role = discord.utils.get(ctx.message.guild.roles, name= ROLES[i])
                await member.add_roles(role)
                await ctx.message.delete()

@client.command()
async def remove_role(ctx):

        ROLES = []
        try:
            Roles = open('roles.txt', 'r')
        except FileNotFoundError:
            Roles = open('roles.txt', 'w')
            Roles.close()
            Roles = open('roles.txt', 'r')
        for word in Roles:
            ROLES.append(word.strip())

        for i in range(len(ROLES)):
            if ROLES[i] in ctx.message.content:
                member = ctx.message.author
                role = discord.utils.get(ctx.message.guild.roles, name= ROLES[i])
                await member.remove_roles(role)
                await ctx.message.delete()

@client.command()
@commands.has_permissions()
async def mute(ctx, user: discord.Member, *, reason=None):
    await asyncio.sleep(1)
    banned_role = discord.utils.get(user.guild.roles, name="[Mute]")
    await user.edit(roles=[]) # Remove all roles
    await user.add_roles(banned_role, reason=None) # Assign the new role
    await ctx.message.delete()
    await ctx.send(f'yууу {user.mention}, плохой')