from concurrent.futures import TimeoutError
import discord
from discord.ext import commands, tasks
from discord import File
import asyncio
from time import *
import threading
import os
import logging
import csv

session = 0
cancel = 0
points = 0
hint = 0
timer = 20
author = "None"


def countdown():
    global my_timer
    global session
    my_timer = timer
    global cancel
    for x in range(timer):
        if cancel == 1:
            session = 0
            return
        print(my_timer)
        if my_timer < 1:
            return
        my_timer = my_timer-1
        sleep(1)

def questionsanswers(id):
    try:
        with open(str(id) + '.csv', 'r', encoding="utf-8") as f:
            questionsanswers = []
            reader = csv.reader(f)
            for row in reader:
                print(row)
                questionsanswers.append(row)
            return questionsanswers
    except:
        logging.exception("message")
        raise FileNotFoundError

def edittrivia(server, questions):
    try:
        with open(str(server) + '.csv', 'w+', newline='', encoding="utf-8") as f:
            addrow = csv.writer(f)
            for question in range(len(questions)):
                row = [questions[question][0]]
                for answer in range(1, len(questions[question])):
                    row.append(questions[question][answer])
                addrow.writerow(row)
    except:
        raise FileNotFoundError

class trivia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trivia(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles:
            global hint
            global session
            global points
            global author
            print(session)
            if session == 1:
                await ctx.channel.send("There is already a trivia session in progress. Use .triviacancel to cancel it")
                return


            def checkr(reaction, user):
                trivia = discord.utils.get(user.guild.roles, name="Trivia Participation")
                return reaction.message.channel.id == 677197493838151720 and str(reaction.emoji) == '✅' and user.id != 594235987438075915 and trivia in user.roles


            questions = questionsanswers(ctx.message.guild.id)
            total = len(questions)
            if questions[0][0] == 'question':
                total = len(questions) - 1
            print(questions)
            start = await ctx.channel.send("**Please read carefully before starting.**\n-You will have " + str(timer) + "s to answer each question. The answers are not case sensitive.\n-There may or may not be a hint available on each question. You can activate the hint by reacting with ❓. If there is a hint available and you choose to use it, you will only be given 0.5 points for a correct answer (instead of 1)\n-There are a total of " + str(total) + ''' questions, each worth 1 point.\n\n__**Rules for Participants:**__ *- Don't spoil/leak any trivia questions.* (met with disqualification or worse punishments)
*- Don't spoil/leak any trivia questions.* (met with disqualification or worse punishments)
*- Don't search answers on any search engines.* (met with disqualification)
*- Make sure to spell your answer correctly, but if you make a typo, you can re-write your final answer as long as the timer isn't over. Write numerical answers as numbers rather than spelling them out.*
*- If the bot does not understand your answer/ or slight spelling mistake, trivia hosts may add you points if they consider it warranted.* 
*- If you have any questions, feedback, or consider there is a different correct answer than the one added onto the bot, feel free to talk about it at the end of your trivia session*. 

**-> And most importantly, enjoy the trivia!**\n\nWhen ready, react with ✅ below.''')
            await start.add_reaction(emoji='✅')
            await self.client.wait_for('reaction_add', check=checkr, timeout=300)
            session = 1
            try:
                print(ctx.message.guild.id)
                message = ctx.message
                channel = message.channel
                points = 0
                counter = 1
                hint = 0

                first = 1
                logs = ""
                for question in range(len(questions)):
                    good = False
                    ans = None
                    answer = ""
                    correctanswers = ""
                    if questions[question][0] == 'question':
                        continue
                    def check(message):
                        try:
                            trivia = discord.utils.get(message.author.guild.roles, name="Trivia Participation")
                            print(author)
                            print(str(message.author))
                            return message.channel == channel and trivia in message.author.roles and str(message.author) == author
                        except:
                            return False
                    try:
                        countdown_thread = threading.Thread(target=countdown)
                        countdown_thread.start()
                        await channel.send("Q " + str(question) + ": " + questions[question][0])
                        global cancel
                        while my_timer > 0:
                            if cancel == 1:
                                raise ZeroDivisionError
                            ans = await self.client.wait_for('message', check=check, timeout=my_timer)
                    except ZeroDivisionError:
                        await channel.send('Trivia has been cancelled.')
                        await asyncio.sleep(1)
                        cancel = 0
                        session = 0
                        return
                    except TimeoutError:
                        logging.exception("message")
                        if ans is not None:
                            answer = ans.content
                        await channel.send("Your answer was: " + answer)
                        await asyncio.sleep(1)
                        for answers in range(2, len(questions[question])):
                            if questions[question][answers] == "":
                                continue
                            if answer.lower().replace(" ", "") == questions[question][answers].lower().replace(" ", ""):
                                good = True
                            correctanswers = correctanswers + questions[question][answers] + ","
                        correctanswers = correctanswers[:-1]
                        await channel.send("The correct answer(s) was/were: `" + correctanswers + "`")
                        await asyncio.sleep(1)
                        if good == True and hint == 0:
                            await channel.send("Congratulations, you got the right answer!")
                            points = points + 1
                        elif good == True and hint == 1:
                            await channel.send("Congratulations, you got the right answer. However, since a hint was used, only 0.5 points will be given.")
                            points = points + 0.5
                        else:
                            await channel.send("Unfortunately, you did not have the right answer.")
                        await asyncio.sleep(1)
                        print(points)
                        hint = 0

                        logs += "Q" + str(counter) + ":" + questions[question][0] + "\nA: " + correctanswers + "\nU: " + answer + "\nTotal pts: " + str(points) + "\n\n"
                        if question < len(questions)-1:
                            await channel.send("``` ```Get ready for the next question:")
                        counter = counter + 1
                        await asyncio.sleep(5)
                await channel.send("Your final score is: " + str(points) + "/" + str(total))
                if first == 1:
                    try:
                        os.remove(str(author) + ".txt")
                        first = 0
                    except:
                        first = 0
                with open(str(author) + ".txt", "a+", newline='') as f:
                    f.write(logs)
                    f.write("Final Score: " + str(points) + "/" + str(total))
                await self.client.get_channel(702061726127882331).send("Final Score for " + str(author) + ": " + str(points) + "/" + str(total),file=File(str(author) + ".txt"))

                os.remove(str(author) + '.txt')
                session = 0
            except:
                logging.exception("msg")
                await ctx.channel.send("Something went wrong.")
                session = 0

    @commands.command()
    async def triviacancel(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles:
            global cancel
            cancel = 1

    @commands.command()
    async def tp(self, ctx, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles:
            if ctx.channel.id == 677197493838151720:
                await ctx.channel.purge(limit=int(arg))

    @commands.command()
    async def addpoints(self, ctx, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles:
            global points
            points = points + float(arg)
            if int(arg) > 0:
                await ctx.channel.send("Point(s) added.")
            else:
                await ctx.channel.send("Point(s) removed.")

    @commands.command()
    async def setpoints(self, ctx, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles:
            global points
            points = float(arg)
            await ctx.channel.send("Points set.")

    @commands.command()
    async def triviatimer(self, ctx, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            global timer
            timer = int(arg)
            await ctx.channel.send("Timer set to " + str(arg) + " seconds")

    @commands.command()
    async def triviaupload(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            for attachment in ctx.message.attachments:
                await attachment.save(str(ctx.message.guild.id) + '.csv')
            await ctx.channel.send("Trivia uploaded.")

    @commands.command()
    async def triviadownload(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                await ctx.channel.send(file=File(str(str(ctx.message.guild.id) + '.csv')))
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def trivialist(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                questions = questionsanswers(ctx.message.guild.id)
                print(questions)
                for question in range(len(questions)):
                    correctanswers = ""
                    if questions[question][0] == 'question':
                        continue
                    else:
                        for answers in range(2, len(questions[question])):
                            if questions[question][answers] == "":
                                continue
                            correctanswers = correctanswers + questions[question][answers] + ","
                        correctanswers = correctanswers[:-1]
                        await ctx.channel.send("Q" + str(question) + ": " + questions[question][0] + "\nH:" + questions[question][1] + "\nA: " + correctanswers)
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def triviaedit(self, ctx, arg1, number, *, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                questions = questionsanswers(ctx.message.guild.id)
                if arg1.lower() == 'q' or arg1.lower() == 'question':
                    questions[int(number)][0] = arg
                    await ctx.channel.send("Question edited. Use .trivialist or .triviadownload to view all the questions.")
                if arg1.lower() == 'a' or arg1.lower() == 'answer' or arg1.lower() == 'answers':
                    hint = questions[int(number)][1]
                    questions[int(number)] = [questions[int(number)][0]]
                    questions[int(number)].append(hint)
                    for answer in arg.split(","):
                        questions[int(number)].append(answer)
                    await ctx.channel.send("Answer edited. Use .trivialist or .triviadownload to view all the questions.")
                if arg1.lower() == 'h' or arg1.lower() == 'hint':
                    questions[int(number)][1] = arg
                    await ctx.channel.send("Hint edited. Use .trivialist or .triviadownload to view all the questions.")
                if arg1.lower() == 'all':
                    questions[int(number)] = arg.split(",")
                    await ctx.channel.send("Question and answer edited. Use .trivialist or .triviadownload to view all the questions.")
                edittrivia(ctx.message.guild.id, questions)
            except IndexError:
                await ctx.channel.send("Question not found.")
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def triviaadd(self, ctx, *, arg):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                with open(str(ctx.message.guild.id) + '.csv', 'a+', newline='', encoding="utf-8-sig") as f:
                    addrow = csv.writer(f)
                    row = arg.split(',')
                    addrow.writerow(row)
                    await ctx.channel.send(
                        "Question Added. Use .trivialist or .triviadownload to view all the questions.")
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def triviadel(self, ctx, num):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                questions = questionsanswers(ctx.message.guild.id)
                del questions[int(num)]
                await ctx.channel.send(
                    "Question deleted. Use .trivialist or .triviadownload to view all the questions.")
                edittrivia(ctx.message.guild.id, questions)
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def triviaclear(self, ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        if manager in ctx.author.roles:
            try:
                os.remove(str(ctx.message.guild.id) + '.csv')
                await ctx.channel.send('Trivia deleted.')
            except FileNotFoundError:
                await ctx.channel.send("Trivia file not found.")

    @commands.command()
    async def triviahelp(self,ctx):
        manager = discord.utils.get(ctx.author.guild.roles, name="Trivia Organizer")
        host = discord.utils.get(ctx.author.guild.roles, name="Trivia Host")
        if manager in ctx.author.roles or host in ctx.author.roles:
            await ctx.channel.send("For Trivia Organizers:\n`.triviatimer [time in seconds]` - Sets the trivia answer timer.\n`.triviaupload [file]` - Upload questions, hints and answers. Format as `question, hint, answer1, answer2, etc`. Newline for new question."
                                   "\n`.triviadownload` - Download the current trivia sheet.\n`.trivialist` - Shows the current trivia sheet.\n`.triviaedit [q/h/a/all] [q#] [question/hint/answer1,answer2,etc/question,hint,answers]` - Edit an existing question, hint, answers, or everything."
                                   "\n`.triviaadd [question,hint,answer]` - Adds a question to the current trivia sheet.\n`.triviadel [q#]` - Deletes the entered question.\n`.triviaclear` - Deletes the entire trivia sheet."
                                   "\n\nFor Trivia Hosts:\n`.trivia` - Begins a trivia session.\n`.tp [number]` - Purges `number` of messages. Only works in <#677197493838151720>.\n`.triviacancel` - Cancels active trivia session.\n`.addpoints [n]` - Adds n points.\n`.setpoints [n]` - Sets the points to n.")

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 594235987438075915:
            if message.content.startswith("Q "):
                await message.add_reaction(emoji='❓')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global author
        if user.id == 594235987438075915:
            return
        if reaction.emoji == "❓":
            if reaction.message.author.id == 594235987438075915:
                if str(user.name) + "#" + str(user.discriminator) == author:
                    if reaction.message.content.startswith("Q "):
                        global hint
                        questions = questionsanswers(reaction.message.guild.id)
                        if questions[int(reaction.message.content.split(":")[0].split(" ")[1])][1].replace(" ", "") == "":
                            await reaction.message.channel.send("Sorry, there are no hints available for this question.")
                        else:
                            await reaction.message.channel.send("Hint: " + questions[int(reaction.message.content.split(":")[0].split(" ")[1])][1])
                            hint = 1

        if reaction.emoji == '✅':
            if reaction.message.author.id == 594235987438075915:
                print()
                author = str(user.name) + "#" + str(user.discriminator)






def setup(client):
    client.add_cog(trivia(client))