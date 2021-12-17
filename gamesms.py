import asyncio
import discord
from discord.ext import commands
import random
import time
import config
bot_Mess = commands.Bot(command_prefix = '+')

@bot_Mess.command()
async def guess_game(ctx, type, userch):
    author = ctx.message.author
    try:
        winner = False
        z = ''
        if int(type) == 1:
            rannum = random.randint(0,10)
            if int(userch) == rannum:
                winner = True
                z = 'Обычный везунчик'
            else:
                z = 'Лузер'
        elif int(type) == 2:
            rannum = random.randint(0, 100)
            if int(userch) == rannum:
                winner = True
                z = '1%'
            else:
                z = 'Может в казино?'
        elif int(type) == 3:
            rannum = random.randint(0, 1000000)
            if int(userch) == rannum:
                winner = True
                z = 'БОГОПОДОБЕН'
            else:
                z = 'Ожидает многого от жизни'
        else:
            await ctx.send(f'Ошибка')
            return
    except:
        await ctx.send(f'Ошибка')
        return
    await ctx.send('🎲 бот подкручивает шансы... 🎲')
    time.sleep(1)
    if winner:
        await ctx.send('Поздравляю, но скольких попыток это тебе стоило?')
    else:
        await ctx.send('Потом повезет... Пытайся больше :)')
        await ctx.send(f'Всего лишь надо было написать {rannum}')
    await author.edit(nick = z)

@bot_Mess.command()
async def rps(ctx):
    author = ctx.message.author
    rps_arr = ['Камень', 'Ножницы', 'Бумага']
    botchoice = random.choice(rps_arr)
    await ctx.send('Камень? Ножницы? Бумага? Выбирай внимательно.')
    user_choice = await bot_Mess.wait_for('message')
    t = user_choice.content
    if t == 'Камень':
        if botchoice == 'Камень':
            await ctx.send(f'🗿 == 🗿 \n {author.mention} думает аналогичну компьютеру 🧐')
        elif botchoice == 'Ножницы':
            await ctx.send(f'🗿 >> ✂ \n Поздравляю с победой {author.mention}')
        else:
            await ctx.send(f'🗿 << 📝 \n Хе-хе обкрутил камень {author.mention} 🦾 ')
        return
    elif t == 'Бумага':
        if botchoice == 'Камень':
            await ctx.send(f'📝 >> 🗿 \n {author.mention} обыграл бота. Поздравим!')
        elif botchoice == 'Ножницы':
            await ctx.send(f'📝 << ✂ \n Хах, {author.mention} думал победить компьютер 👹')
        else:
            await ctx.send(f'📝 == 📝 \n {author.mention} - это компьютер?? Не верю 😥')
    elif t == 'Ножницы':
        if botchoice == 'Камень':
            await ctx.send(f'✂ << 🗿 \n Злой бот сломал ножницы {author.mention} 🤖')
        elif botchoice == 'Ножницы':
            await ctx.send(f'✂ == ✂ \n {author.mention} сыграл вничью со мной  🧠')
        else:
            await ctx.send(f'✂ >> 📝 \n {author.mention} прочитал меня и переиграл 🥶')
    else:
        await ctx.send('Ошибка! Введите ваш выбор правильно.')

@bot_Mess.command()
async def rusgame(ctx, opponent: discord.Member):
    author = ctx.message.author
    await ctx.send(f'{author.mention} предлагает сыграть {opponent.mention} в Русскую рулетку 😬🔫')
    time.sleep(0.5)
    await ctx.send(f'{opponent.mention}, введите любой символ, если согласны')

    def check(user):
        z = user.author.name + '#' + user.author.discriminator
        return str(z) == str(opponent)
    try:
        user_choice = await bot_Mess.wait_for('message', timeout=5.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f'{opponent.mention} не захотел испытывать свою жизнь или не успел принять приглашение 💔')

    else:
        newnicknames = ['zxcghoul666', 'dead inside', 'thx for SBEU', 'le-le-le me die']
        nick = random.choice(newnicknames)
        players = [author, opponent]
        whofirst = random.choice(players)
        whosecond = opponent
        if whofirst == author:
            await ctx.send(f'{author.mention} начинает испытание на смерть!')
        else:
            await ctx.send(f'{opponent.mention} попытается выжить в первом ходу!')
            whosecond = author

        baraban = [0] * 6
        baraban[random.randint(0,5)] = 1
        for i in range(len(baraban)):
            if i == len(baraban) - 1:
                await ctx.send(f'{whosecond.mention} завещает все своей собаке и идет на верную смерть')
                return
            elif i%2 == 0:
                await ctx.send(f'{whofirst.mention} стреляет')
                time.sleep(1)
                if baraban[i] == 0:
                    await ctx.send(f'{whofirst.mention} везёт! Он выживает с {int(100-int(1/(len(baraban) - i) * 100))}% шансом')
                if baraban[i] == 1:
                    await ctx.send(f'{whofirst.mention} погибает от шальной пули😭')
                    await whofirst.edit(nick=nick)
                    return
            else:
                await ctx.send(f'{whosecond.mention} испытывает свою удачу')
                time.sleep(1)
                if baraban[i] == 0:
                    await ctx.send(f'{whosecond.mention} везёт! Он выживает с {int(100-int(1/(len(baraban) - i) * 100))}% шансом')
                if baraban[i] == 1:
                    await ctx.send(f'{whosecond.mention} получает СБЭУ👺')
                    await whosecond.edit(nick=nick)
                    return
bot_Mess.run(config.TOKEN)
