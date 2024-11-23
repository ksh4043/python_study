def determine_winner(player, computer):
    if player == computer:
        print("비겼습니다!")
        return "draw"
    elif (player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위'):
        print("이겼습니다!")
        return "win"
    else:
        print("패배하셨습니다ㅠㅠ")
        return "lose"
