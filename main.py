import discord
from discord.ext import commands
import os
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
IMAGE_DIR="images"
os.makedirs(IMAGE_DIR,exist_ok=True) 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def analiz(ctx):
    if ctx.message.attachments:
        for attachmet in ctx.message.attachments:
            file_name = attachmet.filename
            file_path= os.path.join(IMAGE_DIR, file_name)
            await attachmet.save(file_path)
            await ctx.send("görseliniz başarıyla kaydoldu")
            classname,score = get_class(file_path)
            await ctx.send(f":görselimizin sınıfı {classname},tahmin scoru:{score:.2f}")
            if classname == "poodle":
                await ctx.send("Özel Tıraşlarının Amacı Estetik Değildir: Klasik ponponlu poodle tıraşı aslında avcılık döneminden kalmadır. Tüyler köpeği soğuk suda korurken, avı rahat getirebilmeleri ve eklemlerinin üşümemesi için göğüs ve eklem kısımları dışındaki tüyler tıraş edilirdi")
            else: await ctx.send("• Binlerce yıllık geçmiş: Milattan önce 500'lü yıllardan beri var olduğu bilinen bu ırk, tarihin en eski süs ve kucak köpeği türleri arasındadır.")
    else:
        await ctx.send("görsel göndermeyi unuttunuz lütfen görsel gönderin")
bot.run("TOKEN")