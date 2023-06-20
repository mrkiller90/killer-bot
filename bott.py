#ربات برای X-panel نوشته شده با telebot
#نویسنده بات : @Mr_Killer_1
#سورس ربات پابلیک شد تا عزیزان همه باهم استفاده کنیم

import telebot
import os
import requests
print("Wellcome To Mr-Killer Bot Script !\n id : @Mr_Killer_1\n")
token = input("Enter Bot Token : ")
adminid = input("Enter Admin ID : ")
admin_id = int(adminid)
host = input("Enter Api Host Link  : ")
hostt = input("Enter Host Link(XXX.com) : ")
port = input("Enter Server port : ")
udp = input("Enter udp port : ")
matn = input("Enter Wellcome Text : ")
bot = telebot.TeleBot(token)  
key1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key1.add("✍️افزودن کاربر✍️","✍️حذف کاربر✍️","🔧ادیت کاربر🔧","⚙مشخصات کاربر⚙","💾تنظیم بنر💾","🪦بکاپ🪦")
keyback = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
keyback.add("↩️برگشت↩️")
@bot.message_handler(commands=["start"])
def wellcome(message):
    bot.send_message(message.chat.id, matn, reply_markup=key1)

@bot.message_handler()
def info(message):
    if message.chat.id == admin_id: 
        if message.text == "✍️افزودن کاربر✍️":
            msg = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :",reply_markup=keyback)
            bot.register_next_step_handler(msg, name)
        elif message.text == "✍️حذف کاربر✍️":
            mssg = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :",reply_markup=keyback)
            bot.register_next_step_handler(mssg, namede)
        elif message.text == "⚙مشخصات کاربر⚙":
            mo = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :",reply_markup=keyback)
            bot.register_next_step_handler(mo, mosh) 
        elif message.text == "💾تنظیم بنر💾":
            bot.send_message(message.chat.id,"☕️متن خود را وارد کنید :",reply_markup=keyback)
            bot.register_next_step_handler(message, banner)
        elif message.text == "🪦بکاپ🪦":
            bot.register_next_step_handler(message, backup)
        elif message.text == "🔧ادیت کاربر🔧":
            msgg = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :",reply_markup=keyback)
            bot.register_next_step_handler(msgg,ename)
        elif message.text == "↩️برگشت↩️":
            bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
        
    else:
        bot.send_message(message.chat.id, "گمشو مردک فضول👹") 

def name(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global namek 
        namek = message.text
        msg = bot.send_message(message.chat.id, "🎃رمز کاربر را وارد کنید : ",reply_markup=keyback)
        bot.register_next_step_handler(msg, ramz)
def ename(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global enamek 
        enamek = message.text
        msgg = bot.send_message(message.chat.id, "🎃رمز کاربر را وارد کنید : ",reply_markup=keyback)
        bot.register_next_step_handler(msgg, eramz)
    
def ramz(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global ramzk
        ramzk = message.text
        msg = bot.send_message(message.chat.id, "🎃تعداد کاربر را وارد کنید :",reply_markup=keyback)
        bot.register_next_step_handler(msg, tedad)
def eramz(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global eramzk
        eramzk = message.text
        msgg = bot.send_message(message.chat.id, "🎃تعداد کاربر را وارد کنید :",reply_markup=keyback)
        bot.register_next_step_handler(msgg, etedad)

def tedad(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global tedadk
        tedadk = message.text
        msg = bot.send_message(message.chat.id, "🎃تاریخ انقضاء را وارد کنید :",reply_markup=keyback)
        bot.register_next_step_handler(msg, enq)
def etedad(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global etedadk
        etedadk = message.text
        msgg = bot.send_message(message.chat.id, "🎃تاریخ انقضاء را وارد کنید :",reply_markup=keyback)
        bot.register_next_step_handler(msgg, eenq)

def enq(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global enqk
        enqk = message.text
        msg = bot.send_message(message.chat.id, "🎃حجم مصرفی را وارد کنید : ",reply_markup=keyback)
        bot.register_next_step_handler(msg, trf)
def eenq(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global eenqk
        eenqk = message.text
        msgg = bot.send_message(message.chat.id, "🎃حجم مصرفی را وارد کنید : ",reply_markup=keyback)
        bot.register_next_step_handler(msgg, etrf)

def trf(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global trfk
        trfk = message.text
        url = host+"&method=adduser"
        etk = {
            "username": namek,
            "password": ramzk,
            "multiuser": tedadk,
            "traffic": trfk,
            "type_traffic": "gb",
            "expdate": enqk,
        }
        requests.post(url,etk)
        bot.send_message(message.chat.id,"☠️your user has been created✅"+"\n💥username :" " " + namek+"\n💥password :" " " + ramzk +"\n👹multiuser :" " " + tedadk+"\n🔥traffic :" " " + trfk+" "+"GB"+"\n🔗Link :"+" "+"ssh://"+namek+":"+ramzk+"@"+hostt+":"+port+"#"+namek)
def etrf(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        global etrfk
        miladi = sh_date.togregorian()
        url = host+"&method=edituser" 
        eetk = {
            "username": enamek,
            "password": eramzk,
            "multiuser": etedadk,
            "traffic": etrfk,
            "type_traffic": "gb",
            "expdate": eenqk,
        }
        requests.post(url,eetk)
        bot.send_message(message.chat.id,"☠️your user has been edited✅"+"\n💥username :" " " + enamek+"\n💥password :" " " + eramzk +"\n👹multiuser :" " " + etedadk+"\n🔥traffic :" " " + etrfk+"\n🔗Link :"+" "+"ssh://"+enamek+":"+eramzk+"@"+hostt+":"+port+"#"+enamek)


def namede(message):
    global delnamek
    delnamek = message.text
    url = host+"&method=deleteuser" 
    result = {"username": delnamek}
    requests.post(url, result)
    bot.send_message(message.chat.id,"☠️کاربر با موفقیت حذف شد✅")

def mosh(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        mosh_username = message.text
        url = host+"&method=user&username="+mosh_username
        response = requests.get(url)
        data = response.json()['data'][0]
        messagee = f"💻Username: {data['username']}\n🔗Password: {data['password']}\n🔋Traffic: {data['traffic']}\n🍷Multiuser: {data['multiuser']}\n🎈Start date: {data['startdate']}\n🎈Finish date: {data['finishdate']}"
        bot.send_message(message.chat.id, messagee)
def banner(message):
    if message.text == "↩️برگشت↩️":
        bot.send_message(message.chat.id,"↩️برگشتیم عشقم🍷",reply_markup=key1)
    else:
        matnk = message.text
        f = open("banner.txt", "w+")
        f.write(matnk)
        f.close()
        bot.send_message(message.chat.id, "☠️بنر شما با موفقیت ساخته شد !✅")
def backup(message):
    os.system("mysqldump -u 'admin' --password='pass' XPanel > /root/XPanel.sql") #بجای admin یوزر پنل و بجای pass پسورد پنل بزارید.
    file_path = "/root/XPanel.sql"
    with open(file_path, 'rb') as f:
        file_data = f.read()
    bot.send_document(message.chat.id, file_data, visible_file_name='XPanel.sql')
bot.infinity_polling()
