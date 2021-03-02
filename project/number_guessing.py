
# Number Guessing Game

import  random

def main():

    random_number = 12
    gues_check = True
    # Usr info
    print("1 ile 100 arasinda bir sayi tahmin ettim, bumani istiyorum \n")

    while gues_check:
        user_guesses = int(input("Guess a Number : "))
        if user_guesses == random_number:
            print("""
            (¯`·._.·(¯`·._.· TEBRIKLER ·._.·´¯)·._.·´¯)
                           Oyunu Kazandın
            """)
            print("Tekrar Oynamak Istermisin ?")
            replay = input("[Y / N] : ")

            if replay == "y" or "Y":
                break
            else:
                gues_check = False

        elif user_guesses > random_number:
            print("Yüksek Tahmin! - Daha küçük bir rakam denemelisin.")

        else:
            print("Düşük Tahmin! - Daha büyük bir rakam denemelisin.")

if __name__ == "__main__":
    main()