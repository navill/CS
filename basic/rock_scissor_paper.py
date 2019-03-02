import random

win_list=[]

def get_player_choice():
	player=input("당신의 선택은 : ")
	while player != '바위' and player != '가위' and player.upper() != '보':
		player=input('다시 입력해주세요 : ')
	return player

def get_computer_choice():
	RSP_dic={1:'바위', 2:'가위', 3:'보'}
	computer=random.randint(1, 3)
	computer=RSP_dic[computer]
	return computer

def player_win_or_lose(player, computer):
	b_won=False
	if player == computer:
		b_won=None
	elif player == '바위' and computer == '가위' or \
player == '가위' and computer == '보' or \
player == '보' and computer == '바위':
		b_won=True
	else:
		b_won=False

	return b_won

def who_wins(player, computer):
	is_win=player_win_or_lose(player, computer)
	if is_win == True:
		return 'player'
	elif is_win == False:
		return 'computer'
	else:
		return 'draw'


def play_one():
	while True:
		player=get_player_choice()
		computer=get_computer_choice()
		winner=who_wins(player, computer)
		print(f'플레이어: {player}, 컴퓨터: {computer}')
		if winner=='player':
			print('플레이어 승!')
			return 'player'
		elif winner=='computer':
			print('컴퓨터 승!')
			return 'computer'
		else:
			print('무승부!')
			pass

def check_final_winner(win_list, how_many):
	print(f"플레이어 : {win_list.count('player')} 승, 컴퓨터 : {win_list.count('computer')} 승")
	num_win=how_many+1
	return 'player' if win_list.count('player')>=num_win\
		else 'computer' if win_list.count('computer')>=num_win\
		else None
	
def play():
	user_num_games=int(input("1:3판2선승, 2: 5판3선승: "))
	while user_num_games!=1 and user_num_games!=2:
		user_num_games=int(input("다시 입력해주세요 : "))
	
	num_games= 3 if user_num_games==1 else 5

	for i in range(num_games):
		win_list.append(play_one())
		checked=check_final_winner(win_list, user_num_games)
		if checked=='player':
			print('플레이어가 이겼습니다!')
			break
		elif checked=='computer':
			print('컴퓨터가 이겼습니다!')
			break
		else:
			pass

play()

