import random

word_list = ["APPLE","GRAPE","LEMON","MANGO","MELON","PEACH","PRUNE"]
#print(len(word_list))

OPENING_MESSAGE = """
__________________________________
＊＊＊＊Welcome to WORDLE＊＊＊＊
5文字の英単語を当ててみよう！
🟩 = 場所とアルファベットが一致
🟨 = アルファベットは一致しているが場所が違う
⬛️ = 一致なし
__________________________________
"""
#答えを決めるインデックス
ind = random.randint(0,len(word_list)-1)
answer = word_list[ind]
#答えを一文字ずつリスト化
l_ans = list(answer)
l_res = []

def game():
    count = 1
    
    print(OPENING_MESSAGE)
    while True:
        l_ipt = list(str.upper(input(str(count)+"回目の挑戦！答えを入力してください --> ")))
        for i in range(5):
            if l_ans[i] == l_ipt[i]:
                l_res.append("🟩")
            elif l_ipt[i] in l_ans:
                l_res.append("🟨")
            else:
                l_res.append("⬛️")
        print("".join(l_res))
        if l_res.count("🟩") == 5:
            print("Congratulations!答えは"+answer+"でした！また挑戦してね！")
            break
        elif count == 6:
            print("ざんねん！答えは"+answer+"でした！また挑戦してね！")
        elif l_res.count("🟩") >= 3:
            print("惜しい！！")
        else:
            print("ざんねん！")
        l_res.clear()
        count = count+1

game()
