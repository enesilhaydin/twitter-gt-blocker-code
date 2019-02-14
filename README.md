# twitter-gt-blocker-code
Twitter takipçileri arasında takip'e takip profil tespit eden, istenildiğinde bunları komple engelleyen kod parçası.

API KEY'lerinizi https://developer.twitter.com/ üzerinden alabilirsiniz.

İstenildiğini taktikte takip'e takip yapan kullanıcıları bulan fonksyiyonu değiştirebilirsiniz. Şuanda kullanılan takipci sayısı 1000'den büyük ve takip/takipçi oranı 0.8 ile 1.25 arasındaki kullanıcıları listeleyen fonksyiondur.

Eğer bu kullanıcıları komple engellemek istiyorsanız...Aşağıdaki yorum satırını normal hale getirmeniz gerekmektedir.

#api.create_block(id=takipciler)
        #print(takipciler," kullanicisi engellendi.")
        #print("===")
