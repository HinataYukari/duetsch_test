#deutsch
from numpy.random import *

q_sentence = {1:"不定詞", 2:"直接法過去", 3:"過去分詞"}
word_list_week = {1:
            {0:["パンを焼く", "backen", "backte", "gebacken"],
            1:["命ずる", "befehlen", "befahl", "befohlen"],
            2:["始める", "beginnen", "begann", "begonnen"],
            3:["かむ", "baißen", "biss", "gebissen"],
            4:["救出する", "bergen", "barg", "geborgen"],
            5:["曲げる", "biegen", "bog","gebogen"],
            6:["提供する", "bieten", "bot", "geboten"],
            7:["結ぶ", "binden", "band", "gebunden"],
            8:["頼む", "bitten", "bat", "gebeten"],
            9:["吹く", "blasen", "blies", "geblasen"],
            10:["とどまる", "bleiben", "blieb", "geblieben"],
            11:["（肉を）焼く", "braten", "briet", "gebraten"],
            12:["折る", "brechen", "brach", "gebrochen"],
            13:["燃やす", "brennen", "brannte", "gebrannt"],
            14:["持ってくる", "bringen", "brachte", "gebracht"],
            15:["考える", "denken", "dachte", "gedacht"],
            16:["突き進む", "dringen", "drang", "gedrungen"],
            17:["〜してもよい", "drüfen", "durfte", "gedurft"],
            18:["勧める", "empfehlen", "empfahl", "empfohlen"],
            19:["驚く", "erschrecken", "erschrak", "erschrocken"],
            20:["食べる", "essen", "aß", "gegessen"],
            21:["（乗り物で）行く", "fahren", "fuhr", "gefahren"],
            22:["落ちる", "fallen", "fiel", "gefallen"],
            23:["捕える", "fangen", "fing", "gefangen"],
            24:["見つける", "finden", "fand", "gefunden"],
            25:["飛ぶ", "fliegen", "flog", "geflogen"],
            26:["逃げる", "fliehen", "floh", "geflohen"],
            27:["流れる", "fließen", "floss", "geflossen"],
            28:["（動物が）食う", "fressen", "fraß", "gefressen"],
            29:["凍える", "frieren", "fror", "gefroren"],
            30:["産む", "gebären", "gebar", "geboren"],
            31:["与える", "geben", "gab", "gegeben"],
            32:["行く", "gehen", "ging", "gegangen"],
            33:["成功する", "gelingen", "gelang", "gelungen"],
            34:["通用する", "gelten", "galt", "gegolten"],
            35:["楽しむ", "genießen", "genoss", "genossen"],
            36:["起こる", "geschehen", "geschah", "geschehen"],
            37:["獲得する", "gewinnen", "gewann", "gewonnen"],
            38:["注ぐ", "gießen", "goss", "gegossen"],
            39:["似ている", "gleichen", "glich", "geglichen"],
            40:["すべる", "gleiten", "glitt", "geglitten"],
            41:["掘る", "graben", "grub", "gegraben"],
            42:["つかむ", "greifen", "griff", "gegriffen"],
            43:["持っている", "haben", "hatte", "gehabt"],
            44:["保つ", "halten", "hielt", "gehalten"],
            45:["掛かっている", "hängen", "hing", "gehangen"],
            46:["持ち上げる", "heben", "hob", "gehoben"],
            47:["〜と言う名である", "heißen", "hieß", "geheißen"]
            },
            2:
            {0:["助ける","helfen","half","geholfen"],
            1:["知っている","kennen","kannte","gekannt"],
            2:["鳴る","klingen","klang","geklungen"],
            3:["来る","kommen","kam","gekommen"],
            4:["〜できる/〜かもしれない","ko^nnen","konnte","gekonnt"],
            5:["はう","kriechen","kroch","gekrochen"],
            6:["積み込む","laden","lud","geladen"],
            7:["させる","lassen","ließ","gelassen"],
            8:["走る","laufen","lief","gelaufen"],
            9:["苦しむ","leiden","litt","gelitten"],
            10:["貸す","leihen","lieh","geliehen"],
            11:["読む","lesen","las","gelesen"],
            12:["横たわる","liegen","lag","gelegen"],
            13:["嘘をつく","lu^gen","log","gelogen"],
            14:["避ける","meiden","mied","gemieden"],
            15:["測る","messen","maß","gemessen"],
            16:["〜かもしれない/好む","mo^gen","mochte","gemocht"],
            17:["〜ねばならない/〜に違いない","mu^ssen","musste","gemusst"],
            18:["取る","nehmen","nahm","genommen"],
            19:["名付ける","nennen","nannte","genannt"],
            20:["笛を吹く","pfeifen","pfiff","gepfiffen"],
            21:["褒める","preisen","pries","gepriesen"],
            22:["忠告する","raten","riet","geraten"],
            23:["こする","reiben","rieb","gerieben"],
            24:["裂く","reißen","riss","gerissen"],
            25:["馬で行く","reiten","ritt","geritten"],
            26:["駆ける","rennen","rannte","gerannt"],
            27:["におう","riechen","roch","gerochen"],
            28:["格闘する","ringen","rang","gerungen"],
            29:["呼ぶ","rufen","rief","gerufen"],
            30:["創造する","schaffen","schuf","geschaffen"],
            31:["分ける","scheiden","schied","geschieden"],
            32:["輝く","scheinen","schien","geschienen"],
            33:["しかる","schelten","schalt","gescholten"],
            34:["押す","schieben","schob","geschoben"],
            35:["射つ","schießen","schoss","geschossen"],
            36:["眠る","schlafen","schlief","geschlafen"],
            37:["打つ","schlagen","schlug","geschlagen"],
            38:["忍び歩く","schleichen","schlich","geschlichen"],
            39:["閉める","schließen","schloss","geschlossen"],
            40:["溶ける","schmelzen","schmolz","geschmolzen"],
            41:["切る","schneiden","schnitt","geschnitten"],
            42:["書く","schreiben","schrieb","geschrieben"],
            43:["叫ぶ","schreien","schrie","geschrien"],
            44:["歩く","schreiten","schritt","geschritten"],
            45:["黙っている","schweigen","schwieg","geschwiegen"],
            46:["泳ぐ","schwimmen","schwamm","geschwommen"],
            47:["消える","schwinden","schwand","geschwunden"],
            48:["誓う","schwo^ren","schwor","geschworen"],
            },
            3:{
            0:["見る", "sehen", "sah", "gesehen"],
            1:["ある", "sein", "war", "gewesen"],
            2:["送る", "senden", "sandte", "gesandt"],
            3:["歌う", "singen", "sang", "gesungen"],
            4:["沈む", "sinken", "sank", "gesunken"],
            5:["座っている", "sitzen", "saß","gesessen"],
            6:["〜すべきである/〜と言われている", "sollen", "sollte", "gesollt"],
            7:["話す", "sprechen", "sprach", "gesprochen"],
            8:["跳ぶ", "springen", "sprang", "gesprungen"],
            9:["刺す", "stechen", "stach", "gestochen"],
            10:["立っている", "stehen", "stand", "gestanden"],
            11:["盗む", "stehlen", "stahl", "gestohlen"],
            12:["登る", "steigen", "stieg", "gestiegen"],
            13:["死ぬ", "sterben", "starb", "gestorben"],
            14:["突く", "stoßen", "stieß", "gestoßen"],
            15:["撫でる", "streichen", "strich", "gestrichen"],
            16:["争う", "streiten", "stritt", "gestritten"],
            17:["運ぶ", "tragen", "trug", "getragen"],
            18:["当たる", "treffen", "traf", "getroffen"],
            19:["駆り立てる", "treiben", "trieb", "getrieben"],
            20:["歩む", "treten", "trat", "getreten"],
            21:["飲む", "trinken", "trank", "getrunken"],
            22:["騙す", "tru^gen", "trog", "getrogen"],
            23:["する", "tun", "tat", "getan"],
            24:["台無しにする", "verderben", "verdarb", "verdorben"],
            25:["忘れる", "vergessen", "vergaß", "vergessen"],
            26:["失う", "verlieren", "verlor", "verloren"],
            27:["赦す", "verzeihen", "verzieh", "verziehen"],
            28:["成長する", "wachsen", "wuchs", "gewachsen"],
            29:["洗う", "waschen", "wusch", "gewaschen"],
            30:["よける", "weichen", "wich", "gewichen"],
            31:["指し示す", "weisen", "wies", "gewiesen"],
            32:["向ける", "wenden", "wandte", "gewandt"],
            33:["募集する", "werben", "warb", "geworben"],
            34:["なる", "werden", "wurde", "geworden"],
            35:["投げる", "werfen", "warf", "geworfen"],
            36:["重さを量る", "wiegen", "wog", "gewogen"],
            37:["知っている", "wissen", "wusste", "gewusst"],
            38:["巻く", "winden", "wand", "gewunden"],
            39:["〜するつもりだ", "wollen", "wollte", "gewollt"],
            40:["引く", "ziehen", "zog", "gezogen"],
            41:["強いる", "zwingen", "zwang", "gezwungen"]
            }
            }

week = int(input("week:"))
word_list = word_list_week[week]

seed(1)
rand_list = [i for i in range(len(word_list))]
#出題順をランダムにできする（デフォだとオフ）
'''
shuffle(rand_list)
'''
score = 0
for h, i in enumerate(rand_list):
    print(h + 1,":",word_list[i][0])
    for j in [1,2,3]:
        flag = False
        count = 3
        ques = q_sentence[j]
        while(not(flag) and count):
            try:
                answer = input("{}:".format(ques))
            except UnicodeDecodeError:
                print("retype")
                continue
            if answer == "pass":
                count = 0
                break
            elif answer == word_list[i][j]:
                flag = True
                break
            print("Wrong")
            count -= 1

        if flag:
            print("Right")
            score += 1
        else:
            print("right answer is: ",word_list[i][j])
print("Finish!")
print("score is {0}/{1}".format(score, len(word_list) * 3))
