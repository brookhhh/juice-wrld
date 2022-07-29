import time
import discord.ext
import random
from datetime import datetime


token: str = "put token here"  # ez
now = datetime.now()
current_time = now.strftime("%H:%M:%S") # skidded cos im lazy to do datetime this shit so useless on my momma 

if token == "put token here":
    # SO JANK WAY OF DOING THIS
    print("no token for selfbot, closing")
    time.sleep(3)
    exit()

prefix = input("enter your prefix\n")


class MyClient(discord.Client):

    print("woah the time is", current_time)
    time.sleep(1)

    dynamicOrNAH = input("type 'dynamic' for dynamic delay or 'static' for static delay\n")

    if dynamicOrNAH == "static":
        print("Juice wrld!!! I LOVE JUICE WRLD!!!")
        time.sleep(1.5)
        print("not really recommended to run as admin but it doesnt really matter")
        time.sleep(1)
        option1 = input("put 'run' to run this...\n")

        # actual self bot bit of code
        if option1 == "run":
            print("juice wrld cyan selfbot work work work deposit! (made by brook)")
            time.sleep(1.5)
            print("when you want it to start just type start in the channel you want to selfbot in and check the console")

            class MyClient(discord.Client):

                async def on_ready(self):
                    print('logged on account, ready to bot')

            async def on_message(self, message):
                if message.author != self.user:
                    return

                if message.content == 'start':
                    delay = input("type what delay you want in seconds (i.e 30)\n")
                    while 6 > 4:
                        identifier = random.uniform(1, 9000)
                        await message.channel.send(prefix + 'work')
                        time.sleep(0.7)
                        await message.channel.send(prefix + 'dep all')
                        print("cycle id number", identifier, "done, sleeping for", delay, "s")
                        time.sleep(int(delay))
        else:
            print("closing")
            time.sleep(3)
            exit()

    if dynamicOrNAH == "dynamic":
        print("Juice wrld!!! I LOVE JUICE WRLD!!!")
        time.sleep(1.5)
        print("not really recommended to run as admin but it doesnt really matter")
        time.sleep(1)
        option1 = input("put 'run' to run this...\n")

        # actual self bot bit of code
        if option1 == "run":
            print("juice wrld cyan selfbot work work work deposit! (made by brook)")
            time.sleep(1.5)
            print("when you want it to start just type start in the channel you want to selfbot in and check the console")

            class MyClient(discord.Client):

                async def on_ready(self):
                    print('logged on account, ready to bot')

            async def on_message(self, message):
                if message.author != self.user:
                    return

                if message.content == 'start':
                    dynamic1 = input("enter the first number in seconds (i.e if you wanted to do 30-32 do 30 here)\n")
                    dynamic2 = input("enter the second number in seconds (i.e if you wanted to do 30-32 do 32 here)\n")
                    while 6 > 4:
                        identifier = random.uniform(1, 9000)
                        dynamic_delay = random.uniform(int(dynamic1), int(dynamic2))
                        await message.channel.send(prefix + 'work')  # https://www.reddit.com/r/introvert/comments/3ewxpe/how_many_of_you_introverts_just_work_sleep_eat/
                        time.sleep(0.7)
                        await message.channel.send(prefix + 'dep all')  # imagine deposit as eating
                        print("the time is", current_time, "this was cycle number", round(identifier), "sleeping for", round(int(dynamic_delay)), "s")
                        time.sleep(int(dynamic_delay))
        else:
            print("closing")
            time.sleep(3)
            exit()


client = MyClient()
client.run(token)
