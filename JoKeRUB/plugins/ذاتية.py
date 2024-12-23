from telethon import * 
 
#Here we have imported all classes from module telethon 
 
#Now lets create a instance for our userbot 
#I will name it as Tejas , U can give any name you want to give 
 
api_id = 3768462 
api_hash = "afabdecf9b755c2aed3cadba26741d52" 
 
# We defined our api id and api hash 
 
tejas = TelegramClient("session_name" , api_id= api_id , api_hash= api_hash) 
 
#We need api id and api hash to connect our account to userbot 
# You can get api id and api hash from the link given in the description below 
 
 
# So lets build our first command that we will use to chek our bot is working or not 
@tejas.on(events.NewMessage(outgoing=True , pattern=r".قنوات السورس")) 
async def greeting(event): 
    chat = await event.get_chat() 
     
    await tejas.edit_message(event.message , "قنوات السورس 
1 - @E_4_R
2 - @RobinUserBot
3 - @uui7rb") 
# We have created our first command .hi, This will make us 
 
# That outgoing = True indicates that userbot will respond to only us and our messages , if anyone else try to use this command the userbot will ignore him/her 
 
 
# So now we will start our client 
 
print("Bot is running...") 
 
tejas.start() 
tejas.run_until_disconnected() 
#We have started our userbot