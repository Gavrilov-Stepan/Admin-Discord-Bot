import discord
import os
from discord.ext import commands
bot_Mess = commands.Bot(command_prefix=('+')) #префикс всех команд у бота устанавливается +
bot_Mess.remove_command('help') #удаление команды help

@bot_Mess.command(pass_context = True)
async def clear(ctx, amount=25):
   '''Функция запускается при отправке участником discord-сервера сообщения +clear amount, где amount - количество сообщений. она служит для очистки последних сообщений количества amoun.
   аргумент ctx функции отвечает за контекст
   аргумент amount функции отвечает за количество находящихся в чате сообщений, которые необходимо удалить'''
   await ctx.channel.purge(limit=amount + 1) #в этой строчке происходит очистка канала, в который была отправлена команда об очистке на amount сообщений. если не устанавливать amount при написании команды, бот удалит последние 25 отправленных сообщений. +1 потому что само сообщение с командой для очистки также учитывается при подсчете, из-за этого из уже находившихся в чате сообщений удаляется на одно меньше

@bot_Mess.command(pass_context = True)
async def BW(ctx):
   '''Функция запускается при отправке участником discord-сервера сообщения +BW. она служит для получения ранее установленного на сервере списка запрещенных для использования слов. список таких слов, то выведет, что эти слова не установлены.
   badwords - переменная, содержащая массив слов из файла, куда записываются запретные слова
   read_words - переменная, куда считывается файл с запретными словами
   аргумент ctx функции отвечает за контекст'''
   badwords = [] #задается переменная badwords, описанная выше
   try: #программа пытается открыть файл words.txt на чтение. если такого файла не находится, то выполняется except
      read_words = open('words.txt', 'r') #открывает файл words.txt, который лежит в той же папке, что и бот
   except FileNotFoundError: #выполняется, если при try возникает ошибка. тогда сначала файл создается и открывается на запись, затем закрывается и, наконец, открывается на чтение
      read_words = open('words.txt', 'w') #создает файл words.txt, открывает его на запись
      read_words.close() #закрывает файл words.txt
      read_words = open('words.txt', 'r') #открывает файл words.txt на чтение
   for word in read_words: #считывает строки в ранее открытом файле words.txt(в функции addBW каждое новое запретное на сервере слово добавляется в файл words.txt с новой строки
      badwords.append(word.strip()) #записывает считываемые строкой кода ранее строки файла words.txt в массив badwords как новые элементы
   read_words.close() #закрывает файл words.txt
   if badwords != []: #следующая строка выполняется, если в badwords есть какие-либо строки(если список запрещенных на сервере слов не пустой
      await ctx.send(f"Current forbidden words list: {badwords}") #при ранее описанном условии выводит все запрещенные на сервере слова
   else: #выполняется, если на сервере нет недопустимых слов
      await ctx.send("No forbidden words added on this server. Feel free to write whatever you want!") #если на сервере нет запрещенных слов, то пишет в чат, что их нет

@bot_Mess.command(pass_context = True)
async def bot_commands(ctx):
   '''Функция запускается при отправке участником сервера сообщения +bot_commands. она служит для служит для получения в чат списка применимых к боту команд
   channel - канал сервера, в который отдаются команды'''
   channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот
   await channel.send('This is what i can do:\n'+
         '+bot_commands: you can check all commands\n'+
         '+BW: you can check all forbidden words\n'+
         '+addBW: you can add one or more words to forbidden words list. To do this, write them after a command\n'+
         '+clearBW: you can clear forbidden words list\n'+
         '+createCh: you can create one or more text channel(s). To do this, write their names after a command\n'+
         '+deleteCh: you can delete one or more text channel(s). To do this, write their names after a command\n'+
         '+clear: you can delete some last messages. To do this, write count after a command. Default value: 25\n'+
         '+kick: you can kick a user who breaks the rules. To do this, mention him after a command\n'+
         '+choose: bot helps you to choose on of the written variants\n'+
         '+roll: returns random number from 1 to 100\n'+
         '+del_role: deletes a role from the list\n'+
         '+create_role: creates your personally role\n'+
         '+give_role: gives you one of the created roles list\n'+
         '+remove_role: removes a role on the list\n'+
         '+mute: mutes a mentioned member\n'+
         '+rusgame: play a russian game!\n'+
         '+rps: play rock paper scissors\n'+
         '+guess_game: play a number guessing game') #вывод всего списка команд бота, каждая команда с новой строчки

@bot_Mess.command(pass_context = True)
async def addBW(ctx):
   '''Функция запускается при отправке участником сервера сообщения +addBW она служит для добавления через пробел слов, которые требуется добавить в список запретных
   new_badwords - переменная, записывающая в массив записанные через пробел слова, которые требуется запретить на сервере
   channel - канал сервера, в который бот будет писать
   banwords_list - переменная, куда считывается на запись файл с запретными словами
   аргумент ctx функции отвечает за контекст'''
   new_badwords = ctx.message.content.split(' ') #создается список новых запрещенных слов. в него также будет записана сама команда для вызова функции(+addBW), но учавствовать в программе дальше и записываться в список уже имеющихся слов тоже не будет
   if new_badwords == ['+addBW']: #выполняется, если с командой на вход не поступило никаких параметров(новых слов)
      channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот
      await channel.send('To add some new words, write them separated by space') #отправка сообщения, говорящего о том, как правильно использовать команду: писать команду, после нее слова, которые нужно запретить
   else: #выполняется, если пользователь все ввел верно и на вход с командой поступили нужные слова
      try: #пробует выполнить открытие файла на дозапись в конец файла с запрещенными словами
         banwords_list = open('words.txt', 'a') #само открытие файла
      except FileNotFoundError: #если файла в папке с ботом не находится, то сначала файл создается и открывается на запись, затем закрывается и, наконец, открывается на дозапись
         banwords_list = open('words.txt', 'w') #создает файл words.txt, открывает его на запись
         banwords_list.close() #закрывает файл words.txt
         banwords_list = open('words.txt', 'a') #открывает файл words.txt на чтение
      if os.stat("words.txt").st_size > 0: #проверяет файл на пустоту. если в файле уже есть слова, то в следующие две строчки он добавляет новые, полученные ранее через знак \n переноса строки
         for word in new_badwords[1:]: #проходится по новым запретным словам
            banwords_list.write('\n' + word) #добавляет их с новой строки в файл
      else: #выполняется, если файл с запретными словами пустой, что выполняется, если он был либо только что создан, либо очищен при помощи команды +clearBW
         banwords_list.write(new_badwords[1]) #записвает без переноса на новую строку первое слово из введенных пользователем вместе с командой. если бы ну было проверки на пустоту файла, и все состояло только из строчек кода под else:, то на этом моменте для пустого файла перенос был бы уже на первой строке, что создавало бы ситуацию, что введенные слова записываются начиная со 2-й строки, а 1-ая остается пустой, и из-за этого любое сообщение из отправленных пользователями, удалялось бы с жалобой на то, что содержит запрещенное на сервере слово(следует из того, что пустая строка является подстрокой любой другой строки)
         if len(new_badwords) > 2: #проверяет, что количество введенных пользователем слов, которые надо запретить, больше одного(элемент массива new_badwords с индексом 0 - команда +addBW, которую, очевидно, в запретные слова вносить не нужно
            for word in new_badwords[2:]: #дописывает в конец открытого файла все  оставшиеся незаписанными слова
               banwords_list.write('\n' + word) #собственно, сама команда для дозаписи
      channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот
      await channel.send('New words were successfully added to list') #отправляет отчет об успешной записи слов в файл

@bot_Mess.command(pass_context = True)
async def clearBW(ctx):
   '''Функция очищает файл от всех добавленных туда запретных слов
   badwords - переменная, куда считывается полностью очищенный в силу аргумента "w" у функции open() файл с запрещенными словами
   channel - канал сервера, в который бот будет писать
   аргумент ctx функции отвечает за контекст'''
   badwords = open('words.txt', "w") #открытие очещенного от запрещенных слов файла на запись
   badwords.close() #закрытие файла
   channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот
   await channel.send('Forbidden words list was successfully erased') #отправляет отчет об успешной очистке файла

@bot_Mess.event
async def on_message(message):
   '''Функция, активирующаяся при отправлении пользователем любого сообщения. Проверяет его на наличие ссылок(для защиты других пользователей) и на наличие запрещенных на сервере слов
   аргумент message функии - полученное сообщение
   channel - канал сервера, в который бот будет писать
   word - переменная, получающая и хранящая текст сообщения
   embed - переменная, хранящая особый формат, в котором должно выводться сообщение о нарушении
   badwords_file - переменная, в которую открывается для чтения файл с запрещенными словами
   badwords - переменная, хранящая запретные слова'''
   if message.author.name != 'Mimist': #проверяет, что имя пользователя, отравившего сообщение - не имя самого бота. сделано, чтобы бот не зациклился
      if 'https://' in message.content or 'http://' in message.content: #проверяет сообщение на наличие ссылок
         await message.delete() #если в сообщении содержится ссылка, то удаляет ее
         await message.channel.send(f"{message.author.mention} Don't send links!") #отправляет в канал, в котором считал сообщение, требование к пользователю не отправлять ссылки
         channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот
         word = message.content #задание содержимого сообщения в отдельную переменную
         embed = discord.Embed(title="Suspicious link alert!", description=f"{message.author.name} just sent a suspicious link: {word}",color=discord.Color.blurple()) #задает особый формат, в котором должно выводться сообщение о нарушении
         await channel.send(embed=embed) #отправляет сообщение в указанный выше канал в особом, также указанном выше, формате
         await message.author.send(f"Sending links isn't available on this server") #отправляет личное сообщение пользователю с информацией о том, что ссылки на сервере отправлять нельзя
         return #завершает работу функции
      else: #выполняется если не найдено ссылки в сообщении
         try: #пробует открыть на чтение файл с запрещенными словами
            badwords_file = open('words.txt', 'r') #открытие файла с запретными словами
         except FileNotFoundError: #если файла в папке с ботом не находится, то сначала файл создается и открывается на запись, затем закрывается и, наконец, открывается на чтение
            badwords_file = open('words.txt', 'w') #создание файла и открытие его на запись
            badwords_file.close() #закрытие файла
            badwords_file = open('words.txt', 'r') #открытие файла на чтение
         badwords = [] #создает переменную, в которую перенесутся запрещенные слова
         for word in badwords_file: #записывает все строки файла с запрещенными на сервере словами в массив как отдельные элементы(одна строка в файле содержит одно запрещенное слово)
            badwords.append(word.strip()) #записывает считываемые строкой кода ранее строки файла words.txt в массив badwords как новые элементы
         badwords_file.close() #закрывает открыты на чтение файл с запрещенными словами
         for word in badwords: #перебирает запрещенные слова
            if word in message.content: #проверяет считанное сообщение на наличие в нем запрщенного на сервере слова
               await message.delete() #удаляет сообщение, если находит в нем запрещенное слово
               await message.channel.send(f"{message.author.mention} Don't use that word!") #отправляет в чат требование к пользователю не использовать запрещенные слова
               channel = bot_Mess.get_channel(920228968907554858) #задание того канала, в который будет писать бот следующие сообщения
               word = message.content #задание содержимого сообщения в отдельную переменную
               embed = discord.Embed(title="Profanity Alert!", description=f"{message.author.name} just said ||{word}||", color=discord.Color.blurple()) #задает особый формат, в котором должно выводться сообщение о нарушении
               await channel.send(embed=embed) #отправляет сообщение в указанный выше канал в особом, также указанном выше, формате
               await message.author.send(f"Please stop using bad words!") #отправляет личное сообщение с требованием прекратить использовать запрещенные слова его автору
               return #останавливает функцию
      await bot_Mess.process_commands(message) #останавливает работу всех остальных

@bot_Mess.command()
@commands.has_permissions(administrator = True)
async def createCh(ctx, *channels):
   '''Функция создания произвольного количества каналов на сервере. На вход принимается сама команда и названия новых каналов через пробел. Команда требует прав администратора.
   аргумент ctx функции - контекст
   аргумент *channels функции - перечень всех названий для новых каналов, записывается в список channels'''
   for channel in channels: #перебирает все названия для новых каналов среди введенных в сообщении
      await ctx.guild.create_text_channel(channel) #получает сервер, на который было отправлено сообщение, затем создает там текстовым каналом со взятым из списка в цикле названием
      await ctx.send(f'text channel {channel} has been created') #отправляет в канал, в который было отправлено сообщение, ответ о том, что канал с указанным названием был создан

@bot_Mess.command()
@commands.has_permissions(administrator = True)
async def deleteCh(ctx, *channels: discord.TextChannel):
   '''Функция удаления произвольного количества каналов на сервере. На вход принимается сама команда и названия каналов, которые требуется удалить. Команда требует прав администратора.
   аргумент ctx функции - контекст
   аргумент *channels функции - перечень всех названий удаляемых каналов, записывается в список channels'''
   for channel in channels: #перебирает все названия удаляемых каналов среди введенных в сообщении
      await channel.delete() #удаляет на сервере канал по заданному названию
      await ctx.send(f'text channel {channel} has been deleted') #отправляет в канал, в который было отправлено сообщение, ответ о том, что канал с указанным названием был удален

@bot_Mess.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx, user: discord.Member):
   '''Функция исключения указанного участника сервера. На вход принимается сама команда и имя участника. Команда требует прав администратора.
   аргумант ctx функции - контекст
   аргумент user - имя пользователя, которого требуется исключить'''
   await ctx.channel.purge(limit = 1) #удаляет одно сообщение из канала, а именно то, которое и было с требованием исключить участника
   await ctx.send(f'{user.mention} was kicked from this server by {ctx.message.author.mention}') #отправляет в канал сообщение, что указанный пользователь был кикнут с сервера отправителем команды
   await user.send(f'You were kicked from server by {ctx.message.author.mention}') #отправляет исключенному пользователю личное сообщение о том, что он был исключен с сервера
   await user.kick() #удаляет указанного участника с сервера


TOKEN = open('token.txt', 'r').read()
bot_Mess.run(TOKEN)