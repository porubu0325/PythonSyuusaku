for i in range(1, 101): # 1から100まで繰り返す
    if i % 3 == 0 and i % 5 == 0: # 3と5の両方で割り切れる場合
        print("教育死刑") # 「教育死刑」と出力
    elif i % 3 == 0: # 3で割り切れる場合
        print("教育") # 「教育」と出力
    elif i % 5 == 0: # 5で割り切れる場合
        print("死刑") # 「死刑」と出力
    else: # それ以外の場合
        print(i) # 数字を出力