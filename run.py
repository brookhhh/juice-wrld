import time
import discord.ext
import random

token: str = "put token here"  # ez
delay = input("enter your delay\n")  # this is not jank
prefix = input("enter your prefix\n")  # and this is jank (it throws so many errors to me for no reason)


class MyClient(discord.Client):
    # intro
    print("Juice wrld!!! I LOVE JUICE WRLD!!!")
    time.sleep(1.5)
    print("not really recommended to run as admin but it doesnt really matter")
    time.sleep(1)
    option1 = input("put 'secret' to run this...")

    # actual self bot bit of code
    if option1 == "secret":
        print("juice wrld cyan selfbot work work work deposit! (made by brook)")
        time.sleep(1.5)
        print("when you want it to start just type start in the channel you want to selfbot in")

        class MyClient(discord.Client):

            async def on_ready(self):
                print('logged on account, ready to bot') # this doesnt appear i literally got no reason for it to exist lol

        async def on_message(self, message):
            if message.author != self.user:
                return

            if message.content == 'start':
                while 6 > 4:
                    identifier = random.uniform(1, 9000)
                    await message.channel.send(prefix + ' work')  # https://www.reddit.com/r/introvert/comments/3ewxpe/how_many_of_you_introverts_just_work_sleep_eat/
                    time.sleep(0.7)
                    await message.channel.send(prefix + ' dep all')  # imagine deposit as eating
                    print("cycle id number", identifier, "done, sleeping for", delay, "s\n")  # sometimes this will throw an error for some reason
                    time.sleep(int(delay))


client = MyClient()
client.run(token)
