import random
import game_logic as logic
import replay as rp
import os

path = "c:\\game_set"
file = "game_result.txt"
fullfile = os.path.join(path, file)

def get_player_input():
    valid_inputs = {"가위", "바위", "보"}
    while True:
        player = input("안 내면 진 거! 가위바위보! : ").strip()
        
        if player in valid_inputs:
            return player
        else:
            print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력하세요.")

if __name__ == "__main__":
    if not os.path.isdir(path):
        os.mkdir(path)
        
    win = 0
    defeat = 0
    draw = 0
    choices = {1: '가위', 2: '바위', 3: '보'}
    
    if os.path.exists(fullfile):
        with open(fullfile, "r") as f:
            last_game_data = f.readline().strip().split("|")
            win = int(last_game_data[0])
            defeat = int(last_game_data[1])
            draw = int(last_game_data[2])
        print(f"지난 게임 데이터!! 승리 : {win}, 패배 : {defeat}, 무승부 : {draw}")
    
    while True:
        # 사용자 입력 및 컴퓨터 난수로 가위바위보 결정
        player = get_player_input()
        computer = choices[random.randint(1,3)]
        print(f'플레이어 : {player}, 컴퓨터 : {computer}')

        # 승패 여부 결정
        result = logic.determine_winner(player, computer)
        if result == "draw":
            draw += 1
        elif result == "win":
            win += 1
        else:
            defeat += 1

        # 재시작 여부
        choice_re = rp.replay()
        if choice_re == False:
            break
        else:
            continue

    with open(fullfile, "w") as f:
        f.write(f"{win}|{defeat}|{draw}")
    
    print("=" * 20)
    print("프로그램 종료")
    print(f'승리 : {win}, 패배 : {defeat}, 무승부 : {draw}')
