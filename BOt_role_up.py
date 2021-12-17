import discord   # Импортируем библиотеку discord.py
from discord.ext import commands   # Импортируем из discord.ext функцию commands
import config   # Импортируев вспомогательный файл с данными о токене бота и id некоторых каналов и ролей
import os   # Импортируем библиотеку для работы с txt файлами
client = discord.Client()   # Используем функции бибдиотеки discord

client = commands.Bot(command_prefix=('+'))   # Задаем функции client префикс, которым мы будем вызывать команды ии фунции бота.

@client.command()   # Задаем значение функции по команде. Будет выполнятся только если ввести префикс с названием функции.
async def del_role(ctx):   # Вызываем асинхронную функцию по удалении роли.
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
        if ctx.message.content.startswith('+create_role'):   #Будем выполнять если сообщение начинается с +create_role.

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
                print("something went wrong (A)")

@client.command()
async def give_role(ctx):

    if ctx.message.content.startswith('+give_role'):

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

    if ctx.message.content.startswith('+remove_role'):

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

    else:
        pass

@client.command()
@commands.has_permissions()
async def user_mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

    await member.add_roles(mute_role)
    await ctx.send(f'yууу {member.mention}, плохой')
client.run(config.TOKEN)