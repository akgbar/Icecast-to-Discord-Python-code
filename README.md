# Icecast-to-Discord-Python-code
A simple bot for streaming your Icecast2 radio to Discord 
First step you must create a Discord Bot.
I will not explain how to create a Bot right now. 
I spent days do figure it out how to set permissions and invite to my server. So, That's your homework lol.
After you created a bot go to "Bot" tab and I recommend save your Token in text file.

Credits to: https://github.com/captainmustard/Icecast2DiscordBot
I could not make his way work, so I did mine. But followed his steps mostly.

You must install requirements.
I assume you are on Windows 11. But most of the commands are apply for Linux too.
If you are not on Win11 then install Python3 and dependencies and set PATH for it.

Open Windows Shell
type python3 - it will install automatically if you don't have it - if you have it you should be able to enter command line >>> just exit()

install pip 
install requirements

pip install -r reqs.txt

pip install PyNaCl

winget install "FFmpeg (Essentials Build)"

restart Shell

python3 disco.py 

you must invite your bot into your server and find specific voice channel ID by right clicking on it.
and you must send "PM" instead of typing command in general chat. ( I am new so I couldn't figure out yet also tired at this moment lol) 
Example: /live 1231231241232131

your bot should join the voice chat and start streaming your music.

I am NOT a serious programmer. Feel free to fork it, copy it, adjust it, manipulate it, whatever. I am satisfied with the results that is why I am sharing. 
I tested everything on Linode Ubuntu servers. Then find out I could run this bot on my PC whenever I needed to. So, it's cheaper. But If you want to run your bot constantly on a server I recommend to use Linode. Follow my referral link if you haven't tried yet: 

With my invite code you will receive a $100, 60-day credit once a valid payment method is added to your new account.

https://www.linode.com/lp/refer/?r=0d68775921ab28759691f3e09ecd492cd036abc0
