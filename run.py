import time
import discord.ext
import random

token: str = "put token here"


class MyClient(discord.Client):
    # intro
    print("Juice wrld!!! I LOVE JUICE WRLD!!!")
    time.sleep(1.5)
    print("not really recommended to run as admin but it doesnt really matter")
    time.sleep(1)
    option1 = input("put secret to run this...")

    # actual self bot bit of code ahead
    if option1 == "secret":
        print("juice wrld unbelieveaboat selfbot work work work deposit! (made by brook)")
        time.sleep(1.5)
        print("your money will probably be beamed by expando if you do this, but that's not my fault")
        time.sleep(1.5)
        print("when you want it to start just type start in the channel you want to selfbot in")

        class MyClient(discord.Client):
            async def on_ready(self):
                print('logged on account', self.user, 'ready to bot')

        async def on_message(self, message):
            # only respond to ourselves
            if message.author != self.user:
                return

            if message.content == 'start':
                while 6 > 4:
                    
                    identifier=random.uniform(1,9000)
                    await message.channel.send('!work')  # work
                    time.sleep(0.7)
                    await message.channel.send('!dep all')  # https://tenor.com/view/kitsune-shy-anime-gif-17046222
                    print("cycle id number", identifier, "done, sleeping for 30s\n") # id system jamk, its just to let you know its working
                    time.sleep(29.5)


client = MyClient()
client.run(token)
