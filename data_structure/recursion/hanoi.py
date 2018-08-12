def hanoi(num_tray, _from, _by, _to):
    if num_tray==1:
        print('{}번째 원반을 {}에서 {}로 이동'.format(num_tray, _from, _to))
        return

    hanoi(num_tray-1, _from, _to, _by)
    print('{}번째 원반을 {}에서 {}로 이동'.format(num_tray, _from, _to))
    hanoi(num_tray-1, _by, _from, _to)

if __name__=='__main__':
    while 1:
        num_tray=int(input("원반의 개수를 입력하세요(종료 : 0) :"))
        if num_tray==0:
            break
        hanoi(num_tray, 'A', 'B', 'C')

