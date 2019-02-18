# -*- coding: utf-8 -*-
import tweepy
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
import itertools
import threading
import time
import sys

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rBağlantı gerçekleştiriliyor ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

def animate2():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rKullanıcı bilgisi getiriliyor... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)



cprint(figlet_format('enesilhaydin', font='small'),
        attrs=['bold'])

print("twitter/enesilhaydin \n ======================")


consumer_key=input("Consumer key'i giriniz = ")
consumer_secret=input("Consumer Secret'i giriniz = ")
#access_token=input("Access Token'i giriniz = ")
#access_token_secret=input("Access Token Secret'i giriniz = ")


done = False
t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done = True

print("\n ===========================")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class global_Yap:
    global kullanici_kontrol
    def kullanici_kontrol():
        while True:
            try:
                kullanici_adi=input("\n\033[0;31;40m Arama yapılacak kullanıcı adını giriniz = ")
                user = api.get_user(kullanici_adi)
                return user,kullanici_adi
                break


            except tweepy.TweepError as e:
                print("Böyle bir kullanıcı bulunmamaktadır.")
                print("Lütfen tekrar giriniz...")




user,kullanici_adi=kullanici_kontrol()

done = False
t = threading.Thread(target=animate2)
t.start()
time.sleep(3)
done = True

print ("\n",kullanici_adi,"Kullanıcısının toplam takipci sayısı = ",(user.followers_count))

friend_ids = api.friends_ids(kullanici_adi);
followers_ids = api.followers_ids(kullanici_adi)

print("=====================")
print("Takip'e Takip yaptığı düşünülen takipçiler listesi...")
sayac=0;
for takipciler in followers_ids:
    user_follower = api.get_user(id=takipciler);
    takipci_sayisi = (user_follower.followers_count)
    takip_edilen_sayisi = (user_follower.friends_count);
    oran = takip_edilen_sayisi/takipci_sayisi

    if ( takip_edilen_sayisi > 1000 and oran>0.80 and oran<1.25) :
        sayac=sayac+1
        print(sayac," =",user_follower.screen_name)
        #api.create_block(id=takipciler)
        #print(takipciler," kullanicisi engellendi.")
        #print("===")
