import random
import os
import time

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title():
    print(BLUE + "=" * 30)
    print("  🎮 TAŞ KAĞIT MAKAS OYUNU 🎮")
    print("=" * 30 + RESET)


def get_user_choice():
    print(YELLOW + "\nSeçim yapın: Taş, Kağıt, Makas (çıkmak için q): " + RESET)
    try:
        choice = input().lower()
        if choice == 'q':
            return None
        while choice not in ['taş', 'kağıt', 'makas']:
            print(RED + "Geçersiz seçim! Lütfen tekrar deneyin. (Taş, Kağıt, Makas)" + RESET)
            choice = input("Taş, Kağıt, Makas? (çıkmak için q): ").lower()
            if choice == 'q':
                return None
        return choice
    except (EOFError, KeyboardInterrupt):
        print("\nOyun sonlandırıldı.")
        return None


def get_computer_choice():
    return random.choice(['taş', 'kağıt', 'makas'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere"
    elif (user_choice == 'taş' and computer_choice == 'makas') or \
            (user_choice == 'kağıt' and computer_choice == 'taş') or \
            (user_choice == 'makas' and computer_choice == 'kağıt'):
        return "Kullanıcı"
    else:
        return "Bilgisayar"


def print_choice_art(choice):
    art = {
        'taş': '''
   _______
  |       |
  |   O   |
  |_______|''',
        'kağıt': '''
   _______
  |       |
  |  ___  |
  | |___| |
  |_______|''',
        'makas': '''
   _______
  | /   \ |
  | |   | |
  | |___| |
  |_______|'''
    }
    print(art.get(choice, ""))


def tas_kagit_makas_ADINIZ_SOYADINIZ():
    display_title()
    choices = ['taş', 'kağıt', 'makas']

    while True:
        user_wins = 0
        computer_wins = 0

        while user_wins < 2 and computer_wins < 2:
            print(GREEN + "\nYeni Tur" + RESET)
            user_choice = get_user_choice()
            if user_choice is None:
                print(YELLOW + "Oyundan çıkılıyor..." + RESET)
                return

            computer_choice = get_computer_choice()
            print(f"\nBilgisayarın seçimi: {computer_choice.capitalize()}")
            print_choice_art(computer_choice)

            if user_choice == computer_choice:
                print(YELLOW + "Berabere!" + RESET)
            elif determine_winner(user_choice, computer_choice) == "Kullanıcı":
                user_wins += 1
                print(GREEN + "Bu turu kazandınız!" + RESET)
                print_choice_art(user_choice)
            else:
                computer_wins += 1
                print(RED + "Bu turu bilgisayar kazandı!" + RESET)

            print(f"{GREEN}Skor: Siz - {user_wins}, Bilgisayar - {computer_wins}{RESET}")
            time.sleep(1)
            clear_screen()
            display_title()

        if user_wins == 2:
            print(GREEN + "Tebrikler! Oyunu kazandınız!" + RESET)
        else:
            print(RED + "Bilgisayar oyunu kazandı!" + RESET)

        play_again = input(YELLOW + "Tekrar oynamak ister misiniz? (E/H): " + RESET).lower()
        if play_again == 'h':
            print("Teşekkürler, oyun bitti!" + RESET)
            break
        elif play_again != 'e':
            print(RED + "Geçersiz yanıt! Lütfen 'E' veya 'H' girin." + RESET)
            continue


        computer_wants_to_play = random.choice(['e', 'h'])
        if computer_wants_to_play == 'h':
            print(RED + "Bilgisayar oyundan çekildi. Oyun bitti!" + RESET)
            break

        clear_screen()

tas_kagit_makas_ADINIZ_SOYADINIZ()
