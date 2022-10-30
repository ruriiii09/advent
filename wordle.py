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

def game():
    print(OPENING_MESSAGE)
    ind = random.randint(0,len(word_list)-1)
    answer = word_list[ind]
    
    l_ans = list(answer)
    l_res = []
    
    l_ipt = list(str.upper(input()))
    
    for i in range(5):
        if l_ans[i] == l_ipt[i]:
            l_res.append("🟩")
        elif l_ans[i] in l_ipt:
            l_res.append("🟨")
        else:
            l_res.append("⬛️")
    print("".join(l_res))
    if l_res.count("🟩") == 5:
        print("Congratulations!また挑戦してね！")
    elif l_res.count("🟩") >= 3:
        print("惜しい！！")
    else:
        print("ざんねん！")
    #print(l_ans,l_ipt)

game()
