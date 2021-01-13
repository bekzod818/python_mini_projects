from uzwords import words
import random as r

def display(str1, str2):
    str3 = ''
    for i in str2:
        if i in str1:
            str3 += i.upper()
        else:
            str3 += '-'
    return str3
        
# print(display("dastlabki", "dastlabki").isalpha())
    
def get_word():
    word = r.choice(words)
    while '-' in word or ' ' in word or 'қ' in word or 'ғ' in word or 'ҳ' in word:
        word = r.choice(words)
    return word


def play():
    word = get_word()
    length = len(word)
    print(f"Мен {length} ҳарфли сўз ўйладим. Топа оласизми?")
    ans = "-" * length
    print(ans, "\n")
    enter = ""
    while True:
        letter = input("Ҳарф киритинг: ")
        
        if letter.lower() in enter:
            print(f"Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            print(display(enter, word))
            print(f"Шу вактгача киритган ҳарфларингиз: {enter.upper()}\n")
        
        elif letter.lower() not in enter:
            enter += letter
            if letter.lower() in word:
                print(f"{letter} ҳарфи тўғри!")
                if display(enter, word).isalpha():
                    print(f"Табриклайман {word.upper()} сўзини {len(enter)} уринишда топдингиз!")
                    break
                else:
                    print(display(enter, word))
                    print(f"Шу вактгача киритган ҳарфларингиз: {enter.upper()}\n")

            elif letter.lower() not in word:
                print("Бундай ҳарф йўқ!")
                print(display(enter, word))
                print(f"Шу вактгача киритган ҳарфларингиз: {enter.upper()}\n")
    return word    

play()
