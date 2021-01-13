from random import randint
def son_top(n):
    number = randint(1, n)
    count1 = 1
    print("Keling o'ylagan sonni topishni o'ynaymiz!")
    print(f"1 dan {n} gacha son o'yladim topa olasizmi?")
    while True:
        answer = int(input("Son = "))
        if answer > number:
            print(f"Men o'ylagan son {answer} dan kichikroq. Yana urinib ko'ring!")
        elif answer < number:
            print(f"Men o'ylagan son {answer} dan kattaroq. Yana urinib ko'ring!")
        else:
            print(f"{answer} sonini o'ylagan edim. {count1} ta urinishda topdingiz. Tabriklayman!")
            break
        count1 += 1
    return count1

def son_top_pc(n):
    print(f"\n1 dan {n} gacha son o'ylang. Men topishga harakat qilaman!")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing. Boshlaymiz!")
    L, R = 1, n
    count2 = 1
    son = randint(L, R)
    while L != R:
        javob = input(f"{son} sonini o'yladingiz. To'g'ri bo'lsa (T). Kattaroq bo'lsa (+). Kichikroq bo'lsa (-)? ")
        if javob.lower() == 't':
            print(f"Siz {son} sonini o'ylabsiz. {count2} urinishda topdim.")
            break
        else:
            if javob == '+':
                L = son + 1
            if javob == '-':
                R = son - 1
            son = randint(L, R)
        count2 += 1
    if L == R:
        print(f"Siz {L} sonini o'ylabsiz. {count2} urinishda topdim.")
    return count2
    
def natija(a, b):
    if a > b:
        print("Men sizni yutdim.")
    elif a < b:
        print("Afsus men sizga yutqazdim.")
    else:
        print('Durrang!')

while True:
    a = input(f"\nO'yin o'ynaymizmi? (yes/no) ")
    print()
    if a == 'no':
        print("O'yin tugadi.")
        break
    else:
        b = int(input(f"1 dan qaysi songacha topish o'ynaymiz: "))
        print()
        x = son_top(b)
        print()
        print('*' * 70)
        y = son_top_pc(b)
        print()
        print('----------------Natija-----------------')
        natija(x, y)
        print('-' * 40)