def replay():
    valid_ok = ["네", "예", "Y", "y", "yes", "YES", "Yes"]
    valid_no = ["아니요", "아니오", "N", "n", "no", "No", "NO"]
    while True:
        choice = input("한판 더 하실래용? Y or N : ")     
        if choice in valid_no:
            return False
        elif choice in valid_ok:
            return True
        else:
            print("잘못된 입력이에요! 다시 입력해주세요!")
