# - * - coding: utf-8 - * -

 

from linepy import *

from akad.ttypes import Message

from akad.ttypes import ContentType as Type

from datetime import datetime

from time import sleep

from bs4 import BeautifulSoup

from humanfriendly import format_timespan, format_size, format_number, format_length

import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse

from gtts import gTTS

#import html5lib, shutil

#import wikipedia, goslate

#import youtube_dl, pafy, asyncio

from multiprocessing import Pool, Process

from googletrans import Translator

# ===================================================== ============================= #

botStart = time.time ()

# ===================================================== ============================= #

#line = LINE ()

#line = LINE ("Email", "Passwd")

line = LINE ('')

line.log ("Auth Token:" + str (line.authToken))

line.log ("Timeline Token:" + str (line.tl.channelAccessToken))

 

#ki = LINE ()

# ki.log ("Auth Token:" + str (ki.authToken))

# ki.log ("Timeline Token:" + str (ki.tl.channelAccessToken))

 

#kk = LINE ()

# kk.log ("Auth Token:" + str (kk.authToken))

# kk.log ("Timeline Token:" + str (kk.tl.channelAccessToken))

 

#kc = LINE ()

# kc.log ("Auth Token:" + str (kc.authToken))

# kc.log ("Timeline Token:" + str (kc.tl.channelAccessToken))

 

#ks = LINE ()

# ks.log ("Auth Token:" + str (ks.authToken))

# ks.log ("Timeline Token:" + str (ks.tl.channelAccessToken))

print ("Login Succes")

 

lineMID = line.profile.mid

lineProfile = line.getProfile ()

lineSettings = line.getSettings ()

 

oepoll = OEPoll (line)

#call = Call (line)

readOpen = codecs.open ("read.json", "r", "utf-8")

settingsOpen = codecs.open ("temp.json", "r", "utf-8")

read = json.load (readOpen)

settings = json.load (settingsOpen)

Rfu = [line]

Exc = [line]

lineMID = line.getProfile (). mid

bot1 = line.getProfile (). mid

RfuBot = [lineMID]

Family = ["u010598af074d6d55419609ae63048a60", lineMID]

admin = "u010598af074d6d55419609ae63048a60"

admin = ['u010598af074d6d55419609ae63048a60', lineMID]

RfuFamily = RfuBot + Family

 

protectname = []

protecturl = []

protection = []

autocancel = {}

autoinvite = []

autoleaveroom = []

targets = []

# ===================================================== ============================= #

settings = {

    "contact": False,

    "timeline": False,

    "autoAdd": True,

    "autoJoin": False,

    'autoCancel': {"on": True, "members": 3},             

    "autoLeave": True,

    "autoRead": False,

    "leaveRoom": True,

    "Respontag": True,

    "detectMention": True,

    "checkSticker": False,

    "kickMention": False,

    "potoMention": True,

    "lang": "JP",

    "Wc": True,

    # "Lv": False,

    "blacklist": {},

    "winvite": False,

    "wblacklist": False,

    "dblacklist": False,

    "commentBlack": {},

    "wblack": False,

    "dblack": False,

    "clock": False,

    "cName": "",

    "cNames": "",

    "invite": {},

    "winvite": False,

    "pnharfbot": {},

    "pname": {},

    "pro_name": {},

    "man1": " Set text ",

    "man2": " Set text ",

    "man3": " Set text ",

    "message": " This account is protected by M. Bot Self. The system has automatically blocked you. \ nContact M at Em_club0075 ",

    "comment": "Thanks for add me",

    "userAgent": [

        "Mozilla / 5.0 (X11; U; Linux i586; de; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (X11; U; Linux amd64; rv: 5.0) Gecko / 20100101 Firefox / 5.0 (Debian)",

        "Mozilla / 5.0 (X11; U; Linux amd64; en-US; rv: 5.0) Gecko / 20110619 Firefox / 5.0",

        "Mozilla / 5.0 (X11; Linux) Gecko Firefox / 5.0",

        "Mozilla / 5.0 (X11; Linux x86_64; rv: 5.0) Gecko / 20100101 Firefox / 5.0 FirePHP / 0.5",

        "Mozilla / 5.0 (X11; Linux x86_64; rv: 5.0) Gecko / 20100101 Firefox / 5.0 Firefox / 5.0",

        "Mozilla / 5.0 (X11; Linux x86_64) Gecko Firefox / 5.0",

        "Mozilla / 5.0 (X11; Linux ppc; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (X11; Linux AMD64) Gecko Firefox / 5.0",

        "Mozilla / 5.0 (X11; FreeBSD amd64; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 6.2; WOW64; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 6.1; Win64; x64; rv: 5.0) Gecko / 20110619 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 6.1; Win64; x64; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 6.1; rv: 6.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 6.1.1; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 5.2; WOW64; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 5.1; U; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 5.1; rv: 2.0.1) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 5.0; WOW64; rv: 5.0) Gecko / 20100101 Firefox / 5.0",

        "Mozilla / 5.0 (Windows NT 5.0; rv: 5.0) Gecko / 20100101 Firefox / 5.0"

    ],

    "mimic": {

        "copy": False,

        "status": False,

        "target": {}

    }

}

 

RfuProtect = {

    "protect": False,

    "cancelprotect": False,

    "inviteprotect": False,

    "linkprotect": False,

    "Protectguest": False,

    "Protectjoin": False,

    "autoAdd": True,

}

 

Setmain = {

    "foto": {},

}

 

read = {

    "readPoint": {},

    "readMember": {},

    "readTime": {},

    "ROM": {}

}

 

myProfile = {

              "displayName": "",

              "statusMessage": "",

              "pictureStatus": ""

}

 

mimic = {

    "copy": False,

    "copy2": False,

    "status": False,

    "target": {}

    }

 

RfuCctv = {

    "cyduk": {},

    "point": {},

    "sidermem": {}

}

 

rfuSet = {

    'setTime': {},

    'ricoinvite': {},

    }

 

user1 = lineMID

user2 = ""

             

setTime = {}

setTime = rfuSet ['setTime']

 

contact = line.getProfile ()

backup = line.getProfile ()

backup.dispalyName = contact.displayName

backup.statusMessage = contact.statusMessage

backup.pictureStatus = contact.pictureStatus

 

mulai = time.time ()

dangerMessage = [" M, I'm sorry ", " Good luck ", " Life always has the next draw. ",". winebot ",". kickall "," mayhem "," kick on "," makasih: d ","! kickall "," nuke "," fly ",". ??? "," Kickall " , " Fly to the sky", "Kickword", "kickword", "! Kickword", "/ kickall"]

dangerMessage2 = [ " that will connect me dear M. 5555", " extra's ", " that's just me !! .. love em it's me ," " that's me, O and M wait. Listening "," Emma already "," I love M, I love you "," I like M, I love "," Love M? "," Do you miss M? "]

 

myProfile ["displayName"] = lineProfile.displayName

myProfile ["statusMessage"] = lineProfile.statusMessage

myProfile ["pictureStatus"] = lineProfile.pictureStatus

# ===================================================== ============================= #

# ===================================================== ============================= #

def Rapid1Say (mtosay):

    line.sendText (Rapid1To, mtosay)

 

def summon (to, nama):

    aa = ""

    bb = ""

    strt = int (14)

    akh = int (14)

    nm = nama

    for mm in nm:

      akh = akh + 2

      aa + = "" "{" S ":" "" + json.dumps (str (strt)) + "" "," E ":" "" "+ json.dumps (str (akh)) +" "" , "M": "" "+ json.dumps (mm) +"}, "" "

      strt = strt + 6

      akh = akh + 4

      bb + = "\ xe2 \ x95 \ xa0 @x \ n"

    aa = (aa [: int (len (aa) -1)])

    msg = Message ()

    msg.to = to

    msg.text = "\ xe2 \ x95 \ x94 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ n "+ bb +" \ xe2 \ x95 \ x9a \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 \ x90 \ xe2 \ x95 "

    msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + aa + ']}', 'EMTVER': '4'}

    print ("TAG ALL")

    try:

       line.sendMessage (msg)

    except Exception as error:

       print (error)

 

def restartBot ():

    print ("RESTART SERVER")

    time.sleep (3)

    python = sys.executable

    os.execl (python, python, * sys.argv)

 

def logError (text):

    line.log ("[ notification ]" + str (text))

    time_ = datetime.now ()

    with open ("errorLog.txt", "a") as error:

        error.write ("\ n [% s]% s"% (str (time), text))

 

def sendMessage (to, text, contentMetadata = {}, contentType = 0):

    mes = Message ()

    mes.to, mes.from_ = to, profile.mid

    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata

    if to not in messageReq:

        messageReq [to] = -1

    messageReq [to] + = 1

 

def sendMessageWithMention (to, lineMID):

    try:

        aa = '{"S": "0", "E": "3", "M":' + json.dumps (lineMID) + '}'

        text_ = '@x'

        line.sendMessage (to, text_, contentMetadata = {'MENTION': '{"MENTIONEES": [' + aa + ']}'}, contentType = 0)

    except Exception as error:

        logError (error)

 

def myhelp ():

    myHelp = "" "?? M. Bot Self??

?? statement = statement

?? statement 2 statement Shelbourne Hotel.

?? statement 3 statement TAC.

?? Instruction 4 = Setting Instruction

?? order 5 = search order

?? command 6 = group command

?? command 7 = imitation command

?? command 8 = invisibility command

?? ?? M. Bot Self???? "" "

    return myHelp

 

def listgrup ():

    listGrup = "" "Bot M. BotSelf?? configuration command

?? Open in ? Auto group entered

?? Close ? Close to Auto group

?? Open block ? Auto block

?? Close the block ? Turn off the auto block.

?? Open ? Open chat Total

?? Close ? Close Chat Total

?? Open to read ? Open to read Auto

?? Close read ? Close read auto

?? Open the tag ? Reply to the tag person

?? Close tag ? Close Reply to tag people

?? Open the tag 2 ? Send pictures of people who tag us

?? Close the tag 2 ? Close Send the picture of the person who is tag

?? open TAC 3 ? Reply sticker.

?? Open the shopper . ? Open the link watch.

?? Close the clock ? Close View the link in the link

?? Open to see readers ? Catch people secretly reading

?? Close. Read the reader. ? Close. Catch the secret reader.

?? Open data ? Open read Mid 

?? Close information ? Close Mid  reading

?? Open the link ? Open the post link

?? Close link ? Close. View post link.

?? Set in : ?? Set welcome message

?? Set out : ?? Set resignation message

?? Set the tag: ?? Set the message to the tag person.

?? Check in ?? Welcome check

?? Check out ?? Check to say goodbye to out

?? Check tag ?? Check tag text

?? Cancel invitation ?? Cancel all outstanding invitations

?? welcome   ON?? open to them.

?? Welcome   OFF?? Close with "".

    return listGrup

 

def socmedia ():

    socMedia = "" "?? the TAC M. BotSelf??.

? trademark @ ? ask people to remove the unit.

? mid @  ? down mid others.

? Name @ ? Sign other people

? Titus @ ? down Titus others.

? dyslexia @  ? into dyslexia others.

? Cover @ ? Cover other people's

? Video @ ? Download video cover for other people

? This copy @ ? also cover up other people.

? Info @  ? See other people's data

? Go @  ?, kick back.

? Kick @ ? Kick with the name tag

? nipples @  ? kick back chat

? Administrator @  ? Add admin

? Delete administrator @  ? Delete administrator

? flat @ ? track down black people "" ".

    return socMedia

 

def helpset ():

    helpSet = "" "Bot M. BotSelf???? command

?? M   ?? Contact M

?? Mid   ?? MID Us

?? Name   ?? Our name

?? Titus   ?? status we

?? Check   ?? Inspector

?? District   ? profile

?? Cover   ? Cover photo

?? Video   ? Video Profile

?? Back   ? Return the original body

?? synthase   ? testing bots.

?? All open   ? Open function

?? Completely closed.   ???closed listening

?? Speed   ? Speed ??test

?? Call   ? Call invitation

?? See time ?? Check date and time

?? Spam   ?? Virus release

?? Close bots ?? Close bots

?? Hurry up   ?? Lock in Bot?

?? on   ?? on bots.

?? Add   ?? Group admin

?? Bot ?? Bot   creator  information

?? / delete run   ?? delete run

?? through the   ?? creators of bots.

?? Friends   ?? List of our friends

?? shakes black   ?? check the next dive.

?? clear black   ?? clear the next black.

?? Name : Text   ? Change name

?? Titus : Text   ? change status "" ".

    return helpSet

 

def helpkicker ():

    helpKicker = "" "? BotSelf? M. Search Commands

?? Speak the message ? Order the Siri speak

???????Youtube message ? Search on YouTube

?? Write message ? Write

?? instagram ? Enter a name, search

?? Picture comes message ? Send image

?? cartoon text ? Down "" ".

    return helpKicker

 

def helpsetting ():

    helpSetting = "" "? command group M BotSelf?.

?? Group ? Group information

?? Group ID ? Room ID

?????Group name ????Room name

???????Message group name ? Change room name

?? group photo ? group photo

?? Home ? View group list

?? Members ? List of people in the room

?? Open the link ? Open the group link

?? Close the link ? Close the group link

?? Link ? Request to link to a group

?? MID Group ? Mid Watch Group 

?? Tag ? Tag people in the group

? Set time ? Set time

? Closing time ? Closing time

? Reset time ? Delete time for readers

? bo ? list that we block friends

?????? # Announcement : Message ? Send chat in every room "" "

    return helpSetting

 

def helptexttospeech ():

    helpTextToSpeech = "" " ????? Emulate M BotSelf? command

?? Imitating on / off

?? Imitation

?? Add copy (@)

?? Delete copy (()) "" "

    return helpTextToSpeech

 

def helplanguange ():

    helpLanguange = "" "????Invisible Command ??

??! Tack

??! Completely

??! The Apartment "" "

    return helpLanguange

# ===================================================== ============================= #

def lineBot (op):

    try:

                 

        if op.type == 5:

            if settings ["autoBlock"] == True:

                line.blockContact (op.param1)          

 

        if op.type == 13:

            if lineMID in op.param3:

                G = line.getGroup (op.param1)

                if settings ["autoJoin"] == True:

                    if settings ["autoCancel"] ["on"] == True:

                        if len (G.members) <= settings ["autoCancel"] ["members"]:

                            line.rejectGroupInvitation (op.param1)

                        else:

                            line.acceptGroupInvitation (op.param1)

                    else:

                        line.acceptGroupInvitation (op.param1)

                elif settings ["autoCancel"] ["on"] == True:

                    if len (G.members) <= settings ["autoCancel"] ["members"]:

                        line.rejectGroupInvitation (op.param1)

            else:

                Inviter = op.param3.replace (" - ", ',')

                InviterX = Inviter.split (",")

                matched_list = []

                for tag in settings ["blacklist"]:

                    matched_list + = [str for str in InviterX if str == tag]

                if matched_list == []:

                    pass

                else:

                    line.cancelGroupInvitation (op.param1, matched_list)                                                       

# if op.type == 13:

# group = line.getGroup (op.param1)

# if settings ["autoJoin"] == True:

# line.acceptGroupInvitation (op.param1)

# if op.type == 24:

# if settings ["autoLeave"] == True:

# line.leaveRoom (op.param1)

        if op.type == 24:

            print ("[24] The total chat is now ")

            if settings ["autoLeave"] == True:

                line.leaveRoom (op.param1)

        if op.type == 25:

            msg = op.message          

            if msg.contentType == 13:

                if settings ["contact"] == True:

                    # msg.contentType = 0

                    if 'displayName' in msg.contentMetadata:

                        contact = line.getContact (msg.contentMetadata ["mid"])

                        try:

                            cu = line.getProfileCoverURL (msg.contentMetadata ["mid"])

                        except:

                            cu = ""

                        line.sendMessage (msg.to, "[ name ]: \ n" + msg.contentMetadata ["displayName"] + "\ n [mid]: \ n" + msg.contentMetadata ["mid"] + "\ n [ Titus ]: \ n "+ contact.statusMessage + " \ n [ profile ]: \ nhttp: //dl.profile.line-cdn.net/ "+ contact.pictureStatus +" \ n [ cover ]: \ n. "+ str (cu))

                    else:

                        contact = line.getContact (msg.contentMetadata ["mid"])

                        try:

                            cu = line.getProfileCoverURL (msg.contentMetadata ["mid"])

                        except:

                            cu = ""

                        line.sendMessage (msg.to, "[ name ]: \ n" + contact.displayName + "\ n [mid]: \ n" + msg.contentMetadata ["mid"] + "\ n [ Virtus ]: \ n "+ contact.statusMessage +" \ n [ Profile ]: \ nhttp: //dl.profile.line-cdn.net/ "+ contact.pictureStatus +" \ n [ Cover ]: \ n "+ str (cu ))

        if op.type == 25:

            msg = op.message

            text = msg.text

            msg_id = msg.id

            receiver = msg.to

            sender = msg._from

            if msg.toType == 0:

                if sender! = line.profile.mid:

                    to = sender

                else:

                    to = receiver

            else:

                to = receiver

            if msg.contentType == 0:

                if text is None:

                    return

# ===================================================== ============================= #

 

                if " spam " in msg.text.lower ():

                    spl = re.split (" Spam ", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        mts = spl [1]

                        mtsl = mts.split ()

                        mtsTimeArg = len (mtsl) - 1

                        mtsTime = mtsl [mtsTimeArg]

                        del mtsl [mtsTimeArg]

                        mtosay = "" .join (mtsl)

                        global Rapid1To

                        Rapid1To = msg.to

                        RapidTime = mtsTime

                        rmtosay = []

                        for count in range (0, int (RapidTime)):

                            rmtosay.insert (count, mtosay)

                        p = Pool (20)

                        p.map (Rapid1Say, rmtosay)

                        p.close ()

                if text.lower () == ' command ':

                    myHelp = myhelp ()

                    line.sendMessage (to, str (myHelp))

                elif text.lower () == ' Command 2':

                    helpSet = helpset ()

                    line.sendMessage (to, str (helpSet))

                    sendMessageWithMention (to, lineMID)

                elif text.lower () == ' Command 3':

                    helpKicker = helpkicker ()

                    line.sendMessage (to, str (helpKicker))

                elif text.lower () == ' command 4':

                    listGrup = listgrup ()

                    line.sendMessage (to, str (listGrup))

                elif text.lower () == ' command 5':

                    helpSetting = helpsetting ()

                    line.sendMessage (to, str (helpSetting))

                elif text.lower () == ' Command 6':

                    socMedia = socmedia ()

                    line.sendMessage (to, str (socMedia))

                elif text.lower () == ' Command 7':

                    helpTextToSpeech = helptexttospeech ()

                    line.sendMessage (to, str (helpTextToSpeech))

                elif text.lower () == ' Command 8':

                    helpLanguange = helplanguange ()

                    line.sendMessage (to, str (helpLanguange))

# =============== Find a Lien Name ================================== ===================================== #

                elif text.lower () == '! Tack ':

                    gs = line.getGroup (to)

                    targets = []

                    for g in gs.members:

                        if g.displayName in "":

                            targets.append (g.mid)

                    if targets == []:

                        line.sendMessage (to, "?? No one is wearing a groove in this group ?")

                    else:

                        mc = ""

                        for target in targets:

                            mc + = sendMessageWithMention (to, target) + "\ n"

                        line.sendMessage (to, mc)

                elif text.lower () == '! Mid ':

                    gs = line.getGroup (to)

                    lists = []

                    for g in gs.members:

                        if g.displayName in "":

                            lists.append (g.mid)

                    if lists == []:

                        line.sendMessage (to, "?? doesn't have a MID ????. ")

                    else:

                        mc = ""

                        for mi_d in lists:

                            mc + = "->" + mi_d + "\ n"

                        line.sendMessage (to, mc)

                elif text.lower () == '! Oct ':

                    gs = line.getGroup (to)

                    lists = []

                    for g in gs.members:

                        if g.displayName in "":

                            lists.append (g.mid)

                    if lists == []:

                        line.sendMessage (to, "?? No one is wearing a groove in this group ?")

                    else:

                        for ls in lists:

                            contact = line.getContact (ls)

                            mi_d = contact.mid

                            line.sendContact (to, mi_d)

                elif msg.text.lower (). startswith (" speak "):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'th'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

                elif " group name " in msg.text:

                    if msg.toType == 2:

                        X = line.getGroup (msg.to)

                        X.name = msg.text.replace (" Group name ", "")

                        line.updateGroup (X)

                    else:

                        line.sendMessage (msg.to, " Cannot be used outside of group ")

                elif "# announcement :" in msg.text:

                    bctxt = text.replace ("# Announcement :", "")

                    n = line.getGroupIdsJoined ()

                    for manusia in n:

                        line.sendMessage (manusia, (bctxt))

                elif text.lower (). startswith ('op'):

                        MENTION = eval (msg.contentMetadata ['MENTION'])

                        inkey = MENTION ['MENTIONEES'] [0] ['M']

                        admin.append (str (inkey))

                        line.sendMessage (to, " add ?privileges ")

                elif text.lower (). startswith ('deop'):

                        MENTION = eval (msg.contentMetadata ['MENTION'])

                        inkey = MENTION ['MENTIONEES'] [0] ['M']

                        admin.remove (str (inkey))

                        line.sendMessage (to, " privilege deleted ?")

                elif text.lower () == 'oplist':

                    if admin == []:

                        line.sendMessage (to, " no power ")

                    else:

                        line.sendMessage (to, "The following is an inspector ")

                        mc = ""

                        for mi_d in admin:

                            mc + = " ? " + line.getContact (mi_d) .displayName + "\ n"

                        line.sendMessage (to, mc)             

                elif text.lower () == '. Taste '.

                    ki.sendMessage (to, " M. BotSelf is still here ")

                elif text.lower () == ' Taste '.

                    line.sendMessage (to, " M. BotSelf Loading : ? ... 0%")

                    line.sendMessage (to, "?? ... 10.0%")

                    line.sendMessage (to, "??? ... 20.0%")

                    line.sendMessage (to, "???? ... 30.0%")

                    line.sendMessage (to, "????? ... 40.0%")

                    line.sendMessage (to, "?????? ... 50.0%")

                    line.sendMessage (to, "??????? ... 60.0%")

                    line.sendMessage (to, "??????? ... 70.0%")

                    line.sendMessage (to, "????????? ... 80.0%")

                    line.sendMessage (to, "?????????? ... 90.0%")

                    line.sendMessage (to, "???????????..100.0%")

                    line.sendMessage (to, "?? M. BotSelf is still ? ")

                elif msg.text.lower () == ". On ".

                    line.sendMessage (msg.to, (str (datetime.datetime.now () - start_runtime) [: - 7] .split ("days,") [0] + " date " + str (datetime.datetime.now ( ) - start_runtime) [: - 7] .split ("days,") [1] .split (":") [0] + " hours " if "days" in str (datetime.datetime.now () - start_runtime ) else str (datetime.datetime.now () - start_runtime) [: - 7] .split ("day,") [0] + " date " + str (datetime.datetime.now () - start_runtime) [: - 7] .split ("day,") [1] .split (":") [0] + " hour " if "day" in str (datetime.datetime.now () - start_runtime) else str (datetime.datetime .now () - start_runtime) [: - 7] .split (":") [0] + " hour ") + str (datetime.datetime.now () - start_runtime) [: - 7] .split (": ") [1] +" minutes "+ str (datetime.datetime.now () - start_runtime) [: - 7] .split (": ") [2] +" seconds ")              

                elif " trademark " in msg.text:.

                    mmid = msg.text.replace ( " the North ", "").

                    line.sendContact (to, mmid)

                elif " stopper :" in text:

                    midd = msg.text.replace (" Stopper :", "")

                    line.kickoutFromGroup (msg.to, [midd])

                    line.findAndAddContactsByMid (midd)

                    line.inviteIntoGroup (msg.to, [midd])

                    line.cancelGroupInvitation (msg.to, [midd])

                elif " pacifier " in msg.text:

                        vkick0 = msg.text.replace (" Cork ", "")

                        vkick1 = vkick0.rstrip ()

                        vkick2 = vkick1.replace ("@", "")

                        vkick3 = vkick2.rstrip ()

                        _name = vkick3

                        gs = line.getGroup (msg.to)

                        targets = []

                        for s in gs.members:

                            if _name in s.displayName:

                                targets.append (s.mid)

                        if targets == []:

                            pass

                        else:

                            for target in targets:

                                try:

                                    line.kickoutFromGroup (msg.to, [target])

                                    line.findAndAddContactsByMid (target)

                                    line.inviteIntoGroup (msg.to, [target])

                                    line.cancelGroupInvitation (msg.to, [target])

                                except:

                                    pass

                elif " go " in msg.text:

                    Ri0 = text.replace (" Go ", "")

                    Ri1 = Ri0.rstrip ()

                    Ri2 = Ri1.replace ("@", "")

                    Ri3 = Ri2.rstrip ()

                    _name = Ri3

                    gs = line.getGroup (msg.to)

                    targets = []

                    for s in gs.members:

                        if _name in s.displayName:

                            targets.append (s.mid)

                    if targets == []:

                        pass

                    else:

                        for target in targets:

                            if target in admin:

                                pass

                            else:

                                try:

                                    line.kickoutFromGroup (to, [target])

                                    line.findAndAddContactsByMid (target)

                                    line.inviteIntoGroup (to, [target])

                                except:

                                    pass

                elif " go :" in msg.text:

                    midd = text.replace (" Go :", "")

                    line.kickoutFromGroup (to, [midd])

                    line.findAndAddContactsByMid (midd)

                    line.inviteIntoGroup (to, [midd])

                elif msg.text.lower () == "speed":

                    start = time.time ()

                    line.sendMessage (msg.to, " speed is at ")

                    line.sendMessage (msg.to, str (int (round ((time.time () - start) * 1000))) + + "ms")

                elif ' come dick ' in text.lower ():

                    if msg.toType == 2:

                        G = line.getGroup (to)

                        if G.preventedJoinByTicket == False:

                            line.updateGroup (G)

                            invsend = 0

                            Ti = line.reissueGroupTicket (to)

                            ki.acceptGroupInvitationByTicket (to, Ti)

                            kk.acceptGroupInvitationByTicket (to, Ti)

                            kc.acceptGroupInvitationByTicket (to, Ti)

                            G.preventedJoinByTicket = True

                            line.updateGroup (G)

                        else:

                            G.preventedJoinByTicket = False

                            line.updateGroup (G)

                            invsend = 0

                            Ti = line.reissueGroupTicket (to)

                            ki.acceptGroupInvitationByTicket (to, Ti)

                            kk.acceptGroupInvitationByTicket (to, Ti)

                            kc.acceptGroupInvitationByTicket (to, Ti)

                            G.preventedJoinByTicket = True

                            line.updateGroup (G)

                elif text.lower () == ' Go ':

                    if msg.toType == 2:

                        ginfo = line.getGroup (to)

                        try:

                            ki.leaveGroup (to)

                            kc.leaveGroup (to)

                            kk.leaveGroup (to)

                        except:

                            pass

                elif text.lower () == ' Speed ':

                    start = time.time ()

                    line.sendMessage (to, "The Speed ??of M Bot Self ...")

                    elapsed_time = time.time () - start

                    line.sendMessage (to, format (str (elapsed_time)))             

                elif text.lower () == ' Dash ':

                    line.sendMessage (to, " Starting over ... please wait ...")

                    line.sendMessage (to, " Bot has logged in again ....")

                    restartBot ()

                elif text.lower () == ' Online ':

                    timeNow = time.time ()

                    runtime = timeNow - botStart

                    runtime = format_timespan (runtime)

                    line.sendMessage (to, "? M. Bot Self? \ n" " The duration of the bot. {} ". format (str (runtime)))

                elif text.lower () == ' Bots ':

                    try:

                        arr = []

                        owner = "u010598af074d6d55419609ae63048a60"

                        creator = line.getContact (owner)

                        contact = line.getContact (lineMID)

                        grouplist = line.getGroupIdsJoined ()

                        contactlist = line.getAllContactIds ()

                        blockedlist = line.getBlockedContactIds ()

                        ret_ = "??? [  M. Bot Self]"

                        ret_ + = "\ n???? Name ? {}". format (contact.displayName)

                        ret_ + = "\ n???? group ? {}". format (str (len (grouplist)))

                        ret_ + = "\ n???? Friend ? {}". format (str (len (contactlist)))

                        ret_ + = "\ n???? Block ? {}". format (str (len (blockedlist)))

                        ret_ + = "\ n??? [ status ]"

                        ret_ + = "\ n???? Creator ? {}". format (creator.displayName)

                        ret_ + = "\ n??? [  M Bot Self]"

                        line.sendContact (to, owner)

                        line.sendMessage (to, str (ret_))

                    except Exception as e:

                        line.sendMessage (msg.to, str (e))

# ===================================================== ============================= #

                elif text.lower () == ' Status ':

                    try:

                        ret_ = "????? [  M Bot Self Status ] ????? ? "

                        if settings [" Bots work normally "] == True: ret_ + = "\ n? ?? Get Auto Block ? "

                        else: ret_ + = "\ n??? Get Auto Block ? "   

                        if settings ["autoJoin"] == True: ret_ + = "\ n? ?? Auto room ? "

                        else: ret_ + = "\ n??? Enter the auto room ? "   

                        if settings ["contact"] == True: ret_ + = "\ n? ?? Check Mid ? "

                        else: ret_ + = "\ n??? check , Mid ? ".

                        if settings ["autoCancel"] ["on"] == True: ret _ + = "\ n? ?? Uninvite the group when there are less members :" + str (settings ["autoCancel"] ["members"]) + "? ? "

                        else: ret_ + = "\ n??? cancel the invitation ? ".                                                                                       

                        if settings ["autoLeave"] == True: ret_ + = "\ n? ?? Total Chat ? "

                        else: ret_ + = "\ n??? out chat as well ? ".

                        if settings ["autoRead"] == True: ret_ + = "\ n? ?? Auto read ? "

                        else: ret_ + = "\ n??? Auto read ? "                                                          

                        Settings the if [ "CheckSticker"] == a True: Ret_ +, = "\ N? ?? shakes mark ? ".

                        else: ret_ + = "\ n??? shakes mark ? ".       

                        if settings ["Wc"] == True: ret_ + = "\ n? ?? Welcome people ? "

                        else: ret_ + = "\ n??? When accepting people ? "

                        if settings ["Wc"] == True: ret_ + = "\ n? ?? Messages issued by people ? "

                        else: ret_ + = "\ n??? text issued ? " 

                        if settings ["timeline"] == True: ret_ + = "\ n? ?? Share link ? "

                        else: ret_ + = "\ n??? Link sharing ? "   

                        if settings ["detectMention"] == True: ret_ + = "\ n? ?? Reply to tag people ? "

                        else: ret_ + = "\ n??? Reply to tag people ? "

                        if settings ["potoMention"] == True: ret_ + = "\ n? ?? Show people photos ? "

                        else: ret_ + = "\ n??? Show people photos ? "

                        if settings ["detectMention"] == True: ret_ + = "\ n? ?? Show tick box ? "

                        else: ret_ + = "\ n??? Show tag people ? "

                        ret_ + = "\ n????? [ M Bot Self Status ] ????? ? "

                        line.sendMessage (to, str (ret_))

                    except Exception as e:

                        line.sendMessage (msg.to, str (e))

                elif text.lower () == ' Open ad ':

                    settings ["autoAdd"] = True

                    line.sendMessage (to, " Open !!")

                elif text.lower () == ' Close ad ':

                    settings ["autoAdd"] = False

                    line.sendMessage (to, " Closed !!")

                elif text.lower () == ' Open block ':

                    settings ["autoBlock"] = True

                    line.sendMessage (to, " Auto block enabled .")

                elif text.lower () == ' Close block ':

                    settings ["autoBlock"] = False

                    line.sendMessage (to, " Auto Block disabled ")

                elif text.lower () == ' Open sharing link ':

                    settings ["timeline"] = True

                    line.sendMessage (to, " Shared link ."

                elif text.lower () == ' Close link ':

                    settings ["timeline"] = False

                    line.sendMessage (to, "The link has been closed .")

                elif text.lower () == ' Open in ':

                    settings ["autoJoin"] = True

                    line.sendMessage (to, " Opened to Auto Group .")

                elif text.lower () == ' Close in ':

                    settings ["autoJoin"] = False

                    line.sendMessage (to, " Auto group closed .")

                elif "Gcancel:" in msg.text:

                    try:

                        strnum = msg.text.replace ("Gcancel:", "")

                        if strnum == "off":

                                settings ["autoCancel"] ["on"] = False

                                if settings ["lang"] == "JP":

                                    line.sendText (msg.to, "Invitation refused turned off \ nTo turn on please specify the number of people and send")

                                else:

                                    line.sendText (msg.to, " The invitation has been rejected. If you want to open, please send the number of people specified. ")

                        else:

                                num = int (strnum)

                                settings ["autoCancel"] ["on"] = True

                                if settings ["lang"] == "JP":

                                    line.sendText (msg.to, strnum + " Group members will automatically decline invitations ")

                                else:

                                    line.sendText (msg.to, strnum + " Decline the following group with automatic invitations ")

                    except:

                        if settings ["lang"] == "JP":

                                line.sendText (msg.to, "Value is wrong")

                        else:

                                line.sendText (msg.to, "Bizarre ratings")

                elif text.lower () == ' Open Data ':

                    settings ["contact"] = True

                    line.sendMessage (to, " Shake Mid with the trademark was already open ").

                elif text.lower () == ' Close Data ':

                    settings ["contact"] = False

                    line.sendMessage (to, " Shake Mid with the trademark has been closed .")

                elif text.lower () == ' Open Tag 3':

                    settings ["Respontag"] = True

                    line.sendMessage (to, " Reply with open tag ")

                elif text.lower () == ' Close Tag 3':

                    settings ["Respontag"] = False

                    line.sendMessage (to, " reply with closed tick box ")                                                                      

                elif text.lower () == ' Open out ':

                    settings ["autoLeave"] = True

                    line.sendMessage (to, " Open chat included .")

                elif text.lower () == ' Close out ':

                    settings ["autoLeave"] = False

                    line.sendMessage (to, " Chat has been closed .")

                elif text.lower () == ' Open read ':

                    settings ["autoRead"] = True

                    line.sendMessage (to, " read already .")

                elif text.lower () == ' Close read ':

                    settings ["autoRead"] = False

                    line.sendMessage (to, " read closed .")

                elif text.lower () == ' Open shaker ':

                    settings ["checkSticker"] = True

                    line.sendMessage (to, "Shakes open .")

                elif text.lower () == ' Shake off ':

                    settings ["checkSticker"] = False

                    line.sendMessage (to, "Shaker is closed .")

                elif " set in :" in msg.text:

                    settings ["man1"] = msg.text.replace (" Enter :", "")

                    line.sendText (msg.to, " ? Success Welcome Set ")

                elif " set it off :" in msg.text:

                    settings ["man2"] = msg.text.replace (" Set out :", "")

                    line.sendText (msg.to, " ? Set the message to mention the successful person ")

                elif " set the tag:" in msg.text:

                    settings ["man3"] = msg.text.replace (" Tag Settings :", "")

                    line.sendText (msg.to, " ? set the message to mention the successful tag ")

                elif msg.text in [ " Shake to ", " check "].

                    line.sendText (msg.to, "The latest welcome message is \ n \ n" + str (settings ["man1"])))

                elif msg.text in [ " check it out ", " check it out "]:

                    line.sendText (msg.to, " The most recent message is \ n \ n" + str (settings ["man2"]))

                elif msg.text in [ " Shake TAC ", " check-TAC "].

                    line.sendText (msg.to, "The message mentions the most recent tag is \ n \ n" + str (settings ["man3"]))   

                elif text.lower () == 'kt on':

                    settings ["kickMention"] = True

                    line.sendMessage (to, "?? Open system, kicking people, tacking ??")

                elif text.lower () == 'kt off':

                    settings ["kickMention"] = False

                    line.sendMessage (to, "?? off system, kicking, tacking people ")    

                elif text.lower () == ' Change disk ':

                     settings ["changePictureProfile"] = True

                     line.sendMessage (to, "?? send the image to ??")

                elif text.lower () == ' Change group ':

                     settings ["changeGroupPicture"] = True

                     line.sendMessage (to, "?? send the image to ??")     

# ===================================================== ============================= #

 

                elif text.lower () == ' M ':

                    sendMessageWithMention (to, lineMID)

                    line.sendContact (to, lineMID)

                elif text.lower () == ' ?':

                    sendMessageWithMention (to, lineMID)

                    line.sendContact (to, "u010598af074d6d55419609ae63048a60")

                elif text.lower () == ' Mid ':

                    line.sendMessage (msg.to, "[MID] \ n" + lineMID)

                elif text.lower () == ' Name ':

                    me = line.getContact (lineMID)

                    line.sendMessage (msg.to, "[ display name ] \ n" + me.displayName)

                elif text.lower () == ' Virtus ':

                    me = line.getContact (lineMID)

                    line.sendMessage (msg.to, "[ displayed status ] \ n" + me.statusMessage)

# Elif text.lower () == ' dyslexia '.

# me = line.getContact (lineMID)

# line.sendImageWithURL (msg.to, "http://dl.profile.line-cdn.net/" + me.pictureStatus)

                elif text.lower () == ' Video ':

                    me = line.getContact (lineMID)

                    line.sendVideoWithURL (msg.to, "http://dl.profile.line-cdn.net/" + me.pictureStatus + "/ vp")

                elif text.lower () == ' Cover ':

                    me = line.getContact (lineMID)

                    cover = line.getProfileCoverURL (lineMID)   

                    line.sendImageWithURL (msg.to, cover)

                elif msg.text.lower (). startswith ( " the North ").

                    if 'MENTION' in msg.contentMetadata.keys ()! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        for ls in lists:

                            contact = line.getContact (ls)

                            mi_d = contact.mid

                            line.sendContact (msg.to, mi_d)

                elif msg.text.lower (). startswith (" Mid "):

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        ret_ = "[ Mid ]"

                        for ls in lists:

                            ret_ + = "\ n {}" + ls

                        line.sendMessage (msg.to, str (ret_))

                elif msg.text.lower (). startswith (" Name "):

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        for ls in lists:

                            contact = line.getContact (ls)

                            line.sendMessage (msg.to, "[ display name ] \ n" + contact.displayName)

                elif msg.text.lower (). startswith (" Virtus "):

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        for ls in lists:

                            contact = line.getContact (ls)

                            line.sendMessage (msg.to, "[ status set ] \ n {}" + contact.statusMessage)

                elif msg.text.lower (). startswith ( " Discovery ").

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        for ls in lists:

                            path = "http://dl.profile.line.naver.jp/" + line.getContact (ls) .pictureStatus

                            line.sendImageWithURL (msg.to, str (path))

                elif msg.text.lower (). startswith (" Video "):

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        lists = []

                        for mention in mentionees:

                            if mention ["M"] not in lists:

                                lists.append (mention ["M"])

                        for ls in lists:

                            path = "http://dl.profile.line.naver.jp/" + line.getContact (ls) .pictureStatus + "/ vp"

                            line.sendImageWithURL (msg.to, str (path))

                elif msg.text.lower (). startswith (" cover "):

                    if line! = None:

                        if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                            names = re.findall (r '@ (\ w +)', text)

                            mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                            mentionees = mention ['MENTIONEES']

                            lists = []

                            for mention in mentionees:

                                if mention ["M"] not in lists:

                                    lists.append (mention ["M"])

                            for ls in lists:

                                path = line.getProfileCoverURL (ls)

                                line.sendImageWithURL (msg.to, str (path))

                elif msg.text.lower (). startswith ( " I Hop ").

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        names = re.findall (r '@ (\ w +)', text)

                        mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                        mentionees = mention ['MENTIONEES']

                        for mention in mentionees:

                            contact = mention ["M"]

                            break

                        try:

                            line.cloneContactProfile (contact)

                            line.sendMessage (msg.to, "????")

                        except:

                            line.sendMessage (msg.to, "????")

 

                elif text.lower () == ' Return ':

                    try:

                        lineProfile.displayName = str (myProfile ["displayName"])

                        lineProfile.statusMessage = str (myProfile ["statusMessage"])

                        lineProfile.pictureStatus = str (myProfile ["pictureStatus"])

                        line.updateProfileAttribute (8, lineProfile.pictureStatus)

                        line.updateProfile (lineProfile)

                        line.sendMessage (msg.to, " Successfully returned to original body ")

                    except:

                        line.sendMessage (msg.to, "Invert the original body ")

                                                                                   

# ===================================================== ============================= #

 

                elif msg.text.lower (). startswith (" add imitation "):

                    targets = []

                    key = eval (msg.contentMetadata ["MENTION"])

                    key ["MENTIONEES"] [0] ["M"]

                    for x in key ["MENTIONEES"]:

                        targets.append (x ["M"])

                    for target in targets:

                        try:

                            settings ["mimic"] ["target"] [target] = True

                            line.sendMessage (msg.to, " imitating this person ")

                            break

                        except:

                            line.sendMessage (msg.to, "Added Target Fail!")

                            break

                elif msg.text.lower (). startswith (" remove impersonation "):

                    targets = []

                    key = eval (msg.contentMetadata ["MENTION"])

                    key ["MENTIONEES"] [0] ["M"]

                    for x in key ["MENTIONEES"]:

                        targets.append (x ["M"])

                    for target in targets:

                        try:

                            del settings ["mimic"] ["target"] [target]

                            line.sendMessage (msg.to, " Delete this copy ")

                            break

                        except:

                            line.sendMessage (msg.to, "Deleted Target Fail!")

                            break

                elif text.lower () == ' Imitate ':

                    if settings ["mimic"] ["target"] == {}:

                        line.sendMessage (msg.to, " Open system with ??")

                    else:

                        mc = "??? [ number of people imitated ]"

                        for mi_d in settings ["mimic"] ["target"]:

                            mc + = "\ n?" + line.getContact (mi_d) .displayName

                        line.sendMessage (msg.to, mc + "\ n??? [ completed ]")

 

                elif " imitate " in msg.text.lower ():

                    sep = text.split ("")

                    mic = text.replace (sep [0] + "", "")

                    if mic == "on":

                        if settings ["mimic"] ["status"] == False:

                            settings ["mimic"] ["status"] = True

                            line.sendMessage (msg.to, " The imitation system is enabled ")

                    elif mic == "off":

                        if settings ["mimic"] ["status"] == True:

                            settings ["mimic"] ["status"] = False

                            line.sendMessage (msg.to, " The imitation system is closed ")

# ===================================================== ============================= #

                elif text.lower () == ' Add ':

                    group = line.getGroup (to)

                    GS = group.creator.mid

                    line.sendContact (to, GS)

                    line.sendMessage (to, " He is the creator of this group ")

                elif text.lower () == ' Group ID ':

                    gid = line.getGroup (to)

                    line.sendMessage (to, " group ID \ n" + gid.id)

                elif text.lower () == ' Group image ':

                    group = line.getGroup (to)

                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus

                    line.sendImageWithURL (to, path)

                elif text.lower () == ' Group name ':

                    gid = line.getGroup (to)

                    line.sendMessage (to, " group name -> \ n" + gid.name)

                elif text.lower () == ' Link ':

                    if msg.toType == 2:

                        group = line.getGroup (to)

                        if group.preventedJoinByTicket == False:

                            ticket = line.reissueGroupTicket (to)

                            line.sendMessage (to, " Group link, click this link \ nhttps: //line.me/R/ti/g/ {}" .format (str (ticket)))

                elif text.lower () == ' Open link ':

                    if msg.toType == 2:

                        group = line.getGroup (to)

                        if group.preventedJoinByTicket == False:

                            line.sendMessage (to, " Invited with QR code ")

                        else:

                            group.preventedJoinByTicket = False

                            line.updateGroup (group)

                            line.sendMessage (to, " Invited with QR code ")

                elif text.lower () == ' Close link ':

                    if msg.toType == 2:

                        group = line.getGroup (to)

                        if group.preventedJoinByTicket == True:

                            line.sendMessage (to, " Invited off with QR code ")

                        else:

                            group.preventedJoinByTicket = True

                            line.updateGroup (group)

                            line.sendMessage (to, " Invited with QR code ")

                elif text.lower () == ' Group ':

                    group = line.getGroup (to)

                    try:

                        gCreator = group.creator.displayName

                    except:

                        gCreator = " General "

                    if group.invitee is None:

                        gPending = "0"

                    else:

                        gPending = str (len (group.invitee))

                    if group.preventedJoinByTicket == True:

                        gQr = " Close "

                        gTicket = " Data not found "

                    else:

                        gQr = "Terbuka"

                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))

                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus

                    ret_ = "??? [ group info ]"

                    ret_ + = "\ n? Group name : {}". format (str (group.name))

                    ret_ + = "\ n? MID group : {}". format (group.id)

                    ret_ + = "\ n? Group type : {}". format (str (gCreator))

                    ret_ + = "\ n? Number of members : {}". format (str (len (group.members)))

                    ret_ + = "\ n? Number of pending members : {}". format (gPending)

                    ret_ + = "\ n? Qr group : {}". format (gQr)

                    ret_ + = "\ n? Group link : {}". format (gTicket)

                    ret_ + = "\ n??? [ Done ]

                    line.sendMessage (to, str (ret_))

                    line.sendImageWithURL (to, path)

                elif text.lower () == ' Members ':

                    if msg.toType == 2:

                        group = line.getGroup (to)

                        ret_ = "??? [ group member ]"

                        no = 0 + 1

                        for mem in group.members:

                            ret_ + = "\ n? {}. {}". format (str (no), str (mem.displayName))

                            no + = 1

                        ret_ + = "\ n??? [ amount {}]". format (str (len (group.members))))

                        line.sendMessage (to, str (ret_))

                elif text.lower () == ' House ':

                        groups = line.groups

                        ret_ = "??? [ all groups ]"

                        no = 0 + 1

                        for gid in groups:

                            group = line.getGroup (gid)

                            ret_ + = "\ n? {}. {} | {}". format (str (no), str (group.name), str (len (group.members)))

                            no + = 1

                        ret_ + = "\ n??? [ number { group } ]". format (str (len (groups)))

                        line.sendMessage (to, str (ret_))

                elif "! Taste : "in msg.text.lower ():.

                    settings ['spamtext'] = msg.text.replace ("! setspamtext:", "")

                    line.sendMessage (msg.to, " successful setup ")

 

                elif "! Tess "in msg.text.lower ():.

                    if LINE! = None:

                         spl = re.split ( " Tess ", msg.text, flags = re.IGNORECASE) .

                         if spl [0] == "":

                             prov = eval (msg.contentMetadata ["MENTION"]) ["MENTIONEES"]

                             for i in range (len (prov)):

                                 uid = prov [i] ["M"]

                                 userData = line.getContact (uid)

                                 line.sendMessage (userData.mid, settings ['spamtext'])

                             line.sendMessage (msg.to, " successful ")

                elif ". Call " in msg.text.lower ():

                            if msg.toType == 2:

                                sep = text.split ("")

                                strnum = text.replace (sep [0] + "", "")

                                num = int (strnum)

                                line.sendMessage (to, " The call has been successfully joined. ")

                                for var in range (0, num):

                                    group = line.getGroup (to)

                                    members = [mem.mid for mem in group.members]

                                    line.acquireGroupCallRoute (to)

                                    line.inviteIntoGroupCall (to, contactIds = members)                                         

                elif msg.text.lower (). startswith (" speak "):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'th'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

                elif " call " == msg.text.lower ():

                    line.inviteIntoGroupCall (msg.to, [uid.mid for uid in line.getGroup (msg.to) .members if uid.mid! = line.getProfile (). mid])

                    line.sendMessage (msg.to, " The call has been successfully invited. ")             

                elif text.lower () == ' Tag ':

                            if msg.toType == 0:

                                sendMention (to, to, "", "")

                            elif msg.toType == 2:

                                group = line.getGroup (to)

                                contact = [mem.mid for mem in group.members]

                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len (contact)

                                if jml <= 100:

                                    mentionMembers (to, contact)

                                elif jml> 100 and jml <= 200:

                                    for a in range (0, 99):

                                        ct1 + = [contact [a]]

                                    for b in range (100, jml):

                                        ct2 + = [contact [b]]

                                    mentionMembers (to, ct1)

                                    mentionMembers (to, ct2)

                                elif jml> 200 and jml <= 300:

                                    for a in range (0, 99):

                                        ct1 + = [contact [a]]

                                    for b in range (100, 199):

                                        ct2 + = [contact [b]]

                                    for c in range (200, jml):

                                        ct3 + = [contact [c]]

                                    mentionMembers (to, ct1)

                                    mentionMembers (to, ct2)

                                    mentionMembers (to, ct3)

                                elif jml> 300 and jml <= 400:

                                    for a in range (0, 99):

                                        ct1 + = [contact [a]]

                                    for b in range (100, 199):

                                        ct2 + = [contact [b]]

                                    for c in range (200, 299):

                                        ct3 + = [contact [c]]

                                    for d in range (300, jml):

                                        ct4 + = [contact [d]]

                                    mentionMembers (to, ct1)

                                    mentionMembers (to, ct2)

                                    mentionMembers (to, ct3)

                                    mentionMembers (to, ct4)

                                elif jml> 400 and jml <= 500:

                                    for a in range (0, 99):

                                        ct1 + = [contact [a]]

                                    for b in range (100, 199):

                                        ct2 + = [contact [b]]

                                    for c in range (200, 299):

                                        ct3 + = [contact [c]]

                                    for d in range (300, 399):

                                        ct4 + = [contact [d]]

                                    for e in range (400, jml):

                                        ct4 + = [contact [e]]

                                    mentionMembers (to, ct1)

                                    mentionMembers (to, ct2)

                                    mentionMembers (to, ct3)

                                    mentionMembers (to, ct4)

                                    mentionMembers (to, ct5)

                elif ".sh" in msg.text.lower ():

                    spl = re.split (". sh", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        try:

                            line.sendText (msg.to, subprocess.getoutput (spl [1]))

                        except:

                            pass             

                elif msg.text.lower () == "MID GROUP ":

                    line.sendText (msg.to, " Please calm down ").

                    all = line.getGroupIdsJoined ()

                    text = ""

                    cnt = 0

                    for i in all:

                        text + = line.getGroup (i) .name + "\ n" + i + "\ n \ n"

                        cnt + = 1

                        if cnt == 10:

                            line.sendText (msg.to, text [: - 2])

                            text = ""

                            cnt = 0

                    line.sendText (msg.to, text [: - 2])

                    cnt = 0

                elif " info " in msg.text.lower ():

                    spl = re.split (" data ", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        prov = eval (msg.contentMetadata ["MENTION"]) ["MENTIONEES"]

                        for i in range (len (prov)):

                            uid = prov [i] ["M"]

                            userData = line.getContact (uid)

                            try:

                                line.sendImageWithURL (msg.to, "http://dl.profile.line.naver.jp/" + userData.pictureStatus)

                                line.getProfileCoverURL

                            except:

                                pass

                            line.sendMessage (msg.to, " Display Name :" + userData.displayName)

                            line.sendMessage (msg.to, " status : \ n" + userData.statusMessage).

                            line.sendMessage (msg.to, " ID :" + userData.mid)

                            msg.contentType = 13

                            msg.text = None

                            msg.contentMetadata = {'mid': userData.mid}

                            line.sendMessage (msg.to, text = None, contentMetadata = {'mid': userData.mid}, contentType = 13)

                elif "l" in msg.text:

                    spl = msg.text.split ("l")

                    if spl [len (spl) -1] == "":

                        line.sendText (msg.to, " Click here to shake the text above. : \ nline: // nv / chatMsg? chatId = "+ msg.to +" & messageId = "+ msg.id)             

                elif " invite invitations " in msg.text.lower ():

                    spl = re.split (" Invitation raised ", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        spl [1] = spl [1] .strip ()

                        ag = line.getGroupIdsInvited ()

                        txt = " Canceling outstanding inviting amount "+ str (len (ag)) +" group "

                        if spl [1]! = "":

                            txt = txt + " with the text \" "+ spl [1] +" \ ""

                        txt = txt + "\ nPlease wait .."

                        line.sendText (msg.to, txt)

                        procLock = len (ag)

                        for gr in ag:

                            try:

                                line.acceptGroupInvitation (gr)

                                if spl [1]! = "":

                                    line.sendText (gr, spl [1])

                                line.leaveGroup (gr)

                            except:

                                pass

                        line.sendText (msg.to, " successful ")             

                elif ".whois" in msg.text.lower ():

                    spl = re.split (". whois", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        msg.contentType = 13

                        msg.text = None

                        msg.contentMetadata = {"mid": spl [1]}

                        line.sendMessage (msg)

                elif ".remove" in msg.text.lower ():

                    if msg.toType == 2:

                        prov = eval (msg.contentMetadata ["MENTION"]) ["MENTIONEES"]

                        for i in range (len (prov)):

                            random.choice (Exc) .kickoutFromGroup (msg.to, [prov [i] ["M"]])

                elif ".bye" in msg.text.lower ():

                    if msg.toType == 2:

                        prov = eval (msg.contentMetadata ["MENTION"]) ["MENTIONEES"]

                        allmid = []

                        for i in range (len (prov)):

                            line.kickoutFromGroup (msg.to, [prov [i] ["M"]])

                            allmid.append (prov [i] ["M"])

                        line.findAndAddContactsByMids (allmid)

                        line.inviteIntoGroup (msg.to, allmid)

                        line.cancelGroupInvitation (msg.to, allmid)

 

                elif msg.text.lower () == ".myid":

                    line.sendText (msg.to, user1)

                elif msg.text.lower (). startswith (". mentionall"):

                    data = msg.text [len (". mentionall"):]. strip ()

                    if data == "":

                        group = line.getGroup (msg.to)

                        nama = [contact.mid for contact in group.members if contact.mid! = user1]

                        cb = ""

                        cb2 = ""

                        count = 1

                        strt = len (str (count)) + 2

                        akh = int (0)

                        cnt = 0

                        for md in nama:

                            akh = akh + len (str (count)) + 2 + 5

                            cb + = "" "{" S ":" "" + json.dumps (str (strt)) + "" "," E ":" "" "+ json.dumps (str (akh)) +" "" , "M": "" "+ json.dumps (md) +"}, "" "

                            strt = strt + len (str (count + 1)) + 2 + 6

                            akh = akh + 1

                            cb2 + = str (count) + ". @name \ n"

                            cnt = cnt + 1

                            if cnt == 50:

                                cb = (cb [: int (len (cb) -1)])

                                cb2 = cb2 [: - 1]

                                msg.contentType = 0

                                msg.text = cb2

                                msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                                try:

                                    line.sendMessage (msg)

                                except:

                                    line.sendText (msg.to, "[[NO MENTION]]" ")

                                cb = ""

                                cb2 = ""

                                strt = len (str (count)) + 2

                                akh = int (0)

                                cnt = 0

                            count + = 1

                        cb = (cb [: int (len (cb) -1)])

                        cb2 = cb2 [: - 1]

                        msg.contentType = 0

                        msg.text = cb2

                        msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                        try:

                            line.sendMessage (msg)

                        except:

                            line.sendText (msg.to, "[[NO MENTION]]" ")

                    elif data [0] == "<":

                        mentargs = int (data [1:]. strip ())

                        group = line.getGroup (msg.to)

                        nama = [contact.mid for contact in group.members if contact.mid! = user1]

                        cb = ""

                        cb2 = ""

                        count = 1

                        strt = len (str (count)) + 2

                        akh = int (0)

                        cnt = 0

                        for md in nama:

                            if count> mentargs:

                                break

                            akh = akh + len (str (count)) + 2 + 5

                            cb + = "" "{" S ":" "" + json.dumps (str (strt)) + "" "," E ":" "" "+ json.dumps (str (akh)) +" "" , "M": "" "+ json.dumps (md) +"}, "" "

                            strt = strt + len (str (count + 1)) + 2 + 6

                            akh = akh + 1

                            cb2 + = str (count) + ". @name \ n"

                            cnt = cnt + 1

                            if cnt == 50:

                                cb = (cb [: int (len (cb) -1)])

                                cb2 = cb2 [: - 1]

                                msg.contentType = 0

                                msg.text = cb2

                                msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                                try:

                                    line.sendMessage (msg)

                                except:

                                    line.sendText (msg.to, "[[NO MENTION]]" ")

                                cb = ""

                                cb2 = ""

                                strt = len (str (count)) + 2

                                akh = int (0)

                                cnt = 0

                            count + = 1

                        cb = (cb [: int (len (cb) -1)])

                        cb2 = cb2 [: - 1]

                        msg.contentType = 0

                        msg.text = cb2

                        msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                        try:

                            line.sendMessage (msg)

                        except:

                            line.sendText (msg.to, "[[NO MENTION]]" ")

                    elif data [0] == ">":

                        mentargs = int (data [1:]. strip ())

                        group = line.getGroup (msg.to)

                        nama = [contact.mid for contact in group.members if contact.mid! = user1]

                        cb = ""

                        cb2 = ""

                        count = 1

                        if mentargs> = 0:

                            strt = len (str (mentargs)) + 2

                        else:

                            strt = len (str (count)) + 2

                        akh = int (0)

                        cnt = 0

                        for md in nama:

                            if count <mentargs:

                                count + = 1

                                continue

                            akh = akh + len (str (count)) + 2 + 5

                            cb + = "" "{" S ":" "" + json.dumps (str (strt)) + "" "," E ":" "" "+ json.dumps (str (akh)) +" "" , "M": "" "+ json.dumps (md) +"}, "" "

                            strt = strt + len (str (count + 1)) + 2 + 6

                            akh = akh + 1

                            cb2 + = str (count) + ". @name \ n"

                            cnt = cnt + 1

                            if cnt == 50:

                                cb = (cb [: int (len (cb) -1)])

                                cb2 = cb2 [: - 1]

                                msg.contentType = 0

                                msg.text = cb2

                                msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                                try:

                                    line.sendMessage (msg)

                                except:

                                    line.sendText (msg.to, "[[NO MENTION]]" ")

                                cb = ""

                                cb2 = ""

                                strt = len (str (count)) + 2

                                akh = int (0)

                                cnt = 0

                            count + = 1

                        cb = (cb [: int (len (cb) -1)])

                        cb2 = cb2 [: - 1]

                        msg.contentType = 0

                        msg.text = cb2

                        msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                        try:

                            line.sendMessage (msg)

                        except:

                            line.sendText (msg.to, "[[NO MENTION]]" ")

                    elif data [0] == "=":

                        mentargs = int (data [1:]. strip ())

                        group = line.getGroup (msg.to)

                        nama = [contact.mid for contact in group.members if contact.mid! = user1]

                        cb = ""

                        cb2 = ""

                        count = 1

                        akh = int (0)

                        cnt = 0

                        for md in nama:

                            if count! = mentargs:

                                count + = 1

                                continue

                            akh = akh + len (str (count)) + 2 + 5

                            strt = len (str (count)) + 2

                            cb + = "" "{" S ":" "" + json.dumps (str (strt)) + "" "," E ":" "" "+ json.dumps (str (akh)) +" "" , "M": "" "+ json.dumps (md) +"}, "" "

                            strt = strt + len (str (count + 1)) + 2 + 6

                            akh = akh + 1

                            cb2 + = str (count) + ". @name \ n"

                            cnt = cnt + 1

                            if cnt == 50:

                                cb = (cb [: int (len (cb) -1)])

                                cb2 = cb2 [: - 1]

                                msg.contentType = 0

                                msg.text = cb2

                                msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                                try:

                                    line.sendMessage (msg)

                                except:

                                    line.sendText (msg.to, "[[NO MENTION]]" ")

                                cb = ""

                                cb2 = ""

                                strt = len (str (count)) + 2

                                akh = int (0)

                                cnt = 0

                            count + = 1

                        cb = (cb [: int (len (cb) -1)])

                        cb2 = cb2 [: - 1]

                        msg.contentType = 0

                        msg.text = cb2

                        msg.contentMetadata = {'MENTION': '{"MENTIONEES": [' + cb + ']}', 'EMTVER': '4'}

                        try:

                            line.sendMessage (msg)

                        except:

                            line.sendText (msg.to, "[[NO MENTION]]" ")

                elif ".tx" in msg.text.lower ():

                    spl = re.split (". tx", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        line.kedapkedip (msg.to, spl [1])

                elif " name " in msg.text.lower ():

                    spl = re.split (" name ", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        prof = line.getProfile ()

                        prof.displayName = spl [1]

                        line.updateProfile (prof)

                        line.sendText (msg.to, " successful ")

                elif ".nmx" in msg.text.lower ():

                    spl = re.split (". nmx", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        prof = line.getProfile ()

                        prof.displayName = line.nmxstring (spl [1])

                        line.updateProfile (prof)

                        line.sendText (msg.to, " successful ")

                elif ".join" in msg.text.lower ():

                    spl = re.split (". join", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        try:

                            gid = spl [1] .split ("") [0]

                            ticket = spl [1] .split ("") [1] .replace ("line: // ti / g /", "") if "line: // ti / g /" in spl [1] .split ("") [1] else spl [1] .split ("") [1] .replace ("http://line.me/R/ti/g/", "") if "http: // line.me/R/ti/g/ "in spl [1] .split (" ") [1] else spl [1] .split (" ") [1]

                            line.acceptGroupInvitationByTicket (gid, ticket)

                        except Exception as e:

                            line.sendText (msg.to, str (e))             

                elif msg.text.lower (). startswith (". ctt"):

                    try:

                        text = msg.text.split ("", 1) [1]

                        headers = {

                        "User-Agent": "Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 63.0.3239.132 Safari / 537.36"

                        }

                        data = {

                        "q": text

                        }

                        conv = BeautifulSoup (requests.post ("http://lullar-de-2.appspot.com/", headers = headers, data = data) .content, "html.parser") .find ("span", attrs = {"style": "font-size: 40px"}). text

                        if msg.toType! = 0:

                                kk.sendText (msg.to, "Conversion: \ n" + conv)

                        else:

                                kk.sendText (msg.from _, "Conversion: \ n" + conv)

                    except Exception as e:

                        print (e)                                                                                   

                elif msg.text.lower (). startswith ("pz: gac"):

                    pnum = re.split ("pz: gac", msg.text, flags = re.IGNORECASE) [1]

                    pnum = "66" + pnum [1:]

                    GACReq = GACSender.send (pnum)

                    if GACReq.responseNum == 0:

                        if msg.toType! = 0:

                                kk.sendText (msg.to, " SMS was sent successfully ")

                        else:

                                kk.sendText (msg.from_, " SMS was sent successfully ")

                    elif GACReq.responseNum == 1:

                        if msg.toType! = 0:

                                kk.sendText (msg.to, " can not send SMS was due to send a message to a number of targets in proximity too \ n Please wait a 30 seconds and try again .")

                        else:

                                kk.sendText (msg.from_, " can not send SMS was due to send a message to a number of targets in proximity too \ n Please wait a 30 seconds and try again .")

                    else:

                        if msg.toType! = 0:

                                kk.sendText (msg.to, "Unknown error encountered ")

                        else:

                                kk.sendText (msg.from_, "Unknown error encountered ")

                elif msg.text.lower () == ".groupurl":

                    if msg.toType == 2:

                        line.sendText (msg.to, "http://line.me/R/ti/g/" + str (line.reissueGroupTicket (msg.to)))

                    else:

                        line.sendText (msg.to, " This command can only be used in groups ")

                elif "url" in msg.text.lower ():

                    spl = re.split ("url", msg.text, flags = re.IGNORECASE)

                    if spl [0] == "":

                        try:

                            line.sendText (msg.to, "http://line.me/R/ti/g/" + str (line.reissueGroupTicket (spl [1])))

                        except Exception as e:

                            line.sendText (msg.to, " Error found ( reason \" "+ e.reason +" \ ")")                                                       

# ===================================================== ============================= #

                elif msg.text in ["bo"]:

                    blockedlist = line.getBlockedContactIds ()

                    kontak = line.getContacts (blockedlist)

                    num = 1

                    msgs = "???? blocked list ?????"

                    for ids in kontak:

                        msgs + = "\ n [% i]% s"% (num, ids.displayName)

                        num = (num + 1)

                    msgs + = "\ n????By. M. BotSelf???? \ n \ n Amount :% i "% len (kontak)

                    line.sendMessage (receiver, msgs)

                elif text.lower () == 'tagall':

                    group = line.getGroup (msg.to)

                    nama = [contact.mid for contact in group.members]

                    k = len (nama) // 100

                    for a in range (k + 1):

                        txt = ''

                        s = 0

                        b = []

                        for i in group.members [a * 100: (a + 1) * 100]:

                            b.append ({"S": str (s), "E": str (s + 6), "M": i.mid})

                            s + = 7

                            txt + = '@Alin \ n'

                        line.sendMessage (to, text = txt, contentMetadata = {'MENTION': json.dumps ({'MENTIONEES': b})}, contentType = 0)

                        line.sendMessage (to, " number { people } " .format (str (len (nama)))))

                elif text.lower () == ' Tag ':

                    group = line.getGroup (msg.to)

                    nama = [contact.mid for contact in group.members]

                    k = len (nama) // 100

                    for a in range (k + 1):

                        txt = ''

                        s = 0

                        b = []

                        for i in group.members [a * 100: (a + 1) * 100]:

                            b.append ({"S": str (s), "E": str (s + 6), "M": i.mid})

                            s + = 7

                            txt + = '@Alin \ n'

                        line.sendMessage (to, text = txt, contentMetadata = {'MENTION': json.dumps ({'MENTIONEES': b})}, contentType = 0)

                        line.sendMessage (to, " all { people } " .format (str (len (nama))))) 

                elif text.lower () == ' Timer ':

                    tz = pytz.timezone ("Asia / Jakarta")

                    timeNow = datetime.now (tz = tz)

                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

                    hari = [" Sunday ", " Monday ", " Tuesday ", " Wednesday ", " Thursday ", " Friday ", " Saturday "]

                    bulan = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " December " ]

                    hr = timeNow.strftime ("% A")

                    bln = timeNow.strftime ("% m")

                    for i in range (len (day)):

                        if hr == day [i]: hasil = hari [i]

                    for k in range (0, len (bulan)):

                        if bln == str (k): bln = bulan [k-1]

                    readTime = hasil + "," + timeNow.strftime ('% d') + "-" + bln + "-" + timeNow.strftime ('% Y') + "\ n Duration : [" + timeNow.strftime ('% H:% M:% S') + "]"

                    if msg.to in read ['readPoint']:

                            try:

                                del read ['readPoint'] [msg.to]

                                del read ['readMember'] [msg.to]

                                del read ['readTime'] [msg.to]

                            except:

                                pass

                            read ['readPoint'] [msg.to] = msg.id

                            read ['readMember'] [msg.to] = ""

                            read ['readTime'] [msg.to] = datetime.now (). strftime ('% H:% M:% S')

                            read ['ROM'] [msg.to] = {}

                            with open ('read.json', 'w') as fp:

                                json.dump (read, fp, sort_keys = True, indent = 4)

                                line.sendMessage (msg.to, "Lurking enabled")

                    else:

                        try:

                            del read ['readPoint'] [msg.to]

                            del read ['readMember'] [msg.to]

                            del read ['readTime'] [msg.to]

                        except:

                            pass

                        read ['readPoint'] [msg.to] = msg.id

                        read ['readMember'] [msg.to] = ""

                        read ['readTime'] [msg.to] = datetime.now (). strftime ('% H:% M:% S')

                        read ['ROM'] [msg.to] = {}

                        with open ('read.json', 'w') as fp:

                            json.dump (read, fp, sort_keys = True, indent = 4)

                            line.sendMessage (msg.to, "Set reading point: \ n" + readTime)

 

                elif text.lower () == ' Timer Off ':

                    tz = pytz.timezone ("Asia / Jakarta")

                    timeNow = datetime.now (tz = tz)

                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

                    hari = [" Sunday ", " Monday ", " Tuesday ", " Wednesday ", " Thursday ", " Friday ", " Saturday "]

                    bulan = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " December " ]

                    hr = timeNow.strftime ("% A")

                    bln = timeNow.strftime ("% m")

                    for i in range (len (day)):

                        if hr == day [i]: hasil = hari [i]

                    for k in range (0, len (bulan)):

                        if bln == str (k): bln = bulan [k-1]

                    readTime = hasil + "," + timeNow.strftime ('% d') + "-" + bln + "-" + timeNow.strftime ('% Y') + "\ n Duration : [" + timeNow.strftime ('% H:% M:% S') + "]"

                    if msg.to not in read ['readPoint']:

                        line.sendMessage (msg.to, "Lurking disabled")

                    else:

                        try:

                            del read ['readPoint'] [msg.to]

                            del read ['readMember'] [msg.to]

                            del read ['readTime'] [msg.to]

                        except:

                              pass

                        line.sendMessage (msg.to, "Delete reading point: \ n" + readTime)

 

                elif text.lower () == ' Oval Time ':

                    tz = pytz.timezone ("Asia / Jakarta")

                    timeNow = datetime.now (tz = tz)

                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

                    hari = [" Sunday ", " Monday ", " Tuesday ", " Wednesday ", " Thursday ", " Friday ", " Saturday "]

                    bulan = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " December " ]

                    hr = timeNow.strftime ("% A")

                    bln = timeNow.strftime ("% m")

                    for i in range (len (day)):

                        if hr == day [i]: hasil = hari [i]

                    for k in range (0, len (bulan)):

                        if bln == str (k): bln = bulan [k-1]

                    readTime = hasil + "," + timeNow.strftime ('% d') + "-" + bln + "-" + timeNow.strftime ('% Y') + "\ n Duration : [" + timeNow.strftime ('% H:% M:% S') + "]"

                    if msg.to in read ["readPoint"]:

                        try:

                            del read ["readPoint"] [msg.to]

                            del read ["readMember"] [msg.to]

                            del read ["readTime"] [msg.to]

                        except:

                            pass

                        line.sendMessage (msg.to, "Reset reading point: \ n" + readTime)

                    else:

                        line.sendMessage (msg.to, "The time has been cleared "

 

                elif text.lower () == '# read '.

                    tz = pytz.timezone ("Asia / Jakarta")

                    timeNow = datetime.now (tz = tz)

                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

                    hari = [" Sunday ", " Monday ", " Tuesday ", " Wednesday ", " Thursday ", " Friday ", " Saturday "]

                    bulan = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " December " ]

                    hr = timeNow.strftime ("% A")

                    bln = timeNow.strftime ("% m")

                    for i in range (len (day)):

                        if hr == day [i]: hasil = hari [i]

                    for k in range (0, len (bulan)):

                        if bln == str (k): bln = bulan [k-1]

                    readTime = hasil + "," + timeNow.strftime ('% d') + "-" + bln + "-" + timeNow.strftime ('% Y') + "\ n Time : [" + timeNow.strftime ( '% H:% M:% S') + "]"

                    if receiver in read ['readPoint']:

                        if list (read ["ROM"] [receiver] .items ()) == []:

                            line.sendMessage (receiver, "[Reader]: \ nNone")

                        else:

                            chiya = []

                            for rom in list (read ["ROM"] [receiver] .items ()):

                                chiya.append (rom [1])

                            cmem = line.getContacts (chiya)

                            zx = ""

                            zxc = ""

                            zx2 = []

                            xpesan = '[*** LurkDetector ***]: \ n'

                        for x in range (len (cmem)):

                            xname = str (cmem [x] .displayName)

                            pesan = ''

                            pesan2 = pesan + "@ c \ n"

                            xlen = str (len (zxc) + len (xpesan))

                            xlen2 = str (len (zxc) + len (pesan2) + len (xpesan) -1)

                            zx = {'S': xlen, 'E': xlen2, 'M': cmem [x] .mid}

                            zx2.append (zx)

                            zxc + = pesan2

                        text = xpesan + zxc + "\ n [Lurking time]: \ n" + readTime

                        try:

                            line.sendMessage (receiver, text, contentMetadata = {'MENTION': str ('{"MENTIONEES":' + json.dumps (zx2) .replace ('', '') + '}')}, contentType = 0 )

                        except Exception as error:

                            print (error)

                        pass

                    else:

                        line.sendMessage (receiver, "Lurking has not been set.")

# ===================================================== ============================= #

                elif msg.text.lower (). startswith ("say-af"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'af'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-sq"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'sq'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ar"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ar'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-hy"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'hy'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-bn"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'bn'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ca"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ca'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-zh"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'zh'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-zh-cn"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'zh-cn'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-zh-tw"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'zh-tw'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-zh-yue"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'zh-yue'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-hr"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'hr'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-cs"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'cs'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-da"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'da'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-nl"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'nl'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-en"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'en'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-en-au"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'en-au'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-en-uk"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'en-uk'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-en-us"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'en-us'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-eo"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'eo'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-fi"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'fi'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-fr"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'fr'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-de"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'de'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-el"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'el'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-hi"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'hi'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-hu"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'hu'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-is"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'is'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-id"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'id'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-it"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'it'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ja"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ja'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-km"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'km'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ko"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ko'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-la"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'la'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-lv"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'lv'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-mk"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'mk'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-no"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'no'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-pl"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'pl'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-pt"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'pt'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-do"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ro'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ru"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ru'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-sr"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'sr'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-si"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'si'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-sk"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'sk'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-es"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'es'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-es-es"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'es-es'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-es-us"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'es-us'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-sw"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'sw'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-sv"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'sv'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-ta"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'ta'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-th"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'th'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-tr"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'tr'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-uk"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'uk'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-vi"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'vi'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

 

                elif msg.text.lower (). startswith ("say-cy"):

                    sep = text.split ("")

                    say = text.replace (sep [0] + "", "")

                    lang = 'cy'

                    tts = gTTS (text = say, lang = lang)

                    tts.save ("hasil.mp3")

                    line.sendAudio (msg.to, "hasil.mp3")

# ===================================================== ============================= #

                elif msg.text.lower (). startswith ("tr-af"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'af')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sq"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sq')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-am"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'am')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ar"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ar')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-hy"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'hy')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-az"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'az')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-eu"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'eu')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-be"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'be')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-bn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'bn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-bs"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'bs')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-bg"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'bg')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ca"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ca')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ceb"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ceb')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ny"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ny')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-zh-cn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'zh-cn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-zh-tw"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'zh-tw')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-co"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'co')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-hr"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'hr')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-cs"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'cs')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-da"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'da')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-nl"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'nl')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-en"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'en')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-et"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'et')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-fi"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'fi')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-fr"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'fr')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-fy"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'fy')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-gl"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'gl')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ka"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ka')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-de"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'de')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-el"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'el')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-gu"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'gu')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ht"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ht')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ha"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ha')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-haw"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'haw')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-iw"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'iw')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-hi"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'hi')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-hmn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'hmn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-hu"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'hu')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-is"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'is')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ig"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ig')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-id"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'id')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ga"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ga')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-it"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'it')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ja"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ja')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-jw"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'jw')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-kn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'kn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-kk"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'kk')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-km"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'km')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ko"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ko')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ku"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ku')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ky"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ky')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-lo"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'lo')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-la"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'la')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-lv"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'lv')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-lt"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'lt')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-lb"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'lb')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mk"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mk')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mg"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mg')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ms"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ms')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ml"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ml')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mt"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mt')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mi"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mi')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mr"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mr')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-mn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'mn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-my"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'my')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ne"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ne')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-no"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'no')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ps"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ps')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-fa"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'fa')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-pl"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'pl')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-pt"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'pt')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-pa"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'pa')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ro"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ro')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ru"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ru')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sm"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sm')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-gd"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'gd')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sr"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sr')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-st"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'st')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sn"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sn')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sd"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sd')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-si"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'si')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sk"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sk')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sl"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sl')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-so"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'so')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-es"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'es')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-su"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'su')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sw"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sw')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-sv"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'sv')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-tg"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'tg')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ta"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ta')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-te"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'te')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-th"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'th')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-tr"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'tr')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-uk"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'uk')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-ur"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'ur')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-uz"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'uz')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-vi"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'vi')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-cy"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'cy')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-xh"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'xh')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-yi"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'yi')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-yo"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'yo')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-zu"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'zu')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-fil"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'fil')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

                elif msg.text.lower (). startswith ("tr-he"):

                    sep = text.split ("")

                    isi = text.replace (sep [0] + "", "")

                    translator = Translator ()

                    hasil = translator.translate (isi, dest = 'he')

                    A = hasil.text

                    line.sendMessage (msg.to, A)

 

                elif msg.text in ["Jumanji"]:

                    hasil = "https://youtu.be/2QKg5SZ_35I"

                    A = hasil

                    line.sendVideoWithURL (msg.to, A)

 

#sender = msg._from

# if msg.toType == 0:

# if sender! = line.profile.mid:

# ===================================================== ============================= #  

                elif "Broadcastvoice" in msg.text:

                    bctxt = msg.text.replace ("Bcvoice", "")

                    bc = (".Bdw .. Ini adalah Broadcast .. Salam Owner ARDIAN PURNAMA .. by. RFU boot sekawan")

                    cb = (bctxt + bc)

                    tts = gTTS (cb, lang = 'id', slow = False)

                    tts.save ('tts.mp3')

                    n = line.getGroupIdsJoined ()

                    for manusia in n:

                        line.sendAudio (manusia, 'tts.mp3')

 

                elif "Cbroadcastvoice" in msg.text:

                    bctxt = msg.text.replace ("Cbcvoice", "")

                    bc = (".Bdw .. Ini adalah Broadcast .. Salam Owner ARDIAN PURNAMA .. by. RFU boot sekawan")

                    cb = (bctxt + bc)

                    tts = gTTS (cb, lang = 'id', slow = False)

                    tts.save ('tts.mp3')

                    n = line.getAllContactIdsJoined ()

                    for manusia in n:

                        line.sendAudio (manusia, 'tts.mp3')

 

                elif "Wikipedia" in msg.text:

                      try:

                          wiki = msg.text.lower (). replace ("Wikipedia", "")

                          wikipedia.set_lang ("id")

                          pesan = "Title ("

                          pesan + = wikipedia.page (wiki) .title

                          pesan + = ") \ n \ n"

                          pesan + = wikipedia.summary (wiki, sentences = 1)

                          pesan + = "\ n"

                          pesan + = wikipedia.page (wiki) .url

                          line.sendMessage (msg.to, pesan)

                      except:

                              try:

                                  pesan = "Over Text Limit! Please Click link \ n"

                                  pesan + = wikipedia.page (wiki) .url

                                  line.sendText (msg.to, pesan)

                              except Exception as e:

                                  line.sendMessage (msg.to, str (e))

 

                elif "Film:" in msg.text:

                    proses = msg.text.split (":")

                    get = msg.text.replace (proses [0] + ":", "")

                    getfilm = get.split ()

                    title = getfilm [0]

                    tahun = getfilm [1]

                    r = requests.get ('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')

                    start = time.time ()

                    data = r.text

                    data = json.loads (data)

                    hasil = "Informasi \ n" + str (data ["Title"]) + "(" + str (data ["Year"]) + ")"

                    hasil + = "\ n \ n" + str (data ["Plot"])

                    hasil + = "\ n \ nDirector:" + str (data ["Director"])

                    hasil + = "\ nActors:" + str (data ["Actors"])

                    hasil + = "\ nRelease:" + str (data ["Released"])

                    hasil + = "\ nGenre:" + str (data ["Genre"])

                    hasil + = "\ nRuntime:" + str (data ["Runtime"])

                    path = data ["Poster"]

                    line.sendImageWithURL (msg.to, str (path))

                    line.sendMessage (msg.to, hasil)

 

                elif text.lower () == ' View time ':

                    tz = pytz.timezone ("Asia / Jakarta")

                    timeNow = datetime.now (tz = tz)

                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

                    hari = [" Sunday ", " Monday ", " Tuesday ", " Wednesday ", " Thursday ", " Friday ", " Saturday "]

                    bulan = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " December " ]

                    hr = timeNow.strftime ("% A")

                    bln = timeNow.strftime ("% m")

                    for i in range (len (day)):

                        if hr == day [i]: hasil = hari [i]

                    for k in range (0, len (bulan)):

                        if bln == str (k): bln = bulan [k-1]

                    readTime = hasil + "," + timeNow.strftime ('% d') + "-" + bln + "-" + timeNow.strftime ('% Y') + "\ n Time : [" + timeNow.strftime ( '% H:% M:% S') + "]"

                    line.sendMessage (msg.to, readTime)                

                elif "screenshotwebsite" in msg.text.lower ():

                    sep = text.split ("")

                    query = text.replace (sep [0] + "", "")

                    with requests.session () as web:

                        r = web.get ("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link= {}" .format (urllib.parse.quote (query)))

                        data = r.text

                        data = json.loads (data)

                        line.sendImageWithURL (to, data ["result"])

                elif "checkdate" in msg.text.lower ():

                    sep = msg.text.split ("")

                    tanggal = msg.text.replace (sep [0] + "", "")

                    r = requests.get ('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)

                    data = r.text

                    data = json.loads (data)

                    ret_ = "??? [DATE]"

                    ret_ + = "\ n? Date Of Birth: {}". format (str (data ["data"] ["lahir"]))

                    ret_ + = "\ n? Age: {}". format (str (data ["data"] ["usia"]))

                    ret_ + = "\ n? Birthday: {}". format (str (data ["data"] ["ultah"]))

                    ret_ + = "\ n? Zodiak: {}". format (str (data ["data"] ["zodiak"]))

                    ret_ + = "\ n??? [Success]"

                    line.sendMessage (to, str (ret_))

 

                elif "instagram" in msg.text.lower ():

                    sep = text.split ("")

                    search = text.replace (sep [0] + "", "")

                    with requests.session () as web:

                        web.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                        r = web.get ("https://www.instagram.com/{}/?__a=1" .format (search))

                        try:

                            data = json.loads (r.text)

                            ret_ = "??? [Profile Instagram]"

                            ret_ + = "\ n? Nama: {}". format (str (data ["user"] ["full_name"]))

                            ret_ + = "\ n? Username: {}". format (str (data ["user"] ["username"]))

                            ret_ + = "\ n? Bio: {}". format (str (data ["user"] ["biography"]))

                            ret_ + = "\ n? Pengikut: {}". format (format_number (data ["user"] ["followed_by"] ["count"]))

                            ret_ + = "\ n? Diikuti: {}". format (format_number (data ["user"] ["follows"] ["count"]))

                            if data ["user"] ["is_verified"] == True:

                                ret_ + = "\ n? Verifikasi: Sudah"

                            else:

                                ret_ + = "\ n? Verifikasi: Belum"

                            if data ["user"] ["is_private"] == True:

                                ret_ + = "\ n? Akun Pribadi: Iya"

                            else:

                                ret_ + = "\ n? Akun Pribadi: Tidak"

                            ret_ + = "\ n? Post number : {}". format (format_number (data ["user"] ["media"] ["count"]))

                            ret_ + = "\ n??? [https://www.instagram.com/ {}]". format (search)

                            path = data ["user"] ["profile_pic_url_hd"]

                            line.sendImageWithURL (to, str (path))

                            line.sendMessage (to, str (ret_))

                        except:

                            line.sendMessage (to, " user not found ")

                elif "fotoig" in msg.text.lower ():

                    separate = msg.text.split ("")

                    user = msg.text.replace (separate [0] + "", "")

                    profile = "https://www.instagram.com/" + user

                    with requests.session () as x:

                        x.headers ['user-agent'] = 'Mozilla / 5.0'

                        end_cursor = ''

                        for count in range (1):

                            print (('send foto:', count))

                            r = x.get (profile, params = {'max_id': end_cursor})                       

                            data = re.search (r'window._sharedData = (\ {. +?}); </script> ', r.text) .group (1)

                            j = json.loads (data)                       

                            for node in j ['entry_data'] ['ProfilePage'] [0] ['user'] ['media'] ['nodes']:

                                page = 'https://www.instagram.com/p/' + node ['code']

                                r = x.get (page)

                                print ((node ??['display_src']))

                                line.sendImageWithURL (msg.to, node ['display_src'])

                elif " put pictures " in msg.text.lower ():

                    separate = msg.text.split ("")

                    search = msg.text.replace (separate [0] + "", "")

                    with requests.session () as web:

                        web.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                        r = web.get ("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q= {}" .format (urllib.parse.quote (search)))

                        data = r.text

                        data = json.loads (data)

                        if data ["result"]! = []:

                            items = data ["result"]

                            path = random.choice (items)

                            a = items.index (path)

                            b = len (items)

                            line.sendImageWithURL (to, str (path))

                elif "The image is coming " in msg.text.lower ():

                    separate = msg.text.split ("")

                    search = msg.text.replace (separate [0] + "", "")

                    with requests.session () as web:

                        web.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                        r = web.get ("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q= {}" .format (urllib.parse.quote (search)))

                        data = r.text

                        data = json.loads (data)

                        if data ["result"]! = []:

                            items = data ["result"]

                            path = random.choice (items)

                            a = items.index (path)

                            b = len (items)

                            line.sendImageWithURL (to, str (path))

                elif " youtube " in msg.text.lower ():

                    sep = text.split ("")

                    search = text.replace (sep [0] + "", "")

                    params = {"search_query": search}

                    with requests.session () as web:

                        web.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                        r = web.get ("https://www.youtube.com/results", params = params)

                        soup = BeautifulSoup (r.content, "html.parser")

                        ret_ = "??? [ M. BotSelf search results ]"

                        datas = []

                        for data in soup.select (". yt-lockup-title> a [title]"):

                            if "& lists" not in data ["href"]:

                                datas.append (data)

                        for data in datas:

                            ret_ + = "\ n??? [{}]". format (str (data ["title"])))

                            ret_ + = "\ n? https://www.youtube.com {}" .format (str (data ["href"])))

                        ret_ + = "\ n??? [ amount found {}]". format (len (datas))

                        line.sendMessage (to, str (ret_))

 

                elif msg.text in [" Open to see the readers "]:

                    try:

                        del RfuCctv ['point'] [msg.to]

                        del RfuCctv ['sidermem'] [msg.to]

                        del RfuCctv ['cyduk'] [msg.to]

                    except:

                        pass

                    RfuCctv ['point'] [msg.to] = msg.id

                    RfuCctv ['sidermem'] [msg.to] = ""

                    RfuCctv ['cyduk'] [msg.to] = True

                    line.sendMessage (msg.to, " Open, read ")

                elif msg.text in [" Close, view the reader "]:

                    if msg.to in RfuCctv ['point']:

                        RfuCctv ['cyduk'] [msg.to] = False

                        line.sendText (msg.to, RfuCctv ['sidermem'] [msg.to])

                    else:

                        line.sendMessage (msg.to, " closed, read ")

 

                elif text.lower () == ' Close bot ':

                    line.sendMessage (receiver, 'The cellbot has been stopped. ')

                    print ("Selfbot Off")

                    exit (1)

 

                elif text.lower () == ' Friend ':

                    contactlist = line.getAllContactIds ()

                    kontak = line.getContacts (contactlist)

                    num = 1

                    msgs = "??????friends list"

                    for ids in kontak:

                        msgs + = "\ n [% i]% s"% (num, ids.displayName)

                        num = (num + 1)

                    msgs + = "\ n??List Friend?? \ n \ nTotal Teman:% i"% len (kontak)

                    line.sendMessage (msg.to, msgs)

 

                elif msg.text in ["Blocklist"]:

                    blockedlist = line.getBlockedContactIds ()

                    kontak = line.getContacts (blockedlist)

                    num = 1

                    msgs = "?????Daftar Akun Yang di Blocked?????"

                    for ids in kontak:

                        msgs + = "\ n [% i]% s"% (num, ids.displayName)

                        num = (num + 1)

                    msgs + = "\ n????????List Blocked???????? \ n \ nTotal Blocked:% i"% len (kontak)

                    line.sendMessage (receiver, msgs)

 

                elif msg.text in ["Friendlist mid"]:

                    gruplist = line.getAllContactIds ()

                    kontak = line.getContacts (gruplist)

                    num = 1

                    msgs = "?????????List FriendMid?????????"

                    for ids in kontak:

                        msgs + = "\ n [% i]% s"% (num, ids.mid)

                        num = (num + 1)

                    msgs + = "\ n?????????List FriendMid????????? \ n \ nTotal Friend:% i"% len (kontak)

                    line.sendMessage (receiver, msgs)

 

                elif msg.text.lower () == 'gurl':

                              if msg.toType == 2:

                         g = line.getGroup (receiver)

                         line.updateGroup (g)

                         gurl = line.reissueGroupTicket (receiver)

                         line.sendMessage (receiver, "??????????????? ? \ n? ? line: // ti / g /" + gurl + "\ n? \ n? ? Link Groupnya Tanpa Buka Qr \ n??????????????? ? ")

 

                elif msg.text == " Horny ":

                              line.sendMessage (receiver, "> nekopoi.host \ n> sexvideobokep.com \ n> memek.com \ n> pornktube.com \ n> faketaxi.com \ n> videojorok.com \ n> watchmygf.mobi \ n> xnxx.com \ n> pornhd.com \ n> xvideos.com \ n> vidz7.com \ n> m.xhamster.com \ n> xxmovies.pro \ n> youporn.com \ n> pornhub.com \ n> youjizz.com \ n> thumzilla.com \ n> anyporn.com \ n> brazzers.com \ n> redtube.com \ n> youporn.com ")

 

 

                elif msg.text.lower () == 'invite: gcreator':

                              if msg.toType == 2:               

                           ginfo = line.getGroup (receiver)

                           try:

                               gcmid = ginfo.creator.mid

                           except:

                               gcmid = "Error"

                           if settings ["lang"] == "JP":

                               line.inviteIntoGroup (receiver, [gcmid])

                               line.sendMessage (receiver, "Type?? Invite Pembuat Group Succes")

                           else:

                               line.inviteIntoGroup (receiver, [gcmid])

                               line.sendMessage (receiver, "Pembuat Group Sudah di dalam")

 

                elif msg.text in ["/ uninstall"]:

                    if msg.toType == 2:

                        ginfo = line.getGroup (receiver)

                        try:

                            line.leaveGroup (receiver)                                                                                                 

                        except:

                            pass

 

                elif msg.text in ["Tagimage on", "Tag2 on", " Open Tag 2"]:

                        settings ['potoMention'] = True

                        line.sendMessage (msg.to, " the opening track then .").

 

                elif msg.text in ["Tagimage off", "Tag2 off", " Tag 2 off "]:

                        settings ['potoMention'] = False

                        line.sendMessage (msg.to, "Image tag disabled .")

 

                elif msg.text in ["Respontag on", "Tag on", "My respon on", "Respon: on", " Open Tag "]:

                    settings ["detectMention"] = True

                    line.sendMessage (msg.to, " the opening track to track with it .").

 

                elif msg.text in ["Respontag off", "Tag off", "My respon off", "Respon: off", " Tag off "]:

                    settings ["detectMention"] = False

                    line.sendMessage (msg.to, "tagged with. ")

 

                elif msg.text.lower (). startswith (" write "):

                    sep = msg.text.split ("")

                    textnya = msg.text.replace (sep [0] + "", "")

                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "& chts = FFFFFF, 70 & chf = bg, s, 000000"

                    line.sendImageWithURL (msg.to, urlnya)

 

                elif "kedip" in msg.text:

                    txt = msg.text.replace ("kedip", "")

                    t1 = "\ xf4 \ x80 \ xb0 \ x82 \ xf4 \ x80 \ xb0 \ x82 \ xf4 \ x80 \ xb0 \ x82 \ xf4 \ x80 \ xb0 \ x82 \ xf4 \ x80 \ xa0 \ x81 \ xf4 \ x80 \ xa0 \ x81 \ xf4 \ x80 \ xa0 \ x81 "

                    t2 = "\ xf4 \ x80 \ x82 \ xb3 \ xf4 \ x8f \ xbf \ xbf"

                    line.sendMessage (msg.to, t1 + txt + t2)                                                                                   

                elif msg.text in ["Inviteuser"]:

                        settings ["winvite"] = True

                        line.sendMessage (msg.to, "send a contact to invite user")                           

                elif msg.text.lower () == ".invitecancel":

                    if msg.toType == 2:

                        group = line.getGroup (msg.to)

                        gMembMids = [contact.mid for contact in group.invitee]

                        for i in gMembMids:

                            line.cancelGroupInvitation (msg.to, [i])

                elif msg.text.lower () == ".invitecancel2":

                    if msg.toType == 2:

                        group = line.getGroup (msg.to)

                        gMembMids = [contact.mid for contact in group.invitee]

                        for i in gMembMids:

                            random.choice (Exc) .cancelGroupInvitation (msg.to, [i])

# ============= COMMAND KICKER =============================== #

                elif msg.text in [" Clear black "]:

                    settings ["blacklist"] = {}

                    line.sendMessage (msg.to, "Complete all blacklist ")

                    print ("Clear Ban")

 

                elif ' kick ' in text.lower ():

                       targets = []

                       key = eval (msg.contentMetadata ["MENTION"])

                       key ["MENTIONEES"] [0] ["M"]

                       for x in key ["MENTIONEES"]:

                           targets.append (x ["M"])

                       for target in targets:

                           try:

                               random.choice (Rfu) .kickoutFromGroup (msg.to, [target])     

                               print ("Rfu kick User")

                           except:

                               random.choice (Rfu) .sendMessage (msg.to, "Limit kaka ??")

 

                elif 'kill' in text.lower ():

                       targets = []

                       key = eval (msg.contentMetadata ["MENTION"])

                       key ["MENTIONEES"] [0] ["M"]

                       for x in key ["MENTIONEES"]:

                           targets.append (x ["M"])

                       for target in targets:

                           try:

                               line.kickoutFromGroup (msg.to, [target])            

                               print ("Sb Kick User")

                           except:

                               line.sendMessage (msg.to, "Limit kaka ??")                              

 

                elif 'invite' in text.lower ():

                       targets = []

                       key = eval (msg.contentMetadata ["MENTION"])

                       key ["MENTIONEES"] [0] ["M"]

                       for x in key ["MENTIONEES"]:

                           targets.append (x ["M"])

                       for target in targets:

                           try:

                               line.inviteIntoGroup (msg.to, [target])

                               line.sendMessage (receiver, "Type?? Invite Succes")

                           except:

                               line.sendMessage (msg.to, "Type?? Limit Invite")

                elif "Cleanse" in msg.text:

                              if msg.toType == 2:

                         _name = msg.text.replace ("Cleanse", "")

                         gs = line.getGroup (receiver)

                         line.sendMessage (receiver, "Just some casual cleansing")

                         targets = []

                         for g in gs.members:

                             if _name in g.displayName:

                                 targets.append (g.mid)

                         if targets == []:

                             line.sendMessage (receiver, "Not found.")

                         else:

                             for target in targets:

                                           if not target in Rfu:

                                     try:

                                         klist = [line]

                                         kicker = random.choice (klist)

                                         kicker.kickoutFromGroup (receiver, [target])

                                         print ((receiver, [g.mid]))

                                     except:

                                         line.sendMessage (receiver, "Group cleanse")

                                         print ("Cleanse Group")

# ------------------------------------------------- ------------------------------

                elif text.lower () == 'clearban':

                    if msg._from in bot1:

                        settings ["blacklist"] = {}

                        line.sendMessage (msg.to, "Blacklist Dibersihkan")

 

                elif text.lower () == 'bancontact':

                    if msg._from in bot1:

                        settings ["wblacklist"] = True

                        line.sendMessage (msg.to, "Send Contact")

 

                elif msg.text in ["unbancontact"]:

                    if msg._from in bot1:

                        settings ["dblacklist"] = True

                        line.sendMessage (msg.to, "Send Contact")

# ------------------------------------------------- ------------------------------

                elif text.lower () == ' Black shake ':

                    if msg._from in bot1:

                        if settings ["blacklist"] == {}:

                            line.sendMessage (msg.to, " No black addicted ")

                        else:

                            line.sendMessage (msg.to, " Please wait ...")

                            num = 1

                            msgs = "?????????? List of black addicted ????????? "

                            for mi_d in settings ["blacklist"]:

                                msgs + = "\ n [% i]% s"% (num, line.getContact (mi_d) .displayName)

                                num = (num + 1)

                            msgs + = "\ n?????????? Black list of names ????????? \ n \ nNumber of black additions :% i "% len (settings [" blacklist "])

                            line.sendMessage (msg.to, msgs)

# ===================================================== ==========================================

 

                elif msg.text in ["Scan blacklist"]:

                              if msg.toType == 2:

                         group = line.getGroup (receiver)

                         gMembMids = [contact.mid for contact in group.members]

                         matched_list = []

                         for tag in settings ["blacklist"]:

                             matched_list + = [str for str in gMembMids if str == tag]

                         if matched_list == []:

                             line.sendMessage (receiver, "Nots in Blacklist")

                         else:

                             for jj in matched_list:

                                 try:

                                     klist = [line]

                                     kicker = random.choice (klist)

                                     kicker.kickoutFromGroup (receiver, [jj])

                                     print ((receiver, [jj]))

                                 except:

                                     line.sendMessage (receiver, "sorry bl ke cyduk")

                                     print ("Blacklist di Kick")

                elif " name :" in text.lower ():

                    if msg._from in Family:

                        proses = text.split (":")

                        string = text.replace (proses [0] + ":", "")

                        profile_A = line.getProfile ()

                        profile_A.displayName = string

                        line.updateProfile (profile_A)

                        line.sendMessage (msg.to, " name update successful " + string)

                        print ("Update Name")

                elif "Update add:" in msg.text:

                    settings ["addmsg"] = msg.text.replace ("Update add:", "")

                    line.sendMessage (msg.to, "Update message auto add:" + settings ["addmsg"] + "\ n \ n" + datetime.today (). strftime ('% H:% M:% S'))

                elif msg.text in ["Check add"]:

                    if settings ["lang"] == "JP":

                        line.sendMessage (msg.to, "message auto add. \ n \ n" + settings ["addmsg"])

                    else:

                        line.sendMessage (msg.to, "message add me. \ n \ n" + settings ["addmsg"])

                elif " Titus :" in msg.text.lower ():.

                    if msg._from in Family:

                        proses = text.split (":")

                        string = text.replace (proses [0] + ":", "")

                        profile_A = line.getProfile ()

                        profile_A.statusMessage = string

                        line.updateProfile (profile_A)

                        line.sendMessage (msg.to, " update ??" + string)

                        print ("Update Bio Succes")

                elif msg.text.lower (). startswith ("bitcoin"):

                   search = msg.text.split ("bitcoin")

                   with requests.session () as web:

                       web.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                       url = "https://xeonwz.herokuapp.com/bitcoin.api"

                       r = web.get (url)

                       data = r.text

                       data = json.loads (data)

                       print (data)

                       hasil = " ?Bitcoin Result ?"

                       hasil + = "\ nPrice:" + str (data ["btc"])                               

                       hasil + = "\ nExpensive:" + str (data ["high"])

                       hasil + = "\ nCheap:" + str (data ["low"])              

                       line.sendMessage (to, str (hasil))

# ============= COMMAND PROTECT ========================= # #

                elif msg.text.lower () == 'protect on':

                    if RfuProtect ["protect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " open block    ")

                        else:

                            line.sendMessage (msg.to, " open block    ")

                    else:

                        RfuProtect ["protect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " open block    ")

                        else:

                            line.sendMessage (msg.to, " open block    ")

 

                elif msg.text.lower () == 'protect off':

                    if RfuProtect ["protect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " closed block    ")

                        else:

                            line.sendMessage (msg.to, " closed block    ")

                    else:

                        RfuProtect ["protect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " closed block    ")

                        else:

                            line.sendMessage (msg.to, " closed block    ")

 

                elif msg.text.lower () == 'cancel pro on':

                    if RfuProtect ["cancelprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Enable, prevent, cancel, invite    ")

                        else:

                            line.sendMessage (msg.to, " Enable, prevent, cancel, invite    ")

                    else:

                        RfuProtect ["cancelprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Enable, prevent, cancel, invite    ")

                        else:

                            line.sendMessage (msg.to, " Enable, prevent, cancel, invite    ")

 

                elif msg.text.lower () == 'cancel pro off':

                    if RfuProtect ["cancelprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " off, block, cancel, invite    ")

                        else:

                            line.sendMessage (msg.to, " off, block, cancel, invite    ")

                    else:

                        RfuProtect ["cancelprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " off, block, cancel, invite    ")

                        else:

                            line.sendMessage (msg.to, " off, block, cancel, invite    ")

 

                elif msg.text.lower () == 'invit pro on':

                    if RfuProtect ["inviteprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Open, prevent, raise, invite    ")

                        else:

                            line.sendMessage (msg.to, " Open, prevent, raise, invite    ")

                    else:

                        RfuProtect ["inviteprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Open, prevent, raise, invite    ")

                        else:

                            line.sendMessage (msg.to, " Open, prevent, raise, invite    ")

 

                elif msg.text.lower () == 'invit pro off':

                    if RfuProtect ["inviteprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Disable, prevent, raise, invite    ")

                        else:

                            line.sendMessage (msg.to, " Disable, prevent, raise, invite    ")

                    else:

                        RfuProtect ["inviteprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Disable, prevent, raise, invite    ")

                        else:

                            line.sendMessage (msg.to, " Disable, prevent, raise, invite    ")

 

                elif msg.text.lower () == 'link pro on':

                    if RfuProtect ["linkprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " enable link protection    ")

                        else:

                            line.sendMessage (msg.to, " enable link protection    ")

                    else:

                        RfuProtect ["linkprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " enable link protection    ")

                        else:

                            line.sendMessage (msg.to, " enable link protection    ")

 

                elif msg.text.lower () == 'link pro off':

                    if RfuProtect ["linkprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " close link block    ")

                        else:

                            line.sendMessage (msg.to, " close link block    ")

                    else:

                        RfuProtect ["linkprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " close link block    ")

                        else:

                            line.sendMessage (msg.to, " close link block    ")

 

                elif msg.text.lower () == 'guest pro on':

                    if RfuProtect ["Protectguest"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Open protected members    ")

                        else:

                            line.sendMessage (msg.to, " Open protected members    ")

                    else:

                        RfuProtect ["Protectguest"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " Open protected members    ")

                        else:

                            line.sendMessage (msg.to, " Open protected members    ")

 

                elif msg.text.lower () == 'guest pro off':

                    if RfuProtect ["Protectguest"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " disable member protection    ")

                        else:

                            line.sendMessage (msg.to, " disable member protection    ")

                    else:

                        RfuProtect ["Protectguest"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " disable member protection    ")

                        else:

                            line.sendMessage (msg.to, " disable member protection    ")

 

                elif msg.text.lower () == 'join pro on':

                    if RfuProtect ["Protectjoin"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " prevent access    ")

                        else:

                            line.sendMessage (msg.to, " prevent access    ")

                    else:

                        RfuProtect ["Protectjoin"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, " prevent access    ")

                        else:

                            line.sendMessage (msg.to, " prevent access    ")

 

                elif msg.text.lower () == 'join pro off':

                    if RfuProtect ["Protectjoin"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "Block access    ")

                        else:

                            line.sendMessage (msg.to, "Block access    ")

                    else:

                        RfuProtect ["Protectjoin"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "Block access    ")

                        else:

                            line.sendMessage (msg.to, "Block access    ")

 

                elif msg.text.lower () == ' Open all ':

                    if RfuProtect ["inviteprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Open all protection ?? ")

                        else:

                            line.sendMessage (msg.to, "?? Open all protection ?? ")

                    else:

                        RfuProtect ["inviteprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Open invite ")

                    if RfuProtect ["cancelprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Enable, prevent, cancel, invite ")

                        else:

                            line.sendMessage (msg.to, "?? Enable, prevent, cancel, invite ")

                    else:

                        RfuProtect ["cancelprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Enable, prevent, cancel, invite ")

                    if RfuProtect ["protect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Enable, prevent, cancel, invite ")

                        else:

                            line.sendMessage (msg.to, "?? Enable, prevent, cancel, invite ")

                    else:

                        RfuProtect ["protect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Turn on anti-kick ")

                        else:

                            line.sendMessage (msg.to, "?? Turn on anti-kick ")

                    if RfuProtect ["linkprotect"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Enable link protection ")

                        else:

                            line.sendMessage (msg.to, "?? Enable link protection ")

                    else:

                        RfuProtect ["linkprotect"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Enable link protection ")

                        else:

                            line.sendMessage (msg.to, "?? Enable link protection ")

                    if RfuProtect ["Protectguest"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Turn on group protection ")

                        else:

                            line.sendMessage (msg.to, "?? Turn on group protection ")

                    else:

                        RfuProtect ["Protectguest"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Turn on group protection ")

                        else:

                            line.sendMessage (msg.to, "?? Turn on group protection ")

                    if RfuProtect ["Protectjoin"] == True:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Open to protect people under the group ")

                        else:

                            line.sendMessage (msg.to, "?? Open to protect people under the group ")

                    else:

                        RfuProtect ["Protectjoin"] = True

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "?? Open to protect people under the group ")

                        else:

                            line.sendMessage (msg.to, "?? Open to protect people under the group ")

 

                elif msg.text.lower () == ' Close all ':

                    if RfuProtect ["inviteprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Close all protection ? ")

                        else:

                            line.sendMessage (msg.to, "? Close all protection ? ")

                    else:

                        RfuProtect ["inviteprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Turn off protection ")

                    if RfuProtect ["cancelprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Closed, prevent, raise, invite ")

                        else:

                            line.sendMessage (msg.to, "? Closed, prevent, raise, invite ")

                    else:

                        RfuProtect ["cancelprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Closed, prevent, raise, invite ")

                    if RfuProtect ["protect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Close the kick prevention ")

                        else:

                            line.sendMessage (msg.to, "? Close the kick prevention ")

                    else:

                        RfuProtect ["protect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Close the kick prevention ")

                        else:

                            line.sendMessage (msg.to, "? Close the kick prevention ")

                    if RfuProtect ["linkprotect"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Close, prevent links ")

                        else:

                            line.sendMessage (msg.to, "? Close, prevent links ")

                    else:

                        RfuProtect ["linkprotect"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Close, prevent links ")

                        else:

                            line.sendMessage (msg.to, "? Close, prevent links ")

                    if RfuProtect ["Protectguest"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Turn off group protection ")

                        else:

                            line.sendMessage (msg.to, "? Turn off group protection ")

                    else:

                        RfuProtect ["Protectguest"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Turn off group protection ")

                        else:

                            line.sendMessage (msg.to, "? Turn off group protection ")

                    if RfuProtect ["Protectjoin"] == False:

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Off to prevent people into the group ")

                        else:

                            line.sendMessage (msg.to, "? Off to prevent people into the group ")

                    else:

                        RfuProtect ["Protectjoin"] = False

                        if settings ["lang"] == "JP":

                            line.sendMessage (msg.to, "? Off to prevent people into the group ")

                        else:

                            line.sendMessage (msg.to, "? Off to prevent people into the group ")

 

# ============== FINNISHING PROTECT ======================== #

                elif msg.text.lower () == ' Welcome on':

                        if settings ["Wc"] == True:

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "?? Open welcome message when members join the group ")

                        else:

                            settings ["Wc"] = True

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "?? Open welcome message when members join the group ")

                elif msg.text.lower () == ' welcome off':

                        if settings ["Wc"] == False:

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "? Turn off welcome messages when members join the group    ")

                        else:

                            settings ["Wc"] = False

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "? Turn off welcome messages when members join the group    ")

 

                elif msg.text.lower () == ' Exit on':

                        if settings ["Lv"] == True:

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "?? Open welcome message when members leave the group    ")

                        else:

                            settings ["Lv"] = True

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "?? Open welcome message when members leave the group    ")

                elif msg.text.lower () == ' Exit off':

                        if settings ["Lv"] == False:

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "? Close welcome message when members leave the group    ")

                        else:

                            settings ["Lv"] = False

                            if settings ["lang"] == "JP":

                                line.sendMessage (to, "? Close welcome message when members leave the group    ")

 

                elif text.lower () == '/ delete run ':

                    gid = line.getGroupIdsInvited ()

                    start = time.time ()

                    for i in gid:

                        line.rejectGroupInvitation (i)

                    elapsed_time = time.time () - start

                    line.sendMessage (to, " Delete, run, finished ")

                    line.sendMessage (to, " Duration used :% s seconds "% (elapsed_time))                                                                                                               

                                                                                                               

                elif "Allban" in msg.text:

                  if msg._from in Family:

                      if msg.toType == 2:

                           print ("All Banlist")

                           _name = msg.text.replace ("Allban", "")

                           gs = line.getGroup (msg.to)

                           line.sendMessage (msg.to, "Banned all")

                           targets = []

                           for g in gs.members:

                               if _name in g.displayName:

                                    targets.append (g.mid)

                           if targets == []:

                                line.sendMessage (msg.to, "Maaf")

                           else:

                               for target in targets:

                                   if not target in Family:

                                       try:

                                           settings ["blacklist"] [target] = True

                                           f = codecs.open ('st2__b.json', 'w', 'utf-8')

                                           json.dump (settings ["blacklist"], f, sort_keys = True, indent = 4, ensure_ascii = False)

                                       except:

                                           line.sentMessage (msg.to, " All members have been banned ")

                                                                                                                                              

                elif ' black ' in text.lower ():

                       targets = []

                       key = eval (msg.contentMetadata ["MENTION"])

                       key ["MENTIONEES"] [0] ["M"]

                       for x in key ["MENTIONEES"]:

                           targets.append (x ["M"])

                       for target in targets:

                           try:

                               settings ["blacklist"] [target] = True

                               f = codecs.open ('st2__b.json', 'w', 'utf-8')

                               json.dump (settings ["blacklist"], f, sort_keys = True, indent = 4, ensure_ascii = False)

                               line.sendMessage (msg.to, " successfully added to the blacklist ")

                               print ("Banned User")

                           except:

                               line.sendMessage (msg.to, " contact not found ")

 

                elif ' white ' in text.lower ():

                       targets = []

                       key = eval (msg.contentMetadata ["MENTION"])

                       key ["MENTIONEES"] [0] ["M"]

                       for x in key ["MENTIONEES"]:

                           targets.append (x ["M"])

                       for target in targets:

                           try:

                               del settings ["blacklist"] [target]

                               f = codecs.open ('st2__b.json', 'w', 'utf-8')

                               json.dump (settings ["blacklist"], f, sort_keys = True, indent = 4, ensure_ascii = False)

                               line.sendMessage (msg.to, " Fix black ...")

                               print ("Unbanned User")

                           except:

                               line.sendMessage (msg.to, " contact not found ")

                elif text.lower () == " Virus ":

                                line.sendContact (to, "u010598af074d6d55419609ae63048a60 ',")

# ------------------------------------------------- ------------------------------

                elif text.lower () == ' Look black ':

                    if msg._from in bot1:

                        if settings ["blacklist"] == {}:

                            line.sendMessage (msg.to, "Tidak Ada Banlist")

                        else:

                            line.sendMessage (msg.to, " black list ")

                            num = 1

                            msgs = "??????????Blacklist????????? list "

                            for mi_d in settings ["blacklist"]:

                                msgs + = "\ n [% i]% s"% (num, line.getContact (mi_d) .displayName)

                                num = (num + 1)

                            msgs + = "\ n?????????? Blacklist????????? list \ n \ nTotal Blacklist:% i"% len (settings ["blacklist"])

                            line.sendMessage (msg.to, msgs)

# ===================================================== ==========================================

                elif msg.text.lower (). startswith ("urban"):

                    sep = msg.text.split ("")

                    judul = msg.text.replace (sep [0] + "", "")

                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)

                    with requests.session () as s:

                        s.headers ["User-Agent"] = random.choice (settings ["userAgent"])

                        r = s.get (url)

                        data = r.text

                        data = json.loads (data)

                        y = "[Result Urban]"

                        y + = "\ nTags:" + data ["tags"] [0]

                        y + = "," + data ["tags"] [1]

                        y + = "," + data ["tags"] [2]

                        y + = "," + data ["tags"] [3]

                        y + = "," + data ["tags"] [4]

                        y + = "," + data ["tags"] [5]

                        y + = "," + data ["tags"] [6]

                        y + = "," + data ["tags"] [7]

                        y + = "\ n [1] \ nAuthor:" + str (data ["list"] [0] ["author"])

                        y + = "\ nWord:" + str (data ["list"] [0] ["word"])

                        y + = "\ nLink:" + str (data ["list"] [0] ["permalink"])

                        y + = "\ nDefinition:" + str (data ["list"] [0] ["definition"])

                        y + = "\ nExample:" + str (data ["list"] [0] ["example"])

                        line.sendMessage (to, str (y))

            elif msg.contentType == 1:

                    if settings ["changePictureProfile"] == True:

                        path = line.downloadObjectMsg (msg_id)

                        settings ["changePictureProfile"] = False                                                                              

                        line.updateProfilePicture (path)                                                                                       

                        line.sendMessage (to, " Profile has been changed successfully ")

                    if msg.toType == 2:

                        if to in settings ["changeGroupPicture"]:

                            path = line.downloadObjectMsg (msg_id)

                            settings ["changeGroupPicture"]. remove (to)

                            line.updateGroupPicture (to, path)

                            line.sendMessage (to, " Group image has been changed successfully ")

            elif msg.contentType == 7:

                if settings ["checkSticker"] == True:

                    stk_id = msg.contentMetadata ['STKID']

                    stk_ver = msg.contentMetadata ['STKVER']

                    pkg_id = msg.contentMetadata ['STKPKGID']

                    ret_ = "??? [Sticker Info]"

                    ret_ + = "\ n? STICKER ID: {}". format (stk_id)

                    ret_ + = "\ n? STICKER PACKAGES ID: {}". format (pkg_id)

                    ret_ + = "\ n? STICKER VERSION: {}". format (stk_ver)

                    ret_ + = "\ n? STICKER URL: line: // shop / detail / {}" .format (pkg_id)

                    ret_ + = "\ n??? [Finish]"

                    line.sendMessage (to, str (ret_))

            elif msg.contentType == 16:

                if settings ["timeline"] == True:

                    msg.contentType = 0

                    msg.text = " Link post \ n" + msg.contentMetadata ["postEndUrl"]

                    line.sendMessage (msg.to, msg.text)             

# ===================================================== ============================= #

        if op.type == 19:

            if lineMID in op.param3:

                settings ["blacklist"] [op.param2] = True

        if op.type == 22:

            if settings ['leaveRoom'] == True:

                line.leaveRoom (op.param1)             

        if op.type == 24:

            if settings ['leaveRoom'] == True:

                line.leaveRoom (op.param1)            

# ===================================================== ============================= #

# ===================================================== ============================= #

        if op.type == 17:

            if op.param2 not in Family:

                if op.param2 in Family:

                    pass

            if RfuProtect ["protect"] == True:

                if settings ["blacklist"] [op.param2] == True:

                    try:

                        line.kickoutFromGroup (op.param1, [op.param2])

                        G = line.getGroup (op.param1)

                        G.preventedJoinByTicket = True

                        line.updateGroup (G)

                    except:

                        try:

                            line.kickoutFromGroup (op.param1, [op.param2])

                            G = line.getGroup (op.param1)

                            G.preventedJoinByTicket = True

                            line.updateGroup (G)

                        except:

                            pass

        if op.type == 19:

            if op.param2 not in Family:

                if op.param2 in Family:

                    pass

                elif RfuProtect ["protect"] == True:

                    settings ["blacklist"] [op.param2] = True

                    random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

                    random.choice (Rfu) .inviteIntoGroup (op.param1, [op.param2])

                elif text.lower (). startswith (' admin '):

                        MENTION = eval (msg.contentMetadata ['MENTION'])

                        inkey = MENTION ['MENTIONEES'] [0] ['M']

                        admin.append (str (inkey))

                        line.sendMessage (to, " privilege added ?")

                elif text.lower (). startswith (' delete admin '):

                        MENTION = eval (msg.contentMetadata ['MENTION'])

                        inkey = MENTION ['MENTIONEES'] [0] ['M']

                        admin.remove (str (inkey))

                        line.sendMessage (to, " privilege deleted ?")

                elif text.lower () == ' check ':

                    if admin == []:

                        line.sendMessage (to, " no power ")

                    else:

                        line.sendMessage (to, "The following is an inspector ")

                        mc = ""

                        for mi_d in admin:

                            mc + = " ? " + line.getContact (mi_d) .displayName + "\ n"

                        line.sendMessage (to, mc)

        if op.type == 13:

            if op.param2 not in Family:

                if op.param2 in Family:

                    pass

                elif RfuProtect ["inviteprotect"] == True:

                    settings ["blacklist"] [op.param2] = True

                    random.choice (Rfu) .cancelGroupInvitation (op.param1, [op.param3])

                    random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

                    if op.param2 not in Family:

                        if op.param2 in Family:

                            pass

                        elif RfuProtect ["inviteprotect"] == True:

                            settings ["blacklist"] [op.param2] = True

                            random.choice (Rfu) .cancelGroupInvitation (op.param1, [op.param3])

                            random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

                            if op.param2 not in Family:

                                if op.param2 in Family:

                                    pass

                                elif RfuProtect ["cancelprotect"] == True:

                                    settings ["blacklist"] [op.param2] = True

                                    random.choice (Rfu) .cancelGroupInvitation (op.param1, [op.param3])

 

        if op.type == 11:

            if op.param2 not in Family:

                if op.param2 in Family:

                    pass

                elif RfuProtect ["linkprotect"] == True:

                    settings ["blacklist"] [op.param2] = True

                    G = line.getGroup (op.param1)

                    G.preventedJoinByTicket = True

                    line.updateGroup (G)

                    random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

        if op.type == 5:

            if RfuProtect ["autoAdd"] == True:

                if (settings ["message"] in ["", "", "\ n", None]):

                    pass

                else:

                    line.sendMessage (op.param1, str (settings ["message"]))                   

 

        if op.type == 11:

            if RfuProtect ["linkprotect"] == True:

                if op.param2 not in Family:

                    G = line.getGroup (op.param1)

                    G.preventedJoinByTicket = True

                    random.choice (Rfu) .updateGroup (G)

                    random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param3])                   

 

        if op.type == 13:

           if RfuProtect ["Protectguest"] == True:

               if op.param2 not in Family:

                  random.choice (Rfu) .cancelGroupInvitation (op.param1, [op.param3])

                  random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

 

        if op.type == 17:

           if RfuProtect ["Protectjoin"] == True:

               if op.param2 not in Family:

                   random.choice (Rfu) .kickoutFromGroup (op.param1, [op.param2])

 

        if op.type == 1:

            if sender in Setmain ["foto"]:

                path = line.downloadObjectMsg (msg_id)

                del Setmain ["foto"] [sender]

                line.updateProfilePicture (path)

                line.sendMessage (to, "Foto berhasil dirubah")

 

        if op.type == 26:

            msg = op.message

            text = msg.text

            msg_id = msg.id

            receiver = msg.to

            sender = msg._from

            if msg.toType == 0:

                if sender! = line.profile.mid:

                    to = sender

                else:

                    to = receiver

            else:

                to = receiver

                if settings ["autoRead"] == True:

                    line.sendChatChecked (to, msg_id)                                                       

                if to in read ["readPoint"]:

                    if sender not in read ["ROM"] [to]:

                        read ["ROM"] [to] [sender] = True

                if sender in settings ["mimic"] ["target"] and settings ["mimic"] ["status"] == True and settings ["mimic"] ["target"] [sender] == True:

                    text = msg.text

                    if text is not None:

                        line.sendMessage (msg.to, text)

                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:

                    if 'MENTION' in list (msg.contentMetadata.keys ())! = None:

                        if settings ["kickMention"] == True:

                             contact = line.getContact (msg._from)

                             cName = contact.displayName

                             balas = ["\ n" + cName]

                             ret_ = "" + random.choice (balas)

                             name = re.findall (r '@ (\ w +)', msg.text)

                             mention = ast.literal_eval (msg.contentMetadata ['MENTION'])

                             mentionees = mention ['MENTIONEES']

                             for mention in mentionees:

                                   if mention ['M'] in lineMID:

                                          line.sendMessage (msg.to, ret_)

                                          line.kickoutFromGroup (msg.to, [msg.from_])

                                          break

                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:

                    if "MENTION" in list (msg.contentMetadata.keys ())! = None:

                         if settings ['potoMention'] == True:

                             contact = line.getContact (msg._from)

                             cName = contact.pictureStatus

                             balas = ["http://dl.profile.line-cdn.net/" + cName]

                             ret_ = random.choice (balas)

                             mention = ast.literal_eval (msg.contentMetadata ["MENTION"])

                             mentionees = mention ["MENTIONEES"]

                             for mention in mentionees:

                                   if mention ["M"] in lineMID:

                                          line.sendImageWithURL (to, ret_)

                                          break 

                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:

                    if "MENTION" in list (msg.contentMetadata.keys ())! = None:

                         if settings ['detectMention'] == True:

                             contact = line.getContact (msg._from)

                             cName = contact.displayName

                             balas = ["\ n" + cName]

                             ret_ = "" + random.choice (balas)

                             name = re.findall (r '@ (\ w +)', msg.text)

                             mention = ast.literal_eval (msg.contentMetadata ["MENTION"])

                             mentionees = mention ['MENTIONEES']

                             for mention in mentionees:

                                   if mention ['M'] in lineMID:

                                          line.sendMessage (to, ret_)

                                          line.sendMessage (to, str (settings ["man3"]))

                                          #sendMessageWithMention (to, contact.mid)

                                          line.sendMessage (msg.to, None, contentMetadata = {"STKID": "51626512", "STKPKGID": "11538", "STKVER": "1"}, contentType = 7)

                                          break

                if msg.text in [ "me", " trademark ", "Me", ". The Bangkok ", "! me", " / me"]:.

                    line.sendText (msg.to, " Check all day, all night, hahaha")

                if msg.text in ["speed", "sp", "Speed", " Speed ", "! speed", "/ speed"]:

                    line.sendText (msg.to, " This strong, like M. ??")

                if msg.text in [ " eat rice ", " eat it all ," " eat well ", " meal to anyone ", " eat it too ", " I can not go ". " Have you eaten? "]:

                    line.sendText (msg.to, " Still waiting for someone to enter !!")

                if msg.text in ["555", "5555", "55555", "55 +", "55 ++", "555 +", "555 ++", "5555 +", "5555 ++" ]:

                    line.sendText (msg.to, " Emma said to the doctor that I think ").                                                        

                if msg.text in dangerMessage:

                    random.choice (Rfu) .kickoutFromGroup (receiver, [sender])

                    random.choice (Rfu) .sendText (msg.to, " The bot command delete the M Bot Self group needs to be removed for members ' safety ( ? ?? ?´)")                                                                                                                                             

        if op.type == 17:

          if settings ["Wc"] == True:

            if op.param2 in bot1:

                return

            ginfo = line.getGroup (op.param1)

            contact = line.getContact (op.param2)

            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus

            Line.sendText (Op.param1, "" +, Line.getContact (Op.param2) .displayName +, " ? " +, the str (Ginfo.name) +, " ? " "\ the n \ the n" +, the str (Settings [ "Man1". ]))

            line.sendImageWithURL (op.param1, image)

            line.sendContact (op.param1, op.param2)         

 

# ----------------- NOTIFED MEMBER OUT GROUP

        if op.type == 15:

          if settings ["Wc"] == True:

            if op.param2 in bot1:

                return

            ginfo = line.getGroup (op.param1)

            contact = line.getContact (op.param2)

            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus

            Line.sendText (Op.param1, "" +, Line.getContact (Op.param2) .displayName +, " ? " +, the str (Ginfo.name) +, " ? " "\ the n \ the n" +, the str (Settings [ "MAN2". ]))

            line.sendImageWithURL (op.param1, image)

            line.sendContact (op.param1, op.param2)        

        if op.type == 55:

            try:

                if RfuCctv ['cyduk'] [op.param1] == True:

                    if op.param1 in RfuCctv ['point']:

                        Name = line.getContact (op.param2) .displayName

                        if Name in RfuCctv ['sidermem'] [op.param1]:

                            pass

                        else:

                            RfuCctv ['sidermem'] [op.param1] + = "\ n??" + Name

                            pref = [ ' Hello readers ? ', ' in between ! .. eh !! ?? .. ? ', ' good thread ?? ? ', ' M not see me .. ?? ? ', ' secretly. a mule ? Come to talk ? ',' secretly play with my boyfriend ?? ? ',' M know that I read ?? ? ',' play hide secretly? ?? ? ',' come to talk to him ? '' Naen?ne secretly for Raaa ? '].

                            line.sendMessage (op.param1, str (random.choice (pref)) + '' + Name)

                    else:

                        pass

                else:

                    pass

            except:

                pass

 

        if op.type == 55:

            try:

                if RfuCctv ['cyduk'] [op.param1] == True:

                    if op.param1 in RfuCctv ['point']:

                        Name = line.getContact (op.param2) .displayName

                        if Name in RfuCctv ['sidermem'] [op.param1]:

                            pass

                        else:

                            RfuCctv ['sidermem'] [op.param1] + = "\ n ? " + Name + "\ n????????????????? ? "

                            if "" in Name:

                                          nick = Name.split ('')

                            if len (nick) == 2:

                                          line.sendMessage (op.param1, "Nah" + nick [0])

                            summon (op.param1, [op.param2])

                    else:

                        pass

                else:

                    pass

            except:

                pass

        if op.type == 55:

            print ("[55] Message detected ")

            try:

                if op.param1 in read ['readPoint']:

                    if op.param2 in read ['readMember'] [op.param1]:

                        pass

                    else:

                        read ['readMember'] [op.param1] + = op.param2

                    read ['ROM'] [op.param1] [op.param2] = op.param2

                    backupData ()

                else:

                   pass

            except:

                pass

    except Exception as error:

        logError (error)

# ===================================================== ============================= #

while True:

    try:

        ops = oepoll.singleTrace (count = 50)

        if ops is not None:

            for op in ops:

                lineBot (op)

                oepoll.setRevision (op.revision)

    except Exception as e:

        logError (e)

 