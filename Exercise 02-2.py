from random import randrange
print("------------CHÀO MỪNG BẠN ĐẾN VỚI MINI GAME ĐOÁN SỐ TỪ 1-999-------------")
while True:
    number1 = randrange (1,999)
    so_lan_doan = 0
    win  = False
    while  so_lan_doan < 10:
        so_lan_doan += 1

        so_ban_doan = int(input("Mời bạn đoán số: \n "))

        if so_lan_doan == 5:
            if number1 == so_ban_doan:
                print("Chúc mừng bạn đã đoán trúng, số máy là: ", number1)
                win = True
                break
            else:
                print("Bạn đã trả lời sai lần ",so_lan_doan )
                print("kết quả đã thay đổi.Số đúng là ",number1)
                print(input("Bạn có thêm 5 lượt đoán, mời bạn đoán lại \n"))
                number1 = randrange (1,101)
        elif so_ban_doan in range(number1 -10, number1 +10):
            print("Bạn đoán gần đúng roi")
            continue

        if number1 == so_ban_doan:
            print("Bạn đã oán trúng, số đúng là: ", number1) 
            win = True
            break
        if number1 > so_ban_doan:
            print ("Bạn đoán sai lần", +so_lan_doan)
        elif number1 < so_ban_doan:
            print ("Bạn đoán sai lần", +so_lan_doan)

    if win == False:
        print ("GAME OVER ! số máy = ", number1)
    hoi = input("Bạn có muốn tiếp tục không y/n ! ")
    if hoi == 'n':
        break
print ("Cảm ơn bạn đã chơi game !")


# fgffff
# huy np tesst 123123123