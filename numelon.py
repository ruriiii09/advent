import random

word_list = ["APPLE","GRAPE","LEMON","MANGO","MELON","PEACH","PRUNE"]
#print(len(word_list))

OPENING_MESSAGE = """
__________________________________
＊＊＊＊Welcome to WORDLE＊＊＊＊
5文字の数字を当ててみよう！
🟩 = 場所とアルファベットが一致
🟨 = アルファベットは一致しているが場所が違う
⬛️ = 一致なし
__________________________________
"""

l_res = []

#答えを決める
numbers = ["1","2","3","4","5","6","7","8","9","0"]
num_list = random.sample(numbers,5)

def numgame():
    count = 1
    
    print(OPENING_MESSAGE)
    #print("".join(num_list))
    while True:
        l_ipt = list(str.upper(input(str(count)+"回目の挑戦！答えを入力してください --> ")))
        for i in range(5):
            if num_list[i] == l_ipt[i]:
                l_res.append("🟩")
            elif l_ipt[i] in num_list:
                l_res.append("🟨")
            else:
                l_res.append("⬛️")
        print("".join(l_res))
        if l_res.count("🟩") == 5:
            print("Congratulations!答えは"+"".join(num_list)+"でした！また挑戦してね！")
            break
        elif count == 6:
            print(str(l_res.count("🟩"))+"Hit "+str(l_res.count("🟨"))+"Blow！ざんねん！答えは"+"".join(num_list)+"でした！また挑戦してね！")
            break
        elif l_res.count("🟩") >= 3:
            print(str(l_res.count("🟩"))+"Hit "+str(l_res.count("🟨"))+"Blow！惜しい！！")
        else:
            print(str(l_res.count("🟩"))+"Hit "+str(l_res.count("🟨"))+"Blow！ざんねん！")
        l_res.clear()
        count = count+1

numgame()
