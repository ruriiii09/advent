import collections
import random

cards = ["A","A","A","A",
        "2","2","2","2",
        "3","3","3","3",
        "4","4","4","4",
        "5","5","5","5",
        "6","6","6","6",
        "7","7","7","7",
        "8","8","8","8",
        "9","9","9","9",
        "10","10","10","10",
        "J","J","J","J",
        "Q","Q","Q","Q",
        "K","K","K","K","joker","joker"]
player1 = input("1人目の名前を入力してください。--->")
player2 = input("2人目の名前を入力してください。--->")

#テストハンド
#pl1 = ["10","A","4","4","Q"]
#pl2 = ["A","3","5","5","5"]

pl1 = random.sample(cards,5)
for i in pl1:
    cards.remove(i)
pl2 = random.sample(cards,5)

#各カードの枚数辞書
pl1num = collections.Counter(pl1)
pl2num = collections.Counter(pl2)
#ハンドの枚数だけ取得
handCount1 = pl1num.values()
handCount2 = pl2num.values()
#keyの取得
keys12 = [k for k,v in pl1num.items() if v == 2]
keys13 = [k for k,v in pl1num.items() if v == 3]

keys22 = [k for k,v in pl2num.items() if v == 2]
keys23 = [k for k,v in pl2num.items() if v == 3]


def result(hand,pl,plname,k2,k3):
    if 2 in pl and len(k2) == 1:
        print(plname,":",*hand,"--->",*k2,"ワンペア")
    elif 2 in pl and len(k2) == 2:
        print(plname,":",*hand,"--->", *k2,"ツーペア")
    elif 3 in pl:
        print(plname,":",*hand,"--->",*k3,"スリーカード")
    else:
        print(plname,*hand,"--->",*k3,":ノーペア")

result(pl1,handCount1,player1,keys12,keys13)
result(pl2,handCount2,player2,keys22,keys23)