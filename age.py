drive = input('請問您是否有開過車?')
if drive != '有' and drive != '沒有':
    print('只能輸入有或沒有')
    raise SystemExit

age = input('請問您今年幾歲：')
age = int(age)
if drive == '有':
    if age >= 18:
        print('通過駕照考試！')
    else:
        print('未成年請勿開車')
elif drive == '沒有':
    if age >= 18:
        print('請去考駕照')
    else:
        print('請勿開車上路')