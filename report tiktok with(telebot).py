import requests , time , os , telebot , threading , random
from telebot import types
from Topython import Proxy , Tiktok
 
token = input('Token : ')
bot = telebot.TeleBot(token)

stop = True
work = 0
not_wrok = 0
reports = 0
not_send = 0
erorr_proxy = 0

def buttons():
    report = types.InlineKeyboardButton(text ="( Report Tik Tok )",callback_data = "report")
    chproxy = types.InlineKeyboardButton(text ="( Check Proxy )",callback_data = "chproxy")
    info_button = types.InlineKeyboardButton(text="( Informations )", callback_data="info")
    proxy_button = types.InlineKeyboardButton(text="( Get Proxy )", callback_data="getproxy")
    programmer = types.InlineKeyboardButton(text ="( Programmer )",url="t.me/g_4_q")
    channel = types.InlineKeyboardButton(text ="( Channel )",url="t.me/ToPython")
    github = types.InlineKeyboardButton(text="Open Web", web_app=types.WebAppInfo(url="https://github.com/is-L7N"))
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(report)
    markup.add(chproxy,proxy_button)
    markup.add(info_button)
    markup.add(programmer,channel)
    markup.add(github)
    return markup
    
def back_buttons():
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back ⤴️ )", callback_data="back")
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(back_button)
    return markup

def back2_buttons():
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back ⤴️ )", callback_data="back2")
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(back_button)
    return markup

def check_buttons():
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Proxy Checker )", callback_data="check_proxy")
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(back_button)
    return markup

def checker_buttons(proxy):
    global work , not_wrok
    markup = types.InlineKeyboardMarkup()
    proxybut = types.InlineKeyboardButton(text=f"( Proxy : {proxy} )", callback_data="But")
    workbut = types.InlineKeyboardButton(text=f"( Work : {work} )", callback_data="But")
    notworkbut = types.InlineKeyboardButton(text=f"( Not Work : {not_wrok} )", callback_data="But")    
    stoper = types.InlineKeyboardButton(text="( Stop )", callback_data="stop")
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(proxybut)
    markup.add(workbut,notworkbut)
    markup.add(stoper)
    return markup
    

def report_buttons(username):
    global erorr_proxy , reports , not_send
    markup = types.InlineKeyboardMarkup()
    userbut = types.InlineKeyboardButton(text=f"( Username : {username} )", callback_data="But")
    reportbut = types.InlineKeyboardButton(text=f"( Reports :  {reports} )", callback_data="But")
    erorrproxybut = types.InlineKeyboardButton(text=f"( Bad Proxy :  {erorr_proxy} )", callback_data="But")
    erorrsendbut = types.InlineKeyboardButton(text=f"( Not Send :  {not_send} )", callback_data="But")
    stoper = types.InlineKeyboardButton(text="( Stop )", callback_data="stop")
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(userbut)
    markup.add(reportbut)
    markup.add(erorrproxybut,erorrsendbut)
    markup.add(stoper)
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    get_nams = f"t.me/{message.from_user.username}"
    tag = f"[{message.from_user.first_name}]({get_nams})"
    sent_message = bot.send_message(
    message.chat.id,
    f"*Hi* {tag}* To Bot Report TikTok Accounts\nSelect From the Buttons To Work !*",
    parse_mode="Markdown",
    disable_web_page_preview=True,
    reply_markup=buttons())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global stop
    message = call.message
    if call.data == "report":
        Function(message)
    elif call.data == "chproxy":
        Function3(message)     
    elif call.data == "info":
        Function2(message)
    elif call.data == "getproxy":
        Function4(message)
    elif call.data == "stop":
        stop = False
    elif call.data == "back2":
        Function(message)
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
    elif call.data == "back":
         edit1(call,message)
         bot.clear_step_handler_by_chat_id(call.message.chat.id)

def edit1(call,message):
   get_nams = f"t.me/{message.from_user.username}"
   tag = f"[{message.from_user.first_name}]({get_nams})"   
   bot.edit_message_text(
   f"*Hi* {tag}* To Bot Report TikTok Accounts\nSelect From the Buttons To Work !*",
   disable_web_page_preview=True,
   chat_id=call.message.chat.id,
   message_id=call.message.message_id,
   parse_mode="Markdown",
   reply_markup=buttons()) 

def Function(message):
    bot.edit_message_text(
    'Send Me Username TikTok  \n'
    '> The Report is 100% real ',
    chat_id=message.chat.id,
    message_id=message.message_id,
    parse_mode='MarkdownV2',
    reply_markup=back_buttons())
    bot.register_next_step_handler(message, get_info)

def Function2(message):  
    bot.edit_message_text(
    'To begin with, you can check the proxies to avoid errors and some bans from TikTok , You must choose a Fan account or an account that contains sensitive content to report  \n'
    '> The Report is 100% real \n'
    'Use the bot freely , good luck \\!',
    chat_id=message.chat.id,
    message_id=message.message_id,
    parse_mode='MarkdownV2',
    reply_markup=back_buttons())

def Function3(message):
    bot.edit_message_text(
    "Send the proxy file, Preferably <http>",
    chat_id=message.chat.id,
    message_id=message.message_id,
    reply_markup=back_buttons())

def Function4(message):
    try:
        response = requests.get("https://raw.githubusercontent.com/is-L7N/proxies/main/proxies.txt")
        if os.path.exists("newProxy.txt"):
            os.remove("newProxy.txt")
        with open("newProxy.txt", "w") as f:
            f.write(response.text)
        with open("newProxy.txt", 'rb') as file:
            bot.send_document(message.chat.id, file ,caption="Done Get New Proxies !")
    except Exception as e:
        bot.reply_to(message,f"Erorr : {e}")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        info = bot.get_file(message.document.file_id)
        down = bot.download_file(info.file_path)        
        src = message.document.file_name
        with open(src, 'wb') as f:
            f.write(down)

        with open(src, 'r', encoding='utf-8') as file:
            lines = file.readlines()           
        get_proxy(message,lines=lines) 

    except Exception as e:
        bot.reply_to(message,f"Erorr : {e}")

def get_proxy(message,lines):
    sent_message = bot.reply_to(message, f"Done Save: `{len(lines)}` Proxy ✅", parse_mode="Markdown")
    main(message, lines, sent_message.message_id)

def proxyfor(lines):
       return [proxy.strip() for proxy in lines]

def main(message, lines, reply_message_id):
    proxies = proxyfor(lines)
    threads = []
    for proxy in proxies:
            time.sleep(0.5)         
            thread = threading.Thread(target=check_proxy, args=(message, proxy, reply_message_id))
            threads.append(thread)
            thread.start()
    try:
        bot.reply_to(message,"The Checker Completed ! ",reply_markup=back_buttons())
        
    except Exception as e:
        bot.send_message(message.chat.id,"Erorr Send File")   
    os.remove("workProxy.txt")
    for thread in threads:
            thread.join()

def check_proxy(message, proxy, reply_message_id):
    global work , not_wrok
    response = Proxy.https(proxy)
    if response:
        work += 1            
        with open("workProxy.txt", 'w') as f:
               f.write(proxy + '\n')
    else:
        not_wrok += 1
    print(not_wrok)        
    bot.edit_message_text(
    f"The Checker has Started ",
    chat_id=message.chat.id,
    message_id=reply_message_id,
    reply_markup=checker_buttons(proxy))

def get_info(message):
    username = message.text
    try:
        info = Tiktok.information(username)
        name = info['name']
        id = info['id']       
        country= info['country']
        flag = info['flag']
        sent_message = bot.reply_to(message,"The Reports is Being Sent , Wait a little... ")
        Reports(message,name,id,country,flag,username,sent_message.message_id)
    except Exception as e:
        bot.reply_to(message,e)
        
def Reports(message,name,id,country,flag,username,reply_message_id):
    global erorr_proxy , reports , not_send
    while True:
        headers = {
            "authority": "www.tiktok.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "referer": "https://www.tiktok.com/",
            "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }   
        try:
                proxy = random.choice(open("workProxy.txt", "r").read().splitlines())
                proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                response = requests.get(f"https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={id}&owner_id={id}&reason={random.randint(0, 12000)}",headers=headers,proxies=proxies,timeout=15)
                if "Thanks for your feedback" in response.text:
                    reports += 1
                else:
                    not_send += 1
        except:
                erorr_proxy += 1
                response = requests.get(f"https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={id}&owner_id={id}&reason={random.randint(0, 12000)}",headers=headers)
                if "Thanks for your feedback" in response.text:
                    reports += 1
                else:
                    not_send += 1    
        bot.edit_message_text(
        f"Name : {name}\nCountry : {country}\nFlag : {flag}",
        chat_id=message.chat.id,
        message_id=reply_message_id,
        reply_markup=report_buttons(username))       
#L7N

bot.polling()   