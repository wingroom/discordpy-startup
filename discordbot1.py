
import discord
import random

#接続オブジェクト生成
client = discord.Client()

#room制定
notification_channel = 870588066920792064 #bot通知ルーム
random_channel = 905332906661122050 #ランダム貼り付けルーム

#メンバー制定
petrushka = 558597485493485568 #ペトラ

#起動処理
@client.event
async def on_ready():
    print('botがオンラインになりました')

#通話反応部分
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and after.channel is not None:
        channel = client.get_channel(notification_channel)
        await channel.send(member.name + 'が通話に参加しました')

#メッセージ反応部分
@client.event
async def on_message(message):
    channel = client.get_channel(random_channel)
    if message.content == '/pass' and message.channel == channel and not (message.auther.bot):
        rand_s = random.randint(0, 9999)
        await message.channel.send('{:0>4}'.format(rand_s))
    if message.channel == channel and (message.auther.bot or message.suther.id == petrushka):
        rand_v = random.randint(1,14)
        if rand_v == 1:
            say = 'N-ZAP89(赤ZAP)'
        if rand_v == 2:
            say = 'ボールドマーカーネオ'
        if rand_v == 3:
            say = 'デュアルスイーパー'
        if rand_v == 4:
            say = 'ジェットスイーパー'
        if rand_v == 5:
            say = 'H3リールガン'
        if rand_v == 6:
            say = 'スプラスピナー'
        if rand_v == 7:
            say = 'バケットスロッシャー'
        if rand_v == 8:
            say = '14式竹筒銃・甲'
        if rand_v == 9:
            say = 'ホクサイ・ヒュー'
        if rand_v == 10:
            say = 'ロングブラスターネクロ'
        if rand_v == 11:
            say = 'スプラマニューバー'
        if rand_v == 12:
            say = 'ヴァルアブルローラーフォイル'
        if rand_v == 13:
            say = 'クラッシュブラスターネオ'
        if rand_v == 14:
            say = 'スプラシューターベッチュー'
        else:
            return
        await message.channel.send(say)

#botのトークン
client.run('OTA0OTE3NzMyODM3OTc4MjQz.YYCgUA.EgmrcICuriYjLylYsIsbES2w9bQ')
