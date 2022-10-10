import discord
import os
from webserver import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='from within your walls'))

@client.event
async def on_message_delete(message):
  if message.author == client.user:
    return
  if message.author.bot:
    return
  else:
    await message.channel.send(deletedspam)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.bot:
        return

    hog_list = ['hog rida', 'hog rider']
    for m in hog_list:
      if m in message.content.lower():
        await message.channel.send(hogridaspam)
      
    nft_list = ['nft', 'bitcoin']
    for m in nft_list:
      if m in message.content.lower():
        await message.channel.send(nftspam)

    mom_list = ['mom', 'mum', 'mother']
    for m in mom_list:
      if m in message.content.lower():
        await message.channel.send(momspam)
        
    dream_list = ['dream', 'minecraft']
    for m in dream_list:
      if m in message.content.lower():
        await message.channel.send(dreamspam)
        
    covid_list = ['covid', 'vaccine', 'lockdown']
    for m in covid_list:
      if m in message.content.lower():
        await message.channel.send(covidspam)
      
    china_list = ['china', 'social credit', 'communist', 'communism']
    for m in china_list:
      if m in message.content.lower():
        await message.channel.send(chinaspam)
      
    fortnite_list = ['fn', 'fortnite', 'ninja']
    for m in fortnite_list:
      if m in message.content.lower():
        await message.channel.send(fortnitespam)
      
    amongus_list = ['sus', 'imposter', 'amogus', 'among us']
    for m in amongus_list:
      if m in message.content.lower():
        await message.channel.send(amongusspam)
      
    taiwan_list = ['winnie', 'pooh', 'taiwan']
    for m in taiwan_list:
      if m in message.content.lower():
        await message.channel.send(taiwanspam)

    british_list = ['innit', 'bruv', 'queen', 'tea', 'british', 'britain', 'england']
    for m in british_list:
      if m in message.content.lower():
        await message.channel.send(britishspam)

    daddy_list = ['dad', 'father', 'daddy']
    for m in daddy_list:
      if m in message.content.lower():
        await message.channel.send(daddy)

    vegan_list = ['vegan', 'vegetarian']
    for m in vegan_list:
      if m in message.content.lower():
        await message.channel.send(vegan)

    mcqueen_list = ['mcqueen', 'chick hicks']
    for m in mcqueen_list:
      if m in message.content.lower():
        await message.channel.send(kachigga)
        await message.channel.send(holly)

    chad_list = ['chad', 'sigma', 'alpha']
    for m in chad_list:
      if m in message.content.lower():
        await message.channel.send(chad)

    french_list = ['france', 'french', 'bonjour']
    for m in french_list:
      if m in message.content.lower():
        await message.channel.send(frenchspam)

    american_list = ['america', 'texas', 'alabama']
    for m in american_list:
      if m in message.content.lower():
        await message.channel.send(americanspam)
  
    shit_list = ['shit']
    for m in shit_list:
      if m in message.content.lower():
        await message.channel.send(shitspam)
        
    sex_list = ['sex']
    for m in sex_list:
      if m in message.content.lower():
        await message.channel.send(sex)
        
    grind_list = ['grind']
    for m in grind_list:
      if m in message.content.lower():
        await message.channel.send(grind)

    bitches_list = ['bitch']
    for m in bitches_list:
      if m in message.content.lower():
        await message.channel.send(bitches)

    women_list = ['woman', 'women']
    for m in women_list:
      if m in message.content.lower():
        await message.channel.send(women)

    when_list = ['ratio', "+ L"]
    for m in when_list:
      if m in message.content.lower():
        await message.channel.send(whenspam)

    cum_list = ['cum', 'coom', 'ejaculate']
    for m in cum_list:
      if m in message.content.lower():
        await message.channel.send(cumspam)

    biden_list = ['biden', 'left', 'blm', 'feminis', 'racis']
    for m in biden_list:
      if m in message.content.lower():
        await message.channel.send(bidenspam)

    nigger_list = ['nigger', 'nigga', 'black', 'steal', 'crime', 'criminal', 'negro', 'kunta', 'kente', 'africa', 'bloods', 'crips', 'gang']  
    for m in nigger_list:
      if m in message.content.lower():
        await message.channel.send(niggerspam)
        await message.channel.send(senatorspam)

    cbt_list = ['cbt']
    for m in cbt_list:
      if m in message.content.lower():
        await message.channel.send(cbtspam)

    greetings_list = ['hey sneh', 'sup sneh', 'yo sneh', 'what up sneh', 'hello sneh', 'hi sneh']
    for m in greetings_list:
      if m in message.content.lower():
        await message.channel.send(greetingsspam)

    kys_list = ['kill yourself', 'kill urself', 'kys', 'kms', 'kill myself']
    for m in kys_list:
      if m in message.content.lower():
        await message.channel.send(kysspam)

    bdsm_list = ['bdsm', 'torture', 'dungeon', 'whip', 'kink']
    for m in bdsm_list:
      if m in message.content.lower():
        await message.channel.send(bdsmspam)
  
    else:
        return


momspam = """I do not care what you say about my mother. Your opinion is your opinion. But trust me, if you actually attempt to do something to my mother, even though she's made some bad decisions in the past that we still need to work through, I will personally call the police on you and I'll be laughing as your mugshot is shown on TV. You don't even know her, do you? The point of your entire existence seems to be to just tease other people. Well, I believe your jokes are in bad taste, and you should cease and desist digging through the dregs left at the bottom of the joke barrel; you could get a splinter, whose pain will be significantly increased by the significantly high amount of salt you carry in your bloodstream. Thank you, and let us cease talking about each other's parents."""

nftspam = """Dude I own this NFT. Do you really think that you can get away with theft when you’re showing what you stole from me directly to my face? My lawyer will make an easy job of this case. Prepare to say goodbye to your luscious life and start preparing for the streets. I will ruin you."""

hogridaspam = """okay so basically there's this guy and uhh

    ⠀⠀⠘⡀ HOG RIDAAAAAA ⠀⠀ ⠀⠀⠀  ⡜⠀⠀⠀ ⠀⠀
    ⠀  ⠑⡀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀ 
    ⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠀⠀
    ⠀⠀⠀ ⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠉⢈⠩⢙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠠⠀⠀⠨⠐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢐⠐⠌⡌⢄⢐⢈⠔⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⣿⡏⠉⡀⠐⡀⢁⠈⠐⠱⠑⡑⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⣿⢗⠀⠀⠐⡠⡛⠔⡁⢜⡔⡬⢎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⡿⠡⠀⠀⠀⠀⠂⠁⠀⠄⢂⠈⠂⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⡿⢟⠩⠐⡀⠀⠀⠀⠐⠐⠁⠓⠒⠒⢀⠁⢐⢝⢟⢿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⠫⠡⠡⠨⢀⠂⠠⠀⠀⢁⠑⡱⠛⠗⡓⢂⠠⢸⢸⢨⠣⡝⣻⣿⣿⣿⣿⣿⣿ 
    ⣿⢏⢐⢁⠊⢌⠐⡈⠄⠠⠀⠀⠀⠀⠁⠑⠈⠀⢄⢕⠸⡨⠪⡪⡘⣻⣿⡿⣿⣿⣿ 
    ⣿⢂⠂⡂⠅⡂⠅⡐⠨⢐⠐⠠⠠⡀⢄⠠⡠⡡⡱⡐⠕⢌⢊⢆⢣⢒⠽⢿⣿⣿⣿ 
    ⠣⢂⠂⠄⠡⠐⠐⠈⠌⡐⠨⡈⠢⠨⡂⢌⢂⠆⡪⠨⡊⠂⡂⠢⢡⣢⣣⡣⣍⢿⣿ 
    ⠨⢂⢂⠁⡀⠀⠀⠁⠐⠈⠐⠈⢈⠈⠐⡀⠄⠁⠌⠈⠔⣄⡀⠠⡑⡂⠆⠢⢂⠑⠽ 
    ⡨⠐⠀⠀⠀⢠⡎⡀⠀⠀⠄⠈⡀⠌⠐⠠⠈⠄⡁⠂⡀⡫⠑⣑⠀⢂⠌⠄⢕⠀⠨ 
    ⠺⡪⠢⡀⠀⠞⢇⢂⠀⠂⡀⠠⠀⠄⠁⠌⠨⠀⢄⠢⡁⢂⢿⡟⡀⠀⠈⠈⡀⠂⣰ 
    ⢀⢀⠀⠄⠀⠀⡐⠀⡈⠄⡐⠅⡊⠌⢌⠄⡕⡑⡁⢂⠂⢂⠸⣿⡄⠀⠈⣠⣴⣿⣿ 
    ⢐⠔⠠⠀⠀⡐⠠⢈⠢⢑⠄⠑⢈⠊⡂⡱⢁⣂⢌⢔⢌⢄⠀⠹⢀⣺⡿⣟⢿⣿⣿ 
    ⢀⠡⠁⠂⠐⠠⠈⠄⢈⠠⢈⢢⡣⣗⠕⠄⣕⢮⣞⣞⣗⣯⢯⡷⡴⣹⡪⣷⣿⣿⣿ 
    ⠊⠄⠠⠠⠡⠈⠠⢐⠠⡊⡎⣗⢭⢐⠹⡹⣮⡳⡵⣳⣻⢾⣻⣽⣻⣺⣺⣽⣿⣿⣿ 
    ⣨⣾⢐⠰⠐⠅⡂⡂⢕⢜⢜⢵⢹⢑⢔⠨⢘⠸⡹⡵⣯⣻⢽⣳⣻⣺⢞⡿⣿⣿⣿ 
    ⣿⣿⡔⠠⢈⠐⠐⢠⢱⢸⢸⢸⢸⠰⡡⢘⢔⢕⠝⢮⣳⢽⢝⡾⡵⡯⣏⠯⣿⣿⣿ 
    ⣿⣿⣗⢅⢢⠠⠡⠢⡱⡑⡕⡕⢅⠣⡊⢨⢪⡣⡣⡂⡬⡳⢽⢽⢽⢽⣞⣧⠙⣿⣿ 
    ⡻⣿⡯⡪⠢⡡⠡⢑⢌⠪⡪⡊⠆⢌⠪⢐⢕⢱⢱⢱⢱⢱⢙⢮⡫⡟⣞⢮⣳⠙⣿ 
    ⠊⣿⣯⠪⡊⠄⢅⠂⢂⠁⢇⢇⢃⠂⢕⠐⠌⡲⡰⡡⣇⠇⢇⢕⠪⠉⠂⠅⠂⡑⠹ 
    ⣸⢿⣳⢱⠨⡐⡽⡿⡶⡾⡬⡢⢂⠅⡢⢡⣌⠐⠈⢎⢎⢎⢔⠠⠡⠠⠠⠡⡁⡂⠡ 
    ⡯⡯⡇⢅⠕⠠⢱⢹⡙⢮⢹⠨⡂⡂⢇⠌⠮⡳⠅⡂⢕⠡⡑⠠⢁⢁⣡⣡⣢⣶⣿ 
    ⣗⢽⢌⡢⡡⡡⡸⡢⡣⡣⡱⡑⠔⡈⢎⢆⢂⠂⠅⣢⡳⣽⡐⢅⢂⣊⣿⣿⣿⣿⣿ 
    ⣯⢯⢷⢽⢮⢯⣺⣪⢞⡮⣳⢘⠔⢌⢜⣞⣖⣮⣻⢮⣯⢷⣿⣻⣿⣿⣿⣿⣿⣿⣿ ]
    ⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

dreamspam = """hello guys i need help. i was in science class… i got up to sharpen my dream pencil, and then my dream themed dildo fell out of my ass. i always keep it down there cause I like to imagine daddy dream fucking me 24/7 and it feels so good. anyways it fell out of my ass and out of my pants and my dreamphobic classmates started laughing and making fun of me. the teacher sent me to the office and i had to explain what happened. the principal suspended me from school for a week!!! this is unacceptable. just because i love dream is not a reason to harass me"""

amongusspam = """AMONG US Funny Moments! How to Free Robux and VBUCKS in SQUID GAME FORTNITE UPDATE! (NOT CLICKBAIT) MUKBANG ROBLOX GAMEPLAY TUTORIAL (GONE WRONG) Finger Family Learn Your ABCs at 3AM! Fortnite Impostor Potion! MrBeast free toys halal gameplay nae nae download حدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًا Super Idol的笑容都没你的甜八月正午的阳光都没你耀眼热爱 105 °C的你滴滴清纯的蒸馏水 amongla download Meme Compilation (POLICE CALLED) (GONE WRONG) (GONE SEXUAL) (NOT CLICKBAIT) Minecraft Series Lets Play Videos Number 481 - Poop Funny Hilarious Minecraft Roblox Fails for Fortnite - How to install halal minecraft cheats hacks 2021 still works (STILL WORKS 2018) Impostor Gameplay (Among Us) Zamn"""

fortnitespam = """Hello, concerned father here. My son has recently got into the game called Fortnite? I've spent well over $500 on this game and its becoming a problem. Apparently the game is down right now and its causing a lot distress for my child. He keeps taking my newspaper and tries to "full piece" me. I don't know what this means but I'm starting to think its something associated with the devil. He won't come with us anywhere unless we take a "launch pad" to get there. Its starting to get worse by the hour and I don't know how much longer I can take this. His legs, arms, and hands are shaking violently yet he refuses to take any type of medicine unless its a "big pot" or "chuggies." Someone please help me."""

covidspam = """I have gotten the covid vaccine about 20 times now. 4 Pfizer, 12 moderna, 4 Johnson. Once I got my first vaccine, I started cravings for it. There is something so great knowing I am reducing the spread of the coronavirus with each of them. I am feeling so empowered. I think I may be addicted ngl 😅. At least it won't kill me."""

taiwanspam = """ATTENTION CITIZEN! 市民请注意!

⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿ 
⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿ 
⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿ 
⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻ 
⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄ 
⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄
ATTENTION CITIZEN! 市民请注意!

This is the Ministry of State Security. 您的浏览记录和活动引起了我们的注意 YOUR INTERNET ACTIVITY HAS ATTRACTED OUR ATTENTION. 同志們注意了 you have been found protesting in Predators!!!!! 這是通知你，你必須認同我們將接管台灣 serious crime 以及世界其他地方 100 social credits have been deducted from your account 這對我們未來的所有下屬來說都是重要的機會 stop the protest immediately 立即加入我們的宣傳活動，提前獲得救贖 do not do this again! 不要再这样做! if you do not hesitate, more social credits ( -11115 social credits )will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 ccp) you'll also be sent into a re-education camp in the xinjiang uyghur autonomous zone.

为党争光! Glory to the CCP!"""

chinaspam = """Let us all stand for the national anthem.

三民主義，吾黨所宗；
以建民國，以進大同。
咨爾多士，為民前鋒；
夙夜匪懈，主義是從。
矢勤矢勇，必信必忠；
一心一德，貫徹始終。
Praise be to 中华民国政府! Down with the illegitimate capitalist 中国共产党, fraudulent usurpers of 大陸!

Glory to the 中華民國!"""

britishspam = """OI OI OI!

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣠⣾⣷⣿⣿⣿⣷⣄⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⠁⣩⣿⣿⣿⠿⣿⡿⢿⣿⣿⣿⠛⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢷⣾⣿⣋⡡⠤⣀⣷⣄⠠⠤⣉⣿⣷⣽⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡻⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣟⢋⣰⣯⠉⠉⣿⢄⠉⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⢿⣷⣶⠤⠔⣶⣶⠿⢾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡀⠠⠀⠂⠀⠀⣧⡚⢿⣿⡶⢶⡿⠟⣠⣿⣿⠀⠀⠀⠀⠄⣀⡀⠀⠀ 
⠒⠒⠋⠁⠀⠀⠀⠀⠀⠀⢿⣷⣄⡀⠀⠀⠀⣈⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠒ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠒⠐⠺⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⣋⣀⡄⠠⣢⣀⣩⣛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀

WOTS ALL THIS???

🇬🇧🇬🇧🇬🇧

YER POISTIN LOICENSE HAS EXPOIRED!!!! 🇬🇧🇬🇧🇬🇧🇬🇧

ONE HUNNIT TESCO CLUBCARD POINTS 'AVE BIN DEDUCTED FROM YER ACCOUN'!!!!! 🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧

YER THREE QUID MEAL DEAL IS GONNA BE A FIVER FROM NOW ON!!!! 🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧

YER WILL ALSO ONLY BE ABLE TER CHOOSE FROM A CHICKEN OR 'AM SANDWICH!!!! 🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧

FAILURE TO RENEW YER LOICENCE IS GONNA RESUL' IN THA LOSS OV MORE CLUBCARD POINTS!!!!!!!! 🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧

🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧🇬🇧"""

daddy = "<:dad:702316747025285140>"

vegan = """https://tenor.com/view/carrot-facial-vegan-bukkake-gif-15315590"""

kachigga = """KACHIGGA! KACHIGGA!"""

holly = "https://cdn.discordapp.com/attachments/788846236072935476/951758251517689876/image0.jpg"

chad = "<:GIGACHAD:926301685754761247>:question:"

frenchspam = """Why a dick as big as the Eiffel tower is not as impressive as you may think in Kendrick Lamar's "Backseat Freestyle," Kendrick says the line, "I pray my dick get big as the Eiffel Tower, So I can fuck the world for seventy-two hours". While at first a dick as big as the Eiffel tower may seem to be a dong of immense magnitude, when taking into account the sheer size of earth, the lucky one to be fucked by this dick, we realize that it is not as spectacular as the young MC claims it to be. The Eiffel tower stands at 1063 feet, while the diamater of earth is approximately 41.804 million feet. If Kendrick inserts his Eiffel penis into the earth, his dick would only take up .000025 percent of the earth's vagina. That is pathetic. Kendrick is not fucking the world for 72 hours with his Eiffel tower micropenis. The Earth will get bored after 10 minutes and finish herself with a vibrator the size of Argentina. Be better Kendrick."""

americanspam = """I'm a regular John from city Kansas. I love burgers, soda and my native country very much, but I do not understand our government. Everyone says America is a great country, and I look around and see who else is a great China. China has a very strong government and economy. Chinese resident is a great man. And the greatest leader Xi. Thick hair, strong grip, jade rod! We would have such a leader instead of sleeping in negotiations, rare hair, soft pickle, bad memory old Beadon. Punch!"""

shitspam = """I hate taking shits. Taking shits is the worst function of the human organism after sex. You have to sit on the most uncomfortable seat ever, then you have to go through so much pain to push the shit out of your asshole (not to mention sometimes they get stuck in there). And as if those weren't enough then you have to wipe, you have to take your hand along with toilet paper and shove it up your asshole, this process can sometimes take minutes out of your life, it fucking sucks.

TL;DR I hate shitting"""

sex = """No sex before marriage"""

grind = "I live in the American Gardens building on West 81st street. My name is Patrick Bateman. I'm 27 years old. I believe in taking care of myself, and a balanced diet and a rigorous exercise routine. In the morning, if my face is a little puffy, I'll put on an ice pack while doing my stomach crunches. I can do a thousand now. After I remove the ice pack, I use a deep pore cleanser lotion. In the shower, I use a water activated gel cleanser. Then a honey almond body scrub. And on the face, an exfoliating gel scrub. Then apply an herb mint facial mask, which I leave on for 10 minutes while I prepare the rest of my routine. I always use an aftershave lotion with little or no alcohol, because alcohol dries your face out and makes you look older. Then moisturizer, then an anti-aging eye balm followed by a final moisturizing protective lotion. There is an idea of a Patrick Bateman, some kind of abstraction, but there is no real me. Only an entity, something illusory. And though I can hide my cold gaze, and you can shake my hand and feel flesh gripping yours and maybe you can even sense our life styles are probably comparable, I simply am not there."

bitches = """No bitches?

⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀ 
 ⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀ ⠀
 ⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀ ⠀⠀
  ⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀ ⠀⠀⠀
    ⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
      ⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
      ⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
      ⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀
    ⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀
    ⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀
    ⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

women = """Looking for a female roommate to pay $0 rent

I will not charge you money. but I will be sharing my bed with you as the other room is being used by my parents. They are aware of this arrangement as I have done this before but it has not worked out for reason I rather not say on here. I will except hugs at least 5 times a day, and cuddles at least 2 times a day for at least 10 minutes each. You will not be dating any other man during this arrangement. you will have no male friends either. You may have female friends and they May visit if they like. You will also be required to make me meals 3 times a day. Phsyical requirements are as stated: Must be shorter than 5'5", weigh no more than 120 lbs, caucasian or asian only, republican, no tattoos, no vegans, no smoking/vaping, marrywania, and you MUST shave legs and underarms. I am 44-male/290 lbs last time I checked, 5'6". Please contact me if you would like this arrangement."""

whenspam = """don’t care + didn’t ask + cry about it + who asked + stay mad + get real + L + bleed + mald seethe cope harder + dilate + incorrect + hoes mad + pound sand + basic skill issue + typo + ratio + ur dad left + you fell off + no u + the audacity + triggered + repelled + ur a minor + k. + any askers + get a life + ok and? + cringe + copium + go outside + touch grass + kick rocks + quote tweet + think again + not based + not funny didn’t laugh + social credits -999, 999, 999, 999 + get good + reported + ad hominem + ok boomer + small pp + ur allergic to sunlight + GG! + get rekt + trolled + your loss + muted + banned + kicked + permaban + useless + i slept with ur mom + yo momma + yo momma so fat + redpilled + no bitches allowed +  + talk nonsense + trump supporter + your’re a full time discord mod + you’re* + grammar issue + nerd + get clapped + go outside + bleach + lol + gay + retard + autistic + reported + ask deez + ez clap + straight cash + idgaf + ratio again + stay mad + pedophile + cancelled + done for + don't give a damn + get a job + sus + baka + sussy baka + furry + rip bozo + you're a (insert stereotype) + Super Idol的笑容 + you lose + no one cares + log off + don't care even more + sex offender + sex defender + get religion + not okay + NFT owner + you look like a wall + you don’t know 2 + 2 with yo head ass + you are going to my cringe compilation + you can’t count to five + try again + you failed kindergarten + rickrolled + no lifer + guten freunden schickt man einen deutschen panzer + you have a anime profile picture + an* + fatherless + motherless + sisterless + brotherless + orphan + you can't catch this ratio + catch some bitches + genshin player + 日本語がお上手ですね + get fucked + you can’t understand what the word intelligence means with your dumb ass + put some thought into what you're going to do with that + stfu + go to bed + yes, i'm taller than you + i think your joke is funny + i rejected your mother's advances + I win + final ratio"""

cumspam = """The birds are singing, the flowers are blooming, my dick is throbbing, what a beautiful day for cooming. Good morning, A, I've been awake for 20 whole seconds and I haven't coomed yet. It's time to hope on my porn throne and machine gun jackhammer my bloodshot death-grip bloodshot semi chub with my roided doomfist once again! (Types on keyboard). I-s...is that a?? HMMGH, I-I MUST SNIFF, SNNNNNNNNIIIIIIIIIIIIFFFFFFFF** OH GOD (FAPFAPFAPFAP) FUCCKK, HUHGHU, SNIIFF, HUHGJGUHHGUGHU (SMASHES DESK) I-I-IM COOOMING!!!!! IM COOMING, IM COOMING IM COOOMING IM COOOOOMING COOOOOOOOOOM, COOOMING, FUCCKKK, AHHAFHHAHUHG, COOOOOM, AW FUCK ITS EVERYWHERE, COOOOOM, AWGAHUGHAHG. Aw fuck, aw fuck. oh jesus. ahhghhha, there you are, my slippery white goo to the world, my son, my son...Well, it's time to get breakfast...well a little coom first wouldn't hurt."""

niggerspam = """I hate niggers"""

bidenspam = """Joe Biden’s America

LIBRAL SCOOL BE LIKE:

9:00: GAY LESON!!

9:45: how to be be GAYY!!

10:30: TRANS LERNINNG!!

11:15: GAY RECESS!!

11:45: CROSDRESING HOUR!!

12:45: GAY LESON!!!

1:30: TRANGENER LUNCH!!

2:15: BLM PERIOD!!!

3:00: COMUNIS T HISTORY!!

3:30: TAKE NON BINAR BUS HOME!!

THIS IS WHAT THE LEFT WANT!"""

senatorspam = """https://tenor.com/view/senator-armstrong-armstrong-metal-gear-rising-mgr-speech-bubble-gif-25397532"""

cbtspam = """https://tenor.com/view/metal-gear-rising-hmm-thinking-smile-gif-12571277"""

deletedspam = """https://tenor.com/view/i-saw-w-gus-fring-gus-gustavo-deleted-gif-25440636"""

greetingsspam = """https://cdn.discordapp.com/attachments/942126123624591392/1025977109434343464/hello-chat.gif"""

bdsmspam = """https://tenor.com/view/moistcritical-m0istcritikal-let-me-slip-into-something-more-comfortable-gassed-up-shawty-gif-20088754"""

kysspam = """https://tenor.com/view/moistcr1itkal-charlie-white-jr-penguiz0dance-penguinz0-speed-up-dance-gif-24799632"""

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
