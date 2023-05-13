import discord # made by yıldırımlord#4444
import asyncio
from datetime import datetime
from requests import get


r = get("https://raw.githubusercontent.com/yildirimlord/smsnoktapy/main/sms.py").text # güncel sms apilerini yükler, silersen apiler gidince yenilerini çekip güncellemez :)

with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()

if read == r:
    pass
else:
    print("En güncel bilgiler aktarılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTEwNjU2MTkwMDM3Mzg3MjY1MA.GS19Zs.t2nP1iNK2cx3aW2VUGc-4C1ctHn3KquY6Paqp4"
gif = ""  # embede ekleyeceğiniz gif linki (https://auto.creavite.co bu sitede kıyağım olsun gidip parayla yaptırmayın)
adet = 15   # komut kullanınca kaç sms göndereceğidir
saniye = 0   # sms i kaç saniye aralıklarla göndereceğini ayarlarsınız

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.streaming, name="Made By Mates") # Botun oynuyor kısmıdır
    await client.change_presence(status=discord.Status.idle, activity=activity) # Botun online / offline / boşta / rahatsız etme modudur


    # Aşağıda oynuyor kısmını değiştirmek isteyenler için bilgilendirme yapıldı
# discord.ActivityType.playing: Oynuyor kısmı
# discord.ActivityType.streaming: Yayında kısmı
# discord.ActivityType.listening: Dinliyor kısmı
# discord.ActivityType.watching: İzliyor kısmı
    # idle = boşta | dnd = rahatsız etme | online = çevrimiçi | offline = çevrimdışı

# made by yıldırımlord#4444

        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author == client.user or not message.content.startswith("!"):
        return
    if message.guild is None: # Sadece özel mesajda ise
        await message.channel.send("Bu komutu sadece sunucu kanallarında kullanabilirsiniz.", delete_after=6) ### KOMUTLAR ÖZEL DM MESAJLARINA ÇALIŞMASIN
        return

    if message.content.startswith("!sms "):
        telno = message.content.split(" ")[1]
        if len(telno) == 10:
            sent_time = datetime.now() # mesajın gönderildiği zamanı kaydet
            desc = f"Kullanıcı: `{message.author.name}#{message.author.discriminator}`\nGönderme zamanı: `{sent_time.strftime('%d/%m/%Y %H:%M:%S')}`\n\nİşleminiz başarıyla sıraya alındı, sıra uzunluğuna göre gönderim başlayacaktır.\n*Bizi tercih ettiğiniz için teşekkürler.*"
            embed = discord.Embed(title="SMS Platformu", description=desc, color=0x00eeee)
            embed.set_footer(text="Made By mates - ©2023") # footer
            embed.set_image(url=gif) # yukardaki gifi embede ekler
            sent_message = await message.channel.send(embed=embed, delete_after=15)
            await message.delete()

            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")

            embed = discord.Embed(
                title="Sms platformu!",
                description="Başarılı şekilde işlemin tamamlandı. *Bizi tercih ettiğin için teşekkürler.*"
            )
            embed.set_footer(text="Bu mesaj 30 saniye sonra otomatik olarak silinecektir. | Made By mates ") ## KOMUTU KULLANANA ÖZELDEN MESAJ AT VE 30 SANİYE SONRA SİL

            sent_sms_message = await message.author.send(embed=embed)
            await asyncio.sleep(30)
            await sent_sms_message.delete()
          ### Eğer girien numara hatalıysa
        else:
            embed = discord.Embed(title="Hata", description="Geçersiz telefon numarası girdiniz. `+90` eklemeden deneyiniz.", color=0xff0000)
            await message.channel.send(embed=embed, delete_after=6)
      ###  Yardım menüsü
    elif message.content == "!yardım":
        embed = discord.Embed(title="Yardım", description="Aşağıdaki komutları kullanabilirsiniz:", color=0x00eeee)
        embed.add_field(name="`!sms [telefon numarası]`", value="Belirtilen telefon numarasına bir SMS gönderir.", inline=False)
        await message.channel.send(embed=embed, delete_after=9)

######## !temizle komutu kenaldaki mesajları temizler sdece @rolleri yönet yetkisi olanlar kullanabilir !temizle yazılması yeterli
    elif message.content == "!temizle":
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send("Bu komutu kullanmak için Mesajları Yönet yetkisine sahip olmanız gerekiyor.", delete_after=6)
            return

        deleted = await message.channel.purge()
        await message.channel.send(f"{len(deleted)} adet mesaj kanaldan uçuruldu!", delete_after=6)

###### EĞER BOTTA OLMAYAN BİR KOMUT KULLANIRSA
    else:
        embed = discord.Embed(title="Hata", description="Böyle bir komut yok. Yardım için `!yardım` yazabilirsiniz.", color=0xff0000)
        await message.channel.send(embed=embed, delete_after=6)



# made by yıldırımlord#4444




client.run(TOKEN)
