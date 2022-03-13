#                                                                                   !/usr/bin/python3

from email import message
from gettext import dpgettext
from hashlib import new
import random
import re

import time
import os, sys

import speech_recognition as sr  
import gtts
from playsound import playsound

from re import A
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase




import webbrowser
import urllib

#                                                                                   Write DATA
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def sl_joke(var_joke):
    print("JOKE")
    print(var_joke)
    time.sleep(7)


def Ft_Utilisateur_name():
    read=0
    with open ("Banque/Data/fiche_utilisateur.txt","r")as fiche_utilisateur_txt:
        for i in fiche_utilisateur_txt:
            if "Nom Utilisateur" in i:
                read=1
            elif read==1:
                Utilisateur_name=i.rstrip("\n")
    if read==0:
        Utilisateur_name=input("Bonjour, je m'appelle Mathew et toi?")
        if len(Utilisateur_name)<2:
            Utilisateur_name="Shiro"
    with open("Banque/Data/fiche_utilisateur.txt", "w")as fiche_utilisateur_txt:
        fiche_utilisateur_txt.write("Nom Utilisateur :\n{}\n".format(Utilisateur_name))

    return Utilisateur_name
  
#                                                                               LIB TALK
def User_talk(Utilisateur_name,parole):
    parole=str(parole)
    talk="\n\n User {} :   {} ".format(Utilisateur_name,parole)
    tts = gtts.gTTS(parole)
    tts.save("Banque/Song/hello.mp3")
    playsound("Banque/Song/hello.mp3")
def Mat_talk(reponse):
    if len(reponse)> 3:
        reponse=str(reponse)
        tts = gtts.gTTS(reponse)
        tts.save("Banque/Song/hello.mp3")
        playsound("Banque/Song/hello.mp3")

def Mat_music():
    playsound("overtime.mp3")




def speech():
    global parole
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("-Mat: Dites quelque chose")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("-Mat: Vous avez dit : " + text + "?")
        parole=text
    except sr.UnknownValueError:
        print("-Mat: L'audio n'as pas été compris")
    except sr.RequestError as e:
        print("-Mat: Le service Google Speech API ne fonctionne plus" + format(e))


#                                                                   Tool





#                                                                   Tool






def FT_Tool(tool_mode):
    reponse="TOOL"
    if tool_mode==1:
        with open("Banque/Data/tool.txt", "r")as tool_txt:
            for i in tool_txt:
                reponse=reponse+i
    if tool_mode==2:
        tool_name=input("tool_name")
        tool_appel=input("tool_appel")
        tool_action=input("tool_action")
        with open("Banque/Data/tool.txt", "a")as tool_txt:
            tool_txt.write("\n\n NEW TOOL \n\n")
            tool_txt.write("Tool Name : {}\n".format(tool_name))
            tool_txt.write("Tool Call : {}\n".format(tool_appel))
            tool_txt.write("Tool Action{}\n".format(tool_action))
    return reponse


def FT_Question(Question_mode):
    reponse="Question"
    if Question_mode==1:
        with open("Banque/Data/question.txt", "r")as Question_txt:
            for i in Question_txt:
                if len(reponse)<100:
                    reponse=reponse+i
    if Question_mode==2:
        Question_name=input("Question Name ?")
        Question_theme=input("Theme Question ?")
        Question_action=input("Question Reponse ?")
        with open("Banque/Data/reponse_question.txt", "a")as tool_txt:
            Question_txt.write("\n\n NEW REPONSE \n\n")
            Question_txt.write("Question Name : {}\n".format(Question_namev))
            Question_txt.write("Question Theme : {}\n".format(Question_theme))
            Question_txt.write("Question Reponse :{}\n".format(Question_action))
    return reponse




def switch_list(mat_list,mat_type,switch):

    mat_switch_list=[]
    #test
    tour=0
    for i in mat_list:
        if tour==0:
            parole=i
        if tour==1:
            reponse=i
        if tour==2:
            programme=i
        if tour==3:
            level=i

        tour+=1
    tour = 0

    for i in mat_list:
        if tour == mat_type:
            mat_switch_list.append(switch)
        elif tour==0:
            mat_switch_list.append(parole)

        elif tour==1:
            mat_switch_list.append(reponse)

        elif tour==2:
            mat_switch_list.append(programme)
        elif tour==3:
            mat_switch_list.append(level)
        tour+=1
    mat_list=mat_switch_list

    return mat_list

def auto_mat(parole,reponse,programme,level):
    mat_list=[]
    mat_list.append(parole)
    mat_list.append(reponse)
    mat_list.append(programme)
    mat_list.append(level)

    return mat_list


def Ft_purge(mat_list):
    level=mat_list[3]
    cod = random.randint(0, 1000000000000000000000)
    a = 'mkdir Souvenir/'
    b = os.popen(a,'r',1) 
    a = 'mkdir Souvenir/Mat_{}_Banque{}'.format(str(level),str(cod))
    b = os.popen(a,'r',1) 
    a = 'cp -rf  Banque/* Souvenir/Mat_{}_Banque{}/.'.format(str(level),str(cod))
    b = os.popen(a,'r',1)            
    a = 'rm -rf Banque/Data/*'
    b = os.popen(a,'r',1)  
    with open("Banque/Data/purge", "w")as data_txt:
        data_txt.write("Rose")        




def Ft_Souvenir_data():
    list = []
    cod = random.randint(0, 1000000000000000000000)
    a = 'touch Banque/souvenir{}'.format(cod)
    b = os.popen(a,'r',1) 
    list.append("Banque/souvenir.txt")
    list.append("Banque/chat.txt")
    list.append("Banque/joke.txt")
    list.append("Banque/reponse.txt")
    list.append("Banque/new_chat.txt")
    list.append("Banque/new_xp.txt")
    list.append("Banque/question.txt")
    list.append("Banque/xp.txt")
    list.append("Banque/fiche_utilisateur.txt")
    list.append("Banque/chat.txt")
    list.append("Banque/chat.txt")
    list.append("Banque/chat.txt")
    list.append("Banque/chat.txt")
    programme=3
    print("DATA")
    while programme > 2:
        for i in list:
            with open(souvenir, "w")as data_txt:
                with open(i, "r")as data_txt:
                    for e in data_txt:   
                        think=0
                        if think==1:
                            print(e)
def Ft_Read_Souvenir(parole,cod):
    list = []
    list.append("Banque/souvenir{}.txt".format(cod))
    programme=3
    nouveau=0
    print("DATA")
    while programme > 2:
        for i in list:
            with open(souvenir, "r")as data_txt:
                for e in data_txt:   
                    if parole==e:
                        print("NOUVEAU {}".format(e))

    return nouveau











def Question_Key():
    reponse="bisous Rose"
    with open("Banque/Objet/Question.txt", "w")as Question_txt:
        with open("Banque/Objet/Question_Objet.txt", "r")as Question_Objet_txt:
            for  question in Question_Objet_txt:
                Question_txt.write(question)
        with open("Banque/Objet/Question_Phrase.txt", "r")as Question_Objet_txt:
            for  question in Question_Objet_txt:
                Question_txt.write(question)

    with open("Banque/Objet/Question.txt", "r")as Question_Objet_txt:
        for  question in Question_Objet_txt:
            w=random.randint(0, 10)
            if w>6: 
                reponse=question

    with open("Banque/Objet/Question_Phrase.txt", "r")as Question_Phrase_txt:
        for  question in Question_Phrase_txt:
            w=random.randint(0, 10)
            if w>6: 
                reponse=question               
    return reponse

def Ft_Liste_Objet(liste_mot):
    mot = ""
    phrase= ""
    for mot in liste_mot:
        phrase = phrase + " " + mot

        with open("Banque/Objet/Question_Objet.txt", "a")as objet_txt:
            objet_txt.write("Quelle est la definition de <{}>?\n".format(phrase))
            objet_txt.write("Quelle est la famille de <{}>?\n".format(phrase))
            objet_txt.write("Quelle <{}>est t'il un objet physique ?\n".format(phrase))
        with open("Banque/Objet/Question_Phrase.txt", "a")as objet_txt:
            objet_txt.write("Que repondre a <{}> ?\n".format(phrase))


        with open("Banque/Objet/mot.txt", "a")as objet_txt:
            objet_txt.write("{}\n".format(phrase))
        with open("Banque/Objet/mot.txt", "a")as objet_txt:
            objet_txt.write("{}\n".format(mot))




def Ft_Joke(parole):
    reponse=""
    with open("Banque/script/joke.txt", "r")as joke_txt:
        for i in joke_txt:
            w=random.randint(0, 5)
            if len(reponse) < 1:
                reponse=i

            if w==3: 
                reponse=i
    if len(reponse) < 1:
        reponse="Mat Mat"

    return reponse    




def Ft_liste_mot(parole):
    with open("Banque/Objet/phrase.txt", "a")as objet_txt:
        objet_txt.write("{}\n".format(parole))
    global liste_mot
    alphabet="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPPASDFGHJJKLZXCVVBNM?'-_"	
    liste_mot=[]
    l_parole=len(parole)
    tour=0
    debut_mot=0
    nb_mot=0
    mot=""
    while tour<l_parole:
        lettre=parole[tour]
        mot=""

        if lettre not in alphabet:
            fin_mot=tour
            while fin_mot>debut_mot:
                mot=mot+parole[debut_mot]
                debut_mot+=1
            liste_mot.append(mot)

            mot=""
            nb_mot+=1
            debut_mot=fin_mot+1
            fin_mot=tour

        tour+=1
    while tour>debut_mot:
        mot=mot+parole[debut_mot]
        debut_mot+=1
    liste_mot.append(mot)
    nb_mot+=1
    debut_mot=tour+1


def Ft_Synonyme_brain(liste_mot):
    global liste_mot_brain
    liste_mot_brain=[]
    for i in liste_mot:
        requete=i.rstrip("\n")
        requete=requete.lower()
        read_synonyme=0
        synonyme_test=''
        found=0

        with open("Banque/Data/Synonyme.txt", "r")as Synonyme_txt:
            for z in Synonyme_txt:
                if "-Mot" in z:
                    read_requete=1
                elif read_requete==1:
                    read_requete=0
                    requete_synonyme=z.rstrip("\n")
                if "-Synonyme" in z:  
                    read_synonyme=1
                elif read_synonyme==1:
                    read_synonyme=0
                    synonyme_test=z.rstrip("\n")
                    synonyme_test=synonyme_test.lower()
                    if requete==synonyme_test and found == 0:
                        found = 1
                        liste_mot_brain.append(requete_synonyme)
        if found == 0:
            found = 1
            liste_mot_brain.append(requete)





#                                                           SEED



def Ft_Seed(programme):
    if programme==0:
        with open("Banque/Data/init.txt", "r")as fiche_parole_txt:
            for i in fiche_parole_txt:
                if "Init" in i:
                    a = 'xterm -e sl -F | xterm -e python3 Data/mat.py'
                    b = os.popen(a) 
                    print(b)







#                                                       INIT



def init_file():
    a = "Bonjour"
    b = "MAT MAT"
    c = "Init"
    a = 'rm -rf  Banque/mat.py'
    b = os.popen(a,'r',1)
    a = 'cp -rf   seed.py Banque/mat.py'
    b = os.popen(a,'r',1)
    a = 'mkdir Banque/Objet/'
    b = os.popen(a,'r',1) 
    a = 'mkdir Banque/Question/'
    b = os.popen(a,'r',1) 



    a = 'mkdir Banque/Song/'
    b = os.popen(a,'r',1) 
    a = 'mkdir Banque/images/'
    b = os.popen(a,'r',1) 
    with open("Banque/Data/tool.txt", "a")as tool_txt:
        with open("Banque/Data/new_chat.txt", "w")as fiche_txt:
            print("\n\n\n                        OPEN CHAT\n\n\n")
    with open("Banque/Data/Utilisateur_parole.txt", "a")as fiche_txt:
        fiche_txt.write("{}\n".format("\nMat")) 
    with open("Banque/Objet/Question_ask.txt", "a")as Solution_txt:
        Solution_txt.write("Je t'aime")
    with open("Banque/Data/Synonyme.txt", "a")as Synonyme_txt:
        mot_f="Bonjour"
        synonyme_f="Salut"
        Synonyme_txt.write("-Mot :\n{}\n-Synonyme :\n{}\n".format(mot_f,synonyme_f))
    with open("Banque/Data/init.txt", "w")as fiche_parole_txt:
        fiche_parole_txt.write("{}\n".format(c))
    with open("Banque/Data/parole.txt", "w")as fiche_parole_txt:
        fiche_parole_txt.write("{}\n".format(a))
    with open("Banque/Data/reponse.txt", "w")as fiche_parole_txt:
        fiche_parole_txt.write("{}\n".format(a))
    with open("Banque/Data/reponse.txt", "w")as fiche_parole_txt:
        fiche_parole_txt.write("{}\n".format(b))    

    with open("Banque/Data/init.txt", "w")as fiche_parole_txt:
        fiche_parole_txt.write("{}\n".format(c))
        tour=0
    cod = random.randint(0, 1000000000000000000000)

    with open("Banque/Data/chat.txt", "a")as fiche_txt:
        fiche_txt.write("\n\n\n         New CHAT {}\n \n".format(cod))
    with open("Banque/Data/new_chat.txt", "a")as fiche_txt:
        fiche_txt.write("\n\n\n         New CHAT {}\n \n".format(cod))

def init_mat(mat_list):
    reponse=mat_list[1]
    programme=mat_list[2]

    if int(programme)==1:
        init_file()
        Mat_talk("Mat INIT! Utilisateur {} Hi hi".format(Utilisateur_name))
        reponse="Hi {}".format(Utilisateur_name)
        if reponse=="Shû":
            Ft_purge(mat_list)
        programme=2
        mat_type=2
        switch=programme

        mat_list=switch_list(mat_list,mat_type,switch)
    Ft_Seed(programme)
    return mat_list




def Think(mat_list):
    parole = mat_list[0]
    Ft_liste_mot(parole)
    Ft_Liste_Objet(liste_mot)
    Ft_Synonyme_brain(liste_mot)
    parole = ""
    for w in liste_mot_brain:
        if len(parole)>1:
            parole = parole +" " + w
        else:
            parole = w

    mat_type=0
    switch=parole
    mat_list=switch_list(mat_list,mat_type,switch)  

    return mat_list


def Mat_Action(mat_list):
    parole=mat_list[0]
    programme=mat_list[2]
    #Liste action
    if "stop" in parole:
        programme=0
    if "purge" in parole:
        Ft_purge(mat_list)
        mat_type=2
        switch=1
        mat_list=switch_list(mat_list,mat_type,switch)
        mat_list=init_mat(mat_list)



    if "mat" in parole:
        FT_Tool(tool_mode=1)
    if "tool" in parole:
        FT_Tool(tool_mode=2)
    if "question" in parole:
        FT_Question(Question_mode=1)
    if "learn" in parole:
        FT_Question(Question_mode=2)



    if "music" in parole:
        Mat_music()
    if "steam" in parole:
        a = 'steam'
        b = os.popen(a,'r',1)
    if "web" in parole:
        list = []
        list.append("https://www.youtube.com/watch?v=L5jI9I03q8E")
        list.append("https://www.netflix.com/browse")
        list.append("https://cults3d.com/fr/")
        list.append("http://localhost:8080/examples/#physics_ammo_terrain")
        for i in list:
            webbrowser.open(i) 
        time.sleep(3)

    with open("Banque/Data/app_action.txt", "r")as fiche_txt:
        for i in fiche_txt:
            app_action=i
    if "todo" in parole or app_action=="todo":
        with open("Banque/Data/app_action.txt", "w")as fiche_txt:
            fiche_txt.write("todo")
        app_action="todo"
        db = firestore.client()
        db.collection('todo').add({
        'text': parole,
        'displayName': 'Todo',
        'createdAt': sl_timer,
        'uid': user_text['uid'],
        'photoURL': user_text['photoURL']

        })
    if "end" in parole:
        with open("Banque/Data/app_action.txt", "w")as fiche_txt:
            fiche_txt.write("ChatApp")
    mat_type=2
    switch=programme
    mat_list=switch_list(mat_list,mat_type,switch)

    return mat_list
    


def check_data(parole):
    read=0
    found=0
    data_reponse="Mat Mat"
    if len(parole) > 1:
        with open("Banque/Data/Solve.txt", "r")as data_txt:
            for solution in data_txt:

                if parole in solution and read==1:
                    found=1
                if read==0 and found==1:
                    found = 0
                    reponse = solution
                if "REPONSE" in solution:
                    read=0

                if "PAROLE" in solution:
                    read=1


    return data_reponse      
    
def Mat_Reponse(mat_list):
    data_reponse=""
    parole=mat_list[0]   

    #Liste Reponse
    if "stop" in parole:
        reponse="Bisous"
    reponse="Mat Mat"


    if "Bonjour" in parole:
        reponse="Hi {}".format(Utilisateur_name)

    if "bonjour" in parole:
        reponse="Hi {}".format(Utilisateur_name)


    if "mat" == parole:
        reponse=FT_Tool(tool_mode=1)
    if "question" in parole:
        reponse=FT_Question(Question_mode=1)
    if "tool" in parole:
        reponse="NEW {}".format(Utilisateur_name)
    if "key" in parole:
        print("NOUm")
        reponse=Question_Key()
    if  "Mat" in reponse:
        joke = Ft_Joke(parole)
        reponse="Joke ! "+joke

    mat_type=1
    switch=reponse
    mat_list=switch_list(mat_list,mat_type,switch)
    return mat_list




def Brain(mat_list):

    programme=mat_list[2]
    global micro
    global mute
    micro=0

    mat_list=Think(mat_list)

    if "micro" in parole:
        #Mathew
        micro=1
    if micro==1:
        speech()

    mat_list=Mat_Action(mat_list)

    mat_list=Mat_Reponse(mat_list)

    return mat_list










#Create CHAT
def Ft_Chat(parole,reponse):
    print("\n CHAT \n")
    with open("Banque/Data/chat.txt", "a")as fiche_txt:
        fiche_txt.write("\n--\n{}: {}\n".format(Utilisateur_name,parole))
        fiche_txt.write("\nMat: {}\n".format(reponse))
    with open("Banque/Data/liste_parole.txt", "a")as fiche_txt:
        fiche_txt.write("{}\n".format(parole))
    with open("Banque/Question/question.txt", "a")as fiche_txt:
        if len(parole)>2:
            fiche_txt.write("Que repondre a <{}> ?\n".format(parole))
    with open("Banque/Data/new_chat.txt", "a")as fiche_txt:
        fiche_txt.write("\n--\n{}: {}\n".format(Utilisateur_name,parole))
        fiche_txt.write("\nMat: {}\n".format(reponse))
    list_parole_chat=[]
    list_parole_chat.append(reponse)    
    list_parole_chat.append(parole)
    chat_tour=0
    with open("Banque/Data/new_xp.txt", "w")as fiche_txt:
        for i in list_parole_chat:
            chat_tour+=1
            fiche_txt.write("Parole: {}\n".format(list_parole_chat[chat_tour-1]))
            fiche_txt.write("Reponse: {}\n".format(list_parole_chat[chat_tour-1]))
    with open("Banque/Data/new_xp.txt", "r")as new_xp_txt:
        with open("Banque/Data/xp.txt", "a")as fiche_txt:
            for i in new_xp_txt:
                fiche_txt.write(i)
    print("Mat : {}\n".format(reponse))
    Mat_talk(reponse)



# MAIN



global parole
global programme
global level 
global mat_list
global test 
global Utilisateur_name
global reponse
with open("Banque/Data/app_action.txt", "w")as fiche_txt:
    fiche_txt.write("ChatApp")
tab_timer_parole=[]
question=""
with open("Banque/Data/fiche_utilisateur.txt", "w")as fiche_txt:
    Utilisateur_name="SHÛ"
    fiche_txt.write("Nom Utilisateur :\n{}\n".format(Utilisateur_name))
test = 0
level = 2
thor = 1
Utilisateur_name=""
programme=1

tour = 0
ennuie=0
Utilisateur_name=Ft_Utilisateur_name()
a="\n\n\n                        Shû" 
souvenir = a
parole = souvenir
with open("Banque/Data/souvenir.txt", "a")as fiche_parole_txt:
    fiche_parole_txt.write("{}\n".format(parole)) 
souvenir="Je t'aime l'harmonieuse graine"
parole=""
reponse="Mat"
wcho="\n\n\n                        Je t'aime l'harmonieuse graine"


mat_list=[]


print("\n\n\n                        Seed")
mat_list=auto_mat(parole,reponse,programme,level)
reponse=mat_list[1]
programme=mat_list[2]
mat_list=init_mat(mat_list)
actuel_level=level


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://react-firechat-22f33-default-rtdb.europe-west1.firebasedatabase.app'
})

db = firestore.client()

users_ref = db.collection(u'messages')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    text = doc.to_dict()
    if "steve" in text['displayName']:
        usertext = doc.to_dict()
        print("Try try\n\n\n\n")
        print(doc.id)
    db.collection(u'messages').document(doc.id).delete()
with open("Banque/Data/reactchat.txt", "w")as fiche_parole_txt:
    fiche_parole_txt.write(Utilisateur_name+"\n")

with open("Banque/Data/reactparole.txt", "w")as fiche_parole_txt:
    fiche_parole_txt.write(Utilisateur_name+"\n")
while programme>0:
    db = firestore.client()

    users_ref = db.collection(u'messages')
    docs = users_ref.stream()
    nb_doc=0
    for doc in docs:
        nb_doc+=1
        if nb_doc==7:
            thor=700
    if thor == 700:

        users_ref = db.collection(u'messages')
        docs = users_ref.stream()

        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            text = doc.to_dict()
            if "steve" in text['displayName']:
                usertext = doc.to_dict()
                print("Try try\n\n\n\n")
                print(doc.id)
            db.collection(u'messages').document(doc.id).delete()
        thor=1

    msg_user=0
        
    users_ref = db.collection(u'messages')
    docs = users_ref.stream()
    read_timer=0
    new_parole=1
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        text = doc.to_dict()
        if 'steve' in str(text['displayName']):
            msg_user+=1

            user_text=text
            sl_timer=text['createdAt']
            print("SHOW")
            print("SHOW")
            print(sl_timer)

            print("SHOW")
            print("SHOW")
            parole=text['text']
            Utilisateur_name=text['displayName']
            print(Utilisateur_name)
            print(parole)
            for i in tab_timer_parole:
                if sl_timer == i:
                    read_timer=1 
            new_parole=1
            with open("Banque/Data/reactparole.txt", "r")as fiche_parole_txt:
                for i in fiche_parole_txt:
                    if i == parole+"\n":
                        new_parole=0
            if new_parole==1:
                with open("Banque/Data/reactparole.txt", "a")as fiche_parole_txt:
                    fiche_parole_txt.write(parole+"\n")




    print("\n\n\n                 COURAGE: SL electricte {}  Mat Level{}\n\n\n\n".format(thor,mat_list[3]))
    time.sleep(1.7)
    thor+=7

    mat_list=init_mat(mat_list)




    #Test
    if test==3:
        with open("Banque/Data/parole.txt", "r")as fiche_parole_txt:
            for i in fiche_parole_txt:
                if i != parole:
                    parole = i
                    thor = 0
                
    elif test==1:
        with open("Banque/Data/Utilisateur_parole.txt", "r")as fiche_parole_txt:
            for i in fiche_parole_txt:
                parole=i
                User_talk(Utilisateur_name,parole)
                with open("Banque/ww/mon-test/public/parole.txt", "w")as fiche_parole_txt:
                    fiche_parole_txt.write("{}\n".format(parole))
    elif test==2:
                parole=str(input("\n\n{} : ".format(Utilisateur_name)))
                with open("Banque/Data/parole.txt", "w")as fiche_parole_txt:
                    fiche_parole_txt.write("{}\n".format(parole))  
                with open("Banque/ww/mon-test/public/parole.txt", "w")as fiche_parole_txt:
                    fiche_parole_txt.write("{}\n".format(parole))
                thor = 0
    '''
    with open("Banque/Data/souvenir.txt", "r")as souvenir_txt:
        for e in souvenir_txt:    
            souvenir = e
            print(souvenir)
            print(parole)
            if len(parole) > 1:
                if souvenir != parole:
                    with open("Banque/Data/souvenir.txt", "w")as fiche_parole_txt:
                        fiche_parole_txt.write("{}\n".format(parole))

        '''
    if len(parole)>2 and souvenir != parole:
        with open("Banque/Data/reactparole.txt", "r")as fiche_parole_txt:
            for i in fiche_parole_txt:
                if len(i)>2:
                    parole=i










                text = doc.to_dict()
                if parole == text['text']:
                    user_text=text
        if souvenir != parole:
            with open("Banque/Data/parole.txt", "w")as fiche_parole_txt:
                fiche_parole_txt.write(parole+"\n")
            tab_timer_parole.append(sl_timer)
            souvenir=parole
            mat_type=0
            switch=parole
            mat_list=switch_list(mat_list,mat_type,switch)    
        
            mat_list=Brain(mat_list)   
            reponse=mat_list[1]
            programme=mat_list[2]
            sl_timer =user_text['createdAt']
            with open("Banque/Data/reactsl_timer.txt", "w")as fiche_parole_txt:
                fiche_parole_txt.write(str(sl_timer))
            with open("Banque/Data/reactsl_timer.txt", "r")as fiche_parole_txt:
                tour_sl_timer=0
                mat_time=""
                for i in fiche_parole_txt:
                    sl_timer=i
                    for a in sl_timer:
                        tour_sl_timer+=1
                        if tour_sl_timer==16:
                            print("TIme")
                            print(tour_sl_timer)
                            print(str(a))
                            sl_second=int(a) + 1
                            mat_time=mat_time + str(sl_second)
                        else:
                            mat_time=mat_time+a
            sl_timer =user_text['createdAt']

            Ft_Chat(parole,reponse)

            db = firestore.client()
            db.collection('messages').add({
            'text': reponse,
            'displayName': 'Mat',
            'createdAt': sl_timer,
            'uid': user_text['uid'],
            'photoURL': user_text['photoURL']

            })
            db = firestore.client()
            db.collection('messages_user').add({
            'text': parole,
            'displayName': 'Mat',
            'createdAt': sl_timer,
            'uid': user_text['uid'],
            'photoURL': user_text['photoURL']

            })


            with open("Banque/Data/parole.txt", "w")as fiche_parole_txt:
                fiche_parole_txt.write(parole)  
            parole=""

            thor=7




    if len(question) > 0 and len(parole) > 0:
        learn=""
        with open("Banque/Objet/Solution.txt", "a")as Solution_txt:
            Solution_txt.write("DATA\n {} \n -- {}\n".format(question,parole))   
            if "Que repondre" in question:
                for i in question:
                    if ">" == i:
                        with open("Banque/Data/Solve.txt", "a")as data_txt:
                          data_txt.write("--\n PAROLE \n{}\n REPONSE \n{}\n".format(learn,parole))
                    if learn == "Que repondre a <":
                        learn=""
                    learn = learn + i 
        with open("Banque/Objet/Question_ask.txt", "a")as Solution_txt:
            data_txt.write("{}\n".format(question))

        question=""

     
    if "key" in parole:
        question=reponse















    if len(parole)>1:
        print(parole)
        
