import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import asyncio
import random
import datetime
client = discord.Client()
bot = discord.Client()
token =  'ODAxNjIzNjE4NTMzNzIwMDk1.YAjYLA.EmWZOo2tn3HDb8fAs57g7U8y_ro'
@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    status = cycle(["'x도움'로 명령어 알아보기", f'{len(client.guilds)}서버 | {len(client.users)}명', 'xk봇 V1.0.0'])

    @tasks.loop(seconds=7)
    async def change_status():
        await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

    change_status.start()
@client.event
async def on_message(message):
    if message.content == 'x핑':
        embed = discord.Embed(title=':ping_pong:', description='**Pong !**', color= 0x0000ff) #embed라는 변수를 지정, 색깔을 0x0000ff로 지정, 제목을 ":ping:pong:", 내용을 "Pong !" 이라고 지정한다.
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url) #embed 변수의 footer를 설정, 글을 메세지를 입력한 사람의 태그로 지정하고 아이콘을 메세지를 입력한 사람의 아바타 (프로필 사진) 으로 지정한다.
        embed.add_field(name = '`Ping`', value = str(client.latency*1000) + 'ms') # 필트 지정 코드, name 은 제목을, value는 내용을 나타낸다.
        await message.channel.send(embed=embed)
    if message.content.startswith('x투표'):
        subject = message.content[6:]
        embed = discord.Embed(title="찬반투표!", description="찬성은 따봉을 반대는 싫어요 반응을 눌러주세요!", color=0x0088ff)
        embed.add_field(name="주제", value=subject, inline=False)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    if message.content.startswith("x청소"):
        if message.content == "x청소":
            await message.channel.send(
                embed=discord.Embed(title="에러 발생", description="올바른 명령어는 'x청소 (청소할 개수)'에요", color=0xff0000))
        else:
            if message.author.guild_permissions.administrator or message.author.id == 704535152763601007:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(embed=discord.Embed(title="청소기능 발동",
                                                                   description=f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다",
                                                                   color=0x00ff00))
            else:
                await message.channel.send(
                    embed=discord.Embed(title="오류발생", description=f"{message.author.mention}님은 권한이 없어요",
                                        color=0xff0000))
                return
    if message.content.startswith('x타이머'): # `!타이머` 라는 메시지를 받았을 때
        if message.content == 'x타이머': # 만약 메시지가 숫자 없이 `!타이머` 만 있다면
            await message.channel.send(f"{message.author.mention} \n그래서 몇 초를 맞추라고요?\n올바른 명령어는 `x타이머 (숫자)` 에요!") # 몇 초를 맞추라는지 출력한다.
        else: #그렇지 않다면
            timer = int (message.content.split(" ")[1]) # 타이머를 숫자만큼 지정한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 설정되었습니다.\n시간이 끝나면 맨션해드릴게요!") # 설정 완료 메시지를 보낸다.
            await asyncio.sleep(timer) # 그 숫자만큼 대기한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 끝났어요!")
    if message.content.startswith('x초대'):
        await message.channel.send('봇을 초대하려면 아래의링크로 봇을 초대하세요 \nhttps://discord.com/api/oauth2/authorize?client_id=801623618533720095&permissions=8&scope=bot')
    if message.content.startswith("x파티모집"):
        Game = message.content[6:]
        await message.channel.send(f'{message.author.mention}님과 같이 "{Game}"를 하실분을 찾습니다')
    if message.content == "x가위바위보 가위" or message.content == "x가위바위보 바위" or message.content == "x가위바위보 보":
        random_ = random.randint(1, 3)

        if random_ == 1:
            if message.content == "x가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저도 가위! 비겼습니다.")
            elif message.content == "x가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 가위! {message.author.mention}님이 이겼습니다.")
            elif message.content == "x가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 가위! 제가 이겼습니다.")
        elif random_ == 2:
            if message.content == "x가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 바위! 제가 이겼습니다.")
            elif message.content == "x가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저도 바위! 비겼습니다.")
            elif message.content == "x가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 바위! {message.author.mention}님이 이겼습니다.")
        elif random_ == 3:
            if message.content == "x가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 보! {message.author.mention}님이 이겼습니다.")
            elif message.content == "x가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 보! 제가 이겼습니다.")
            elif message.content == "x가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저도 보! 비겼습니다.")
    if message.content == "x프로필":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x000000)
        embed.add_field(name="닉네임", value=message.author, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.add_field(name="디스코드가입일", value=str(date.year) + "-" + str(date.month) + "-" + str(date.day),
                        inline=False)
        joat = message.author.joined_at.isoformat().split("T")[0]
        embed.add_field(name="서버가입일", value=joat, inline=False)
        st = str(message.author.status)
        if st == "online":
            sta = "온라인"
        elif st == "offline":
            sta = "오프라인"
        elif st == "idle":
            sta = "자리비움"
        elif st == "dnd":
            sta = "방해금지"
        embed.add_field(name="상태", value=sta, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith('안녕'):  # 만약 사용자가 '안녕'이라고 입력햇을떄
        await message.channel.send('ㅎㅇ')  # 봇이 'ㅎㅇ'라고 말한다
client.run(token)