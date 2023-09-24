from tkinter import *
import webbrowser

root = Tk()
root.title("Green Finder")
root.geometry("1200x800")

#1 원추리
def open_website1():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=570494&cid=46640&categoryId=46640")

def flash_buttons():
    for button in flashing_buttons:
        current_color = button.cget("background")
        next_color = "red" if current_color == "SystemButtonFace" else "SystemButtonFace"
        button.config(background=next_color)

def start_flashing():
    global flashing_buttons
    flashing_buttons = wonchuri  
    flash_buttons()
    root.after(500, flash_buttons) 

def open_new_window1():
    new_window1 = Toplevel()
    new_window1.title("식물 이름")

    photoPlant1_mul = PhotoImage(file="학교세특/입구/원추리_멀.png").subsample(3)
    plant_picMul1 = Label(new_window1, image=photoPlant1_mul)
    plant_picMul1.pack(side=LEFT)
    plant_picMul1.image = photoPlant1_mul

    photoPlant1_ga = PhotoImage(file="학교세특/입구/원추리_가.png").subsample(3)
    plant_picGa1 = Label(new_window1, image=photoPlant1_ga)
    plant_picGa1.pack(side=RIGHT)
    plant_picGa1.image = photoPlant1_ga

    btn_flash1 = Button(new_window1, text="교내 분포", command=start_flashing)
    btn_flash1.pack(side=BOTTOM)
    btn_web1 = Button(new_window1, text="Naver식물도감", command=open_website1)
    btn_web1.pack(side=BOTTOM)
    btn_ex1 = Label(new_window1, text="이름 : 원추리")
    btn_ex1.pack(side=BOTTOM)

photo_flowerIcon1 = PhotoImage(file="학교세특/입구/꽃아이콘_원추리.png").subsample(30)
btn_plant1 = Button(root, image=photo_flowerIcon1, command=open_new_window1)
btn_plant1.place(x=490, y=67)

wonchuri = [btn_plant1]

#2 루드베키아
def open_website2():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1088853&cid=40942&categoryId=32725")

def start_flashing2():
    global flashing_buttons
    flashing_buttons = rudbeckia  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window2():
    new_window2 = Toplevel()
    new_window2.title("식물 이름")

    photoPlant2_mul = PhotoImage(file="학교세특/입구/루드베키아_멀.png").subsample(3)
    plant_picMul2 = Label(new_window2, image=photoPlant2_mul)
    plant_picMul2.pack(side=LEFT)
    plant_picMul2.image = photoPlant2_mul

    photoPlant2_ga = PhotoImage(file="학교세특/입구/루드베키아_가.png").subsample(3)
    plant_picGa2 = Label(new_window2, image=photoPlant2_ga)
    plant_picGa2.pack(side=RIGHT)
    plant_picGa2.image = photoPlant2_ga

    btn_flash2 = Button(new_window2, text="교내 분포", command=start_flashing2)
    btn_flash2.pack(side=BOTTOM)
    btn_web2 = Button(new_window2, text="Naver식물도감", command=open_website2)
    btn_web2.pack(side=BOTTOM)
    btn_ex2 = Label(new_window2, text="이름 : 루드베키아")
    btn_ex2.pack(side=BOTTOM)

photo_flowerIcon2 = PhotoImage(file="학교세특/입구/꽃아이콘_루드베키아.png").subsample(30)
btn_plant2 = Button(root, image=photo_flowerIcon2, command=open_new_window2)
btn_plant2.place(x=580, y=170)

rudbeckia = [btn_plant2]

#3 홍단풍 
def open_website3():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=769909&cid=46694&categoryId=46694")

def start_flashing3():
    global flashing_buttons
    flashing_buttons = hongdanpung  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window3():
    new_window3 = Toplevel()
    new_window3.title("식물 이름")

    photoPlant3_mul = PhotoImage(file="학교세특/입구/홍단풍_멀.png").subsample(3)
    plant_picMul3 = Label(new_window3, image=photoPlant3_mul)
    plant_picMul3.pack(side=LEFT)
    plant_picMul3.image = photoPlant3_mul

    photoPlant3_ga = PhotoImage(file="학교세특/입구/홍단풍_가.png").subsample(3)
    plant_picGa3 = Label(new_window3, image=photoPlant3_ga)
    plant_picGa3.pack(side=RIGHT)
    plant_picGa3.image = photoPlant3_ga

    btn_flash3 = Button(new_window3, text="교내 분포", command=start_flashing3)
    btn_flash3.pack(side=BOTTOM)
    btn_web3 = Button(new_window3, text="Naver식물도감", command=open_website3)
    btn_web3.pack(side=BOTTOM)
    btn_ex3 = Label(new_window3, text="이름 : 홍단풍")
    btn_ex3.pack(side=BOTTOM)

photo_flowerIcon3 = PhotoImage(file="학교세특/입구/나무아이콘_홍단풍.png").subsample(33)
btn_plant3 = Button(root, image=photo_flowerIcon3, command=open_new_window3)
btn_plant3.place(x=580, y=220)

def open_new_window3_1():
    new_window3_1 = Toplevel()
    new_window3_1.title("식물 이름")

    photoPlant3_1_mul = PhotoImage(file="학교세특/운동장옆/홍단풍_1.png").subsample(3)
    plant_picMul3_1 = Label(new_window3_1, image=photoPlant3_1_mul)
    plant_picMul3_1.pack()
    plant_picMul3_1.image = photoPlant3_1_mul

    btn_flash3_1 = Button(new_window3_1, text="교내 분포", command=start_flashing3)
    btn_flash3_1.pack()

photo_flowerIcon3_1 = PhotoImage(file="학교세특/입구/나무아이콘_홍단풍.png").subsample(30)
btn_plant3_1 = Button(root, image=photo_flowerIcon3_1, command=open_new_window3_1)
btn_plant3_1.place(x=580, y=430)

hongdanpung = [btn_plant3, btn_plant3_1]

#4 푸른주름무당버섯, 찹살떡버섯
def open_website4():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=814402&cid=46689&categoryId=46689")
def open_website4_1():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=989824&cid=42526&categoryId=50851")

def start_flashing4():
    global flashing_buttons
    flashing_buttons = mushrooms  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window4():
    new_window4 = Toplevel()
    new_window4.title("식물 이름")

    photoPlant4_mul = PhotoImage(file="학교세특/정문차도/버섯_멀.png").subsample(3)
    plant_picMul4 = Label(new_window4, image=photoPlant4_mul)
    plant_picMul4.pack(side=LEFT)
    plant_picMul4.image = photoPlant4_mul

    photoPlant4_ga = PhotoImage(file="학교세특/정문차도/버섯_가.png").subsample(3)
    plant_picGa4 = Label(new_window4, image=photoPlant4_ga)
    plant_picGa4.pack(side=RIGHT)
    plant_picGa4.image = photoPlant4_ga

    btn_flash4 = Button(new_window4, text="교내 분포", command=start_flashing4)
    btn_flash4.pack(side=BOTTOM)
    btn_web4 = Button(new_window4, text="Naver식물도감(밑)", command=open_website4)
    btn_web4.pack(side=BOTTOM)
    btn_web4_1 = Button(new_window4, text="Naver식물도감(위)", command=open_website4_1)
    btn_web4_1.pack(side=BOTTOM)
    btn_ex4 = Label(new_window4, text="이름 : 푸른주름무당버섯(위)\n찹쌀떡버섯(밑)")
    btn_ex4.pack(side=BOTTOM)

photo_flowerIcon4 = PhotoImage(file="학교세특/버섯아이콘.png").subsample(36)
btn_plant4 = Button(root, image=photo_flowerIcon4, command=open_new_window4)
btn_plant4.place(x=450, y=440)

mushrooms = [btn_plant4]

#5 유카
def open_website5():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=2427988&cid=46695&categoryId=46695")

def start_flashing5():
    global flashing_buttons
    flashing_buttons = yucca  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window5():
    new_window5 = Toplevel()
    new_window5.title("식물 이름")

    photoPlant5_mul = PhotoImage(file="학교세특/정문차도/유카_멀.png").subsample(3)
    plant_picMul5 = Label(new_window5, image=photoPlant5_mul)
    plant_picMul5.pack(side=LEFT)
    plant_picMul5.image = photoPlant5_mul

    photoPlant5_ga = PhotoImage(file="학교세특/정문차도/유카_가.png").subsample(3)
    plant_picGa5 = Label(new_window5, image=photoPlant5_ga)
    plant_picGa5.pack(side=RIGHT)
    plant_picGa5.image = photoPlant5_ga

    btn_flash5 = Button(new_window5, text="교내 분포", command=start_flashing5)
    btn_flash5.pack(side=BOTTOM)
    btn_web5 = Button(new_window5, text="Naver식물도감", command=open_website5)
    btn_web5.pack(side=BOTTOM)
    btn_ex5 = Label(new_window5, text="이름 : 유카")
    btn_ex5.pack(side=BOTTOM)

photo_flowerIcon5 = PhotoImage(file="학교세특/정문차도/풀아이콘_유카.png").subsample(37)
btn_plant5 = Button(root, image=photo_flowerIcon5, command=open_new_window5)
btn_plant5.place(x=450, y=500)

def open_new_window5_1():
    new_window5_1 = Toplevel()
    new_window5_1.title("식물 이름")

    photoPlant5_1_mul = PhotoImage(file="학교세특/운동장옆/유카_1.png").subsample(3)
    plant_picMul5_1 = Label(new_window5_1, image=photoPlant5_1_mul)
    plant_picMul5_1.pack()
    plant_picMul5_1.image = photoPlant5_1_mul

    btn_flash5_1 = Button(new_window5_1, text="교내 분포", command=start_flashing5)
    btn_flash5_1.pack()

photo_flowerIcon5_1 = PhotoImage(file="학교세특/정문차도/풀아이콘_유카.png").subsample(37)
btn_plant5_1 = Button(root, image=photo_flowerIcon5_1, command=open_new_window5_1)
btn_plant5_1.place(x=580, y=550)

yucca = [btn_plant5, btn_plant5_1]

#6 은행나무
def open_website6():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=5782101&cid=62861&categoryId=62861")

def start_flashing6():
    global flashing_buttons
    flashing_buttons = eunhang  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window6():
    new_window6 = Toplevel()
    new_window6.title("식물 이름")

    photoPlant6_mul = PhotoImage(file="학교세특/정자/은행나무_멀.png").subsample(3)
    plant_picMul6 = Label(new_window6, image=photoPlant6_mul)
    plant_picMul6.pack(side=LEFT)
    plant_picMul6.image = photoPlant6_mul

    photoPlant6_ga = PhotoImage(file="학교세특/정자/은행나무_가.png").subsample(3)
    plant_picGa6 = Label(new_window6, image=photoPlant6_ga)
    plant_picGa6.pack(side=RIGHT)
    plant_picGa6.image = photoPlant6_ga

    btn_flash6 = Button(new_window6, text="교내 분포", command=start_flashing6)
    btn_flash6.pack(side=BOTTOM)
    btn_web6 = Button(new_window6, text="Naver식물도감", command=open_website6)
    btn_web6.pack(side=BOTTOM)
    btn_ex6 = Label(new_window6, text="이름 : 은행나무")
    btn_ex6.pack(side=BOTTOM)

photo_treeIcon6 = PhotoImage(file="학교세특/정자/나무아이콘_은행나무.png").subsample(33)
btn_plant6 = Button(root, image=photo_treeIcon6, command=open_new_window6)
btn_plant6.place(x=700, y=150)

eunhang = [btn_plant6]

#7 강아지 풀
def open_website7():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=5647115&cid=62861&categoryId=62861")

def start_flashing7():
    global flashing_buttons
    flashing_buttons = gangaji  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window7():
    new_window7 = Toplevel()
    new_window7.title("식물 이름")

    photoPlant7_mul = PhotoImage(file="학교세특/쓰레기장/강아지풀_멀.png").subsample(3)
    plant_picMul7 = Label(new_window7, image=photoPlant7_mul)
    plant_picMul7.pack(side=LEFT)
    plant_picMul7.image = photoPlant7_mul

    photoPlant7_ga = PhotoImage(file="학교세특/쓰레기장/강아지풀_가.png").subsample(3)
    plant_picGa7 = Label(new_window7, image=photoPlant7_ga)
    plant_picGa7.pack(side=RIGHT)
    plant_picGa7.image = photoPlant7_ga

    btn_flash7 = Button(new_window7, text="교내 분포", command=start_flashing7)
    btn_flash7.pack(side=BOTTOM)
    btn_web7 = Button(new_window7, text="Naver식물도감", command=open_website7)
    btn_web7.pack(side=BOTTOM)
    btn_ex7 = Label(new_window7, text="이름 : 강아지풀")
    btn_ex7.pack(side=BOTTOM)

photo_treeIcon7 = PhotoImage(file="학교세특/쓰레기장/풀아이콘_강아지풀.png").subsample(37)
btn_plant7 = Button(root, image=photo_treeIcon7, command=open_new_window7)
btn_plant7.place(x=1400, y=150)

def open_new_window7_1():
    new_window7_1 = Toplevel()
    new_window7_1.title("식물 이름")

    photoPlant7_1_mul = PhotoImage(file="학교세특/운동장옆/강아지풀_1.png").subsample(3)
    plant_picMul7_1 = Label(new_window7_1, image=photoPlant7_1_mul)
    plant_picMul7_1.pack()
    plant_picMul7_1.image = photoPlant7_1_mul

    btn_flash7_1 = Button(new_window7_1, text="교내 분포", command=start_flashing7)
    btn_flash7_1.pack()

photo_treeIcon7_1 = PhotoImage(file="학교세특/쓰레기장/풀아이콘_강아지풀.png").subsample(37)
btn_plant7_1 = Button(root, image=photo_treeIcon7_1, command=open_new_window7_1)
btn_plant7_1.place(x=580, y=587)

gangaji = [btn_plant7, btn_plant7_1]

#8 머위
def open_website8():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1092347&cid=40942&categoryId=32725")

def start_flashing8():
    global flashing_buttons
    flashing_buttons = meowi  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window8():
    new_window8 = Toplevel()
    new_window8.title("식물 이름")

    photoPlant8_mul = PhotoImage(file="학교세특/쓰레기장/머위_멀.png").subsample(3)
    plant_picMul8 = Label(new_window8, image=photoPlant8_mul)
    plant_picMul8.pack(side=LEFT)
    plant_picMul8.image = photoPlant8_mul

    photoPlant8_ga = PhotoImage(file="학교세특/쓰레기장/머위_가.png").subsample(3)
    plant_picGa8 = Label(new_window8, image=photoPlant8_ga)
    plant_picGa8.pack(side=RIGHT)
    plant_picGa8.image = photoPlant8_ga

    btn_flash8 = Button(new_window8, text="교내 분포", command=start_flashing8)
    btn_flash8.pack(side=BOTTOM)
    btn_web8 = Button(new_window8, text="Naver식물도감", command=open_website8)
    btn_web8.pack(side=BOTTOM)
    btn_ex8 = Label(new_window8, text="이름 : 머위")
    btn_ex8.pack(side=BOTTOM)

photo_treeIcon8 = PhotoImage(file="학교세특/쓰레기장/풀아이콘_머위.png").subsample(37)
btn_plant8 = Button(root, image=photo_treeIcon8, command=open_new_window8)
btn_plant8.place(x=1500, y=150)

def open_new_window8_1():
    new_window8_1 = Toplevel()
    new_window8_1.title("식물 이름")

    photoPlant8_1_mul = PhotoImage(file="학교세특/본관옆/머위_1.png").subsample(3)
    plant_picMul8_1 = Label(new_window8_1, image=photoPlant8_1_mul)
    plant_picMul8_1.pack()
    plant_picMul8_1.image = photoPlant8_1_mul

    btn_flash8_1 = Button(new_window8_1, text="교내 분포", command=start_flashing8)
    btn_flash8_1.pack()

photo_treeIcon8_1 = PhotoImage(file="학교세특/쓰레기장/풀아이콘_머위.png").subsample(37)
btn_plant8_1 = Button(root, image=photo_treeIcon8_1, command=open_new_window8_1)
btn_plant8_1.place(x=580, y=720)

meowi = [btn_plant8, btn_plant8_1]

#9 무궁화
def open_website9():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=3376588&cid=46694&categoryId=46694")

def start_flashing9():
    global flashing_buttons
    flashing_buttons = mugung  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window9():
    new_window9 = Toplevel()
    new_window9.title("식물 이름")

    photoPlant9_mul = PhotoImage(file="학교세특/별관골목/무궁화_멀.png").subsample(3)
    plant_picMul9 = Label(new_window9, image=photoPlant9_mul)
    plant_picMul9.pack(side=LEFT)
    plant_picMul9.image = photoPlant9_mul

    photoPlant9_ga = PhotoImage(file="학교세특/별관골목/무궁화_가.png").subsample(3)
    plant_picGa9 = Label(new_window9, image=photoPlant9_ga)
    plant_picGa9.pack(side=RIGHT)
    plant_picGa9.image = photoPlant9_ga

    btn_flash9 = Button(new_window9, text="교내 분포", command=start_flashing9)
    btn_flash9.pack(side=BOTTOM)
    btn_web9 = Button(new_window9, text="Naver식물도감", command=open_website9)
    btn_web9.pack(side=BOTTOM)
    btn_ex9 = Label(new_window9, text="이름 : 무궁화")
    btn_ex9.pack(side=BOTTOM)

photo_treeIcon9 = PhotoImage(file="학교세특/별관골목/꽃아이콘_무궁화.png").subsample(30)
btn_plant9 = Button(root, image=photo_treeIcon9, command=open_new_window9)
btn_plant9.place(x=1500, y=650)

def open_new_window9_1():
    new_window9_1 = Toplevel()
    new_window9_1.title("식물 이름")

    photoPlant9_1_mul = PhotoImage(file="학교세특/별관골목/무_1_멀.png").subsample(3)
    plant_picMul9_1 = Label(new_window9_1, image=photoPlant9_1_mul)
    plant_picMul9_1.pack(side=LEFT)
    plant_picMul9_1.image = photoPlant9_1_mul

    photoPlant9_1_ga = PhotoImage(file="학교세특/별관골목/무_1_가.png").subsample(3)
    plant_picGa9_1 = Label(new_window9_1, image=photoPlant9_1_ga)
    plant_picGa9_1.pack(side=RIGHT)
    plant_picGa9_1.image = photoPlant9_1_ga

    btn_flash9_1 = Button(new_window9_1, text="교내 분포", command=start_flashing9)
    btn_flash9_1.pack(side=BOTTOM)

photo_treeIcon9_1 = PhotoImage(file="학교세특/별관골목/꽃아이콘_무궁화.png").subsample(30)
btn_plant9_1 = Button(root, image=photo_treeIcon9, command=open_new_window9_1)
btn_plant9_1.place(x=1500, y=690)
mugung = [btn_plant9, btn_plant9_1]

#10 대나무
def open_website10():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=771421&cid=46695&categoryId=46695")

def start_flashing10():
    global flashing_buttons
    flashing_buttons = daenamu  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window10():
    new_window10 = Toplevel()
    new_window10.title("식물 이름")

    photoPlant10_mul = PhotoImage(file="학교세특/별관골목/대나무_멀.png").subsample(3)
    plant_picMul10 = Label(new_window10, image=photoPlant10_mul)
    plant_picMul10.pack(side=LEFT)
    plant_picMul10.image = photoPlant10_mul

    photoPlant10_ga = PhotoImage(file="학교세특/별관골목/대나무_가.png").subsample(3)
    plant_picGa10 = Label(new_window10, image=photoPlant10_ga)
    plant_picGa10.pack(side=RIGHT)
    plant_picGa10.image = photoPlant10_ga

    btn_flash10 = Button(new_window10, text="교내 분포", command=start_flashing10)
    btn_flash10.pack(side=BOTTOM)
    btn_web10 = Button(new_window10, text="Naver식물도감", command=open_website10)
    btn_web10.pack(side=BOTTOM)
    btn_ex10 = Label(new_window10, text="이름 : 대나무")
    btn_ex10.pack(side=BOTTOM)

photo_treeIcon10 = PhotoImage(file="학교세특/별관골목/나무아이콘_대나무.png").subsample(33)
btn_plant10 = Button(root, image=photo_treeIcon10, command=open_new_window10)
btn_plant10.place(x=1500, y=850)

daenamu = [btn_plant10]

#11 소철
def open_website11():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1114158&cid=40942&categoryId=32683")

def flash_buttons():
    for button in flashing_buttons:
        current_color = button.cget("background")
        next_color = "red" if current_color == "SystemButtonFace" else "SystemButtonFace"
        button.config(background=next_color)

def start_flashing11():
    global flashing_buttons
    flashing_buttons = sochul  # wonchuri 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window11():
    new_window11 = Toplevel()
    new_window11.title("식물 이름")

    photoPlant11_mul = PhotoImage(file="학교세특/본관앞/소철_멀.png").subsample(3)
    plant_picMul11 = Label(new_window11, image=photoPlant11_mul)
    plant_picMul11.pack(side=LEFT)
    plant_picMul11.image = photoPlant11_mul

    photoPlant11_ga = PhotoImage(file="학교세특/본관앞/소철_가.png").subsample(3)
    plant_picGa11 = Label(new_window11, image=photoPlant11_ga)
    plant_picGa11.pack(side=RIGHT)
    plant_picGa11.image = photoPlant11_ga

    btn_flash11 = Button(new_window11, text="교내 분포", command=start_flashing11)
    btn_flash11.pack(side=BOTTOM)
    btn_web11 = Button(new_window11, text="Naver식물도감", command=open_website11)
    btn_web11.pack(side=BOTTOM)
    btn_ex11 = Label(new_window11, text="이름 : 소철")
    btn_ex11.pack(side=BOTTOM)

photo_flowerIcon11 = PhotoImage(file="학교세특/본관앞/나무아이콘_소철.png").subsample(30)
btn_plant11 = Button(root, image=photo_flowerIcon11, command=open_new_window11)
btn_plant11.place(x=890, y=674)

sochul = [btn_plant11]

#12 목련
def open_website12():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1094006&cid=40942&categoryId=32698")

def flash_buttons():
    for button in flashing_buttons:
        current_color = button.cget("background")
        next_color = "red" if current_color == "SystemButtonFace" else "SystemButtonFace"
        button.config(background=next_color)

def start_flashing12():
    global flashing_buttons
    flashing_buttons = mokryun  # wonchuri 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window12():
    new_window12 = Toplevel()
    new_window12.title("식물 이름")

    photoPlant12_mul = PhotoImage(file="학교세특/본관앞/목련_멀.png").subsample(3)
    plant_picMul12 = Label(new_window12, image=photoPlant12_mul)
    plant_picMul12.pack(side=LEFT)
    plant_picMul12.image = photoPlant12_mul

    photoPlant12_ga = PhotoImage(file="학교세특/본관앞/목련_가.png").subsample(3)
    plant_picGa12 = Label(new_window12, image=photoPlant12_ga)
    plant_picGa12.pack(side=RIGHT)
    plant_picGa12.image = photoPlant12_ga

    btn_flash12 = Button(new_window12, text="교내 분포", command=start_flashing12)
    btn_flash12.pack(side=BOTTOM)
    btn_web12 = Button(new_window12, text="Naver식물도감", command=open_website12)
    btn_web12.pack(side=BOTTOM)
    btn_ex12 = Label(new_window12, text="이름 : 목련")
    btn_ex12.pack(side=BOTTOM)

photo_flowerIcon12 = PhotoImage(file="학교세특/본관앞/나무아이콘_목련.png").subsample(30)
btn_plant12 = Button(root, image=photo_flowerIcon11, command=open_new_window12)
btn_plant12.place(x=670, y=674)

mokryun = [btn_plant12]

#13 배롱나무
def open_website13():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=768292&cid=46694&categoryId=46694")

def start_flashing13():
    global flashing_buttons
    flashing_buttons = baelong  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window13():
    new_window13 = Toplevel()
    new_window13.title("식물 이름")

    photoPlant13_mul = PhotoImage(file="학교세특/운동장옆/배롱나무_멀.png").subsample(3)
    plant_picMul13 = Label(new_window13, image=photoPlant13_mul)
    plant_picMul13.pack(side=LEFT)
    plant_picMul13.image = photoPlant13_mul

    photoPlant13_ga = PhotoImage(file="학교세특/운동장옆/배롱나무_가.png").subsample(3)
    plant_picGa13 = Label(new_window13, image=photoPlant13_ga)
    plant_picGa13.pack(side=RIGHT)
    plant_picGa13.image = photoPlant13_ga

    btn_flash13 = Button(new_window13, text="교내 분포", command=start_flashing13)
    btn_flash13.pack(side=BOTTOM)
    btn_web13 = Button(new_window13, text="Naver식물도감", command=open_website13)
    btn_web13.pack(side=BOTTOM)
    btn_ex13 = Label(new_window13, text="이름 : 배롱나무")
    btn_ex13.pack(side=BOTTOM)

photo_flowerIcon13 = PhotoImage(file="학교세특/운동장옆/나무아이콘_배롱나무.png").subsample(33)
btn_plant13 = Button(root, image=photo_flowerIcon13, command=open_new_window13)
btn_plant13.place(x=580, y=500)

baelong = [btn_plant13]

#14 구절초
def open_website14():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1066437&cid=40942&categoryId=32725")

def start_flashing14():
    global flashing_buttons
    flashing_buttons = gujulcho  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window14():
    new_window14 = Toplevel()
    new_window14.title("식물 이름")

    photoPlant14_mul = PhotoImage(file="학교세특/구절초/5.png").subsample(3)
    plant_picMul14 = Label(new_window14, image=photoPlant14_mul)
    plant_picMul14.pack(side=LEFT)
    plant_picMul14.image = photoPlant14_mul

    photoPlant14_ga = PhotoImage(file="학교세특/구절초/1.png").subsample(3)
    plant_picGa14 = Label(new_window14, image=photoPlant14_ga)
    plant_picGa14.pack(side=RIGHT)
    plant_picGa14.image = photoPlant14_ga

    btn_flash14 = Button(new_window14, text="교내 분포", command=start_flashing14)
    btn_flash14.pack(side=BOTTOM)
    btn_web14 = Button(new_window14, text="Naver식물도감", command=open_website14)
    btn_web14.pack(side=BOTTOM)
    btn_ex14 = Label(new_window14, text="이름 : 구절초")
    btn_ex14.pack(side=BOTTOM)

photo_flowerIcon14 = PhotoImage(file="학교세특/구절초/꽃아이콘_구절초.png").subsample(30)
btn_plant14 = Button(root, image=photo_flowerIcon14, command=open_new_window14)
btn_plant14.place(x=1266, y=440)

def open_new_window14_1():
    new_window14_1 = Toplevel()
    new_window14_1.title("식물 이름")

    photoPlant14_1 = PhotoImage(file="학교세특/구절초/2.png").subsample(3)
    plant_picMul14_1 = Label(new_window14_1, image=photoPlant14_1)
    plant_picMul14_1.pack()
    plant_picMul14_1.image = photoPlant14_1

    btn_flash14_1 = Button(new_window14_1, text="교내 분포", command=start_flashing14)
    btn_flash14_1.pack()

photo_flowerIcon14_1 = PhotoImage(file="학교세특/구절초/꽃아이콘_구절초_1.png").subsample(30)
btn_plant14_1 = Button(root, image=photo_flowerIcon14_1, command=open_new_window14_1)
btn_plant14_1.place(x=450, y=640)

def open_new_window14_2():
    new_window14_2 = Toplevel()
    new_window14_2.title("식물 이름")

    photoPlant14_2 = PhotoImage(file="학교세특/구절초/3.png").subsample(3)
    plant_picMul14_2 = Label(new_window14_2, image=photoPlant14_2)
    plant_picMul14_2.pack()
    plant_picMul14_2.image = photoPlant14_2

    btn_flash14_2 = Button(new_window14_2, text="교내 분포", command=start_flashing14)
    btn_flash14_2.pack()

photo_flowerIcon14_2 = PhotoImage(file="학교세특/구절초/꽃아이콘_구절초_2.png").subsample(30)
btn_plant14_2 = Button(root, image=photo_flowerIcon14_2, command=open_new_window14_2)
btn_plant14_2.place(x=1500, y=500)

def open_new_window14_3():
    new_window14_3 = Toplevel()
    new_window14_3.title("식물 이름")

    photoPlant14_3 = PhotoImage(file="학교세특/구절초/4.png").subsample(3)
    plant_picMul14_3 = Label(new_window14_3, image=photoPlant14_3)
    plant_picMul14_3.pack()
    plant_picMul14_3.image = photoPlant14_3

    btn_flash14_3 = Button(new_window14_3, text="교내 분포", command=start_flashing14)
    btn_flash14_3.pack()

photo_flowerIcon14_3 = PhotoImage(file="학교세특/구절초/꽃아이콘_구절초_3.png").subsample(30)
btn_plant14_3 = Button(root, image=photo_flowerIcon14_3, command=open_new_window14_3)
btn_plant14_3.place(x=1500, y=230)

gujulcho = [btn_plant14, btn_plant14_1, btn_plant14_2, btn_plant14_3]

#15 측백나무 
def open_website15():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=3376649&cid=46690&categoryId=46690")

def start_flashing15():
    global flashing_buttons
    flashing_buttons = chekbaek  # rudbeckia 리스트에 버튼 추가
    flash_buttons()
    root.after(500, flash_buttons)  # 500ms마다 버튼 깜빡임 업데이트

def open_new_window15():
    new_window15 = Toplevel()
    new_window15.title("식물 이름")

    photoPlant15_mul = PhotoImage(file="학교세특/본관앞/측백나무_멀.png").subsample(3)
    plant_picMul15 = Label(new_window15, image=photoPlant15_mul)
    plant_picMul15.pack(side=LEFT)
    plant_picMul15.image = photoPlant15_mul

    photoPlant15_ga = PhotoImage(file="학교세특/본관앞/측백나무_가.png").subsample(3)
    plant_picGa15 = Label(new_window15, image=photoPlant15_ga)
    plant_picGa15.pack(side=RIGHT)
    plant_picGa15.image = photoPlant15_ga

    btn_flash15 = Button(new_window15, text="교내 분포", command=start_flashing15)
    btn_flash15.pack(side=BOTTOM)
    btn_web15 = Button(new_window15, text="Naver식물도감", command=open_website15)
    btn_web15.pack(side=BOTTOM)
    btn_ex15 = Label(new_window15, text="이름 : 측백나무")
    btn_ex15.pack(side=BOTTOM)

photo_flowerIcon15 = PhotoImage(file="학교세특/본관앞/나무아이콘_측백나무.png").subsample(33)
btn_plant15 = Button(root, image=photo_flowerIcon15, command=open_new_window15)
btn_plant15.place(x=630, y=674)

chekbaek = [btn_plant15]

#어디서나 볼 수 있는 식물
label_everywhere = Label(root, text="어디서나 볼 수 있는 식물")
label_everywhere.place(x=250, y=80)
#뾰소
def open_websitebbo():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=5781963&cid=62861&categoryId=62861")

def open_new_windowbbo():
    new_windowbbo = Toplevel()
    new_windowbbo.title("식물 이름")

    photoPlantbbo_mul = PhotoImage(file="학교세특/어디서나/뾰소_멀.png").subsample(3)
    plant_picMulbbo = Label(new_windowbbo, image=photoPlantbbo_mul)
    plant_picMulbbo.pack(side=LEFT)
    plant_picMulbbo.image = photoPlantbbo_mul

    photoPlantbbo_ga = PhotoImage(file="학교세특/어디서나/뾰소_가.png").subsample(3)
    plant_picGabbo = Label(new_windowbbo, image=photoPlantbbo_ga)
    plant_picGabbo.pack(side=RIGHT)
    plant_picGabbo.image = photoPlantbbo_ga

    btn_webbbo = Button(new_windowbbo, text="Naver식물도감", command=open_websitebbo)
    btn_webbbo.pack(side=BOTTOM)
    btn_exbbo = Label(new_windowbbo, text="이름 : 소나무")
    btn_exbbo.pack(side=BOTTOM)

photo_flowerIconbbo = PhotoImage(file="학교세특/어디서나/뾰소_멀.png").subsample(10)
btn_plantbbo = Button(root, image=photo_flowerIconbbo, command=open_new_windowbbo)
btn_plantbbo.place(x=250, y=100)
#향나무
def open_websitenul():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=3376657&cid=46690&categoryId=46690")

def open_new_windownul():
    new_windownul = Toplevel()
    new_windownul.title("식물 이름")

    photoPlantnul_mul = PhotoImage(file="학교세특/어디서나/넓소_멀.png").subsample(3)
    plant_picMulnul = Label(new_windownul, image=photoPlantnul_mul)
    plant_picMulnul.pack(side=LEFT)
    plant_picMulnul.image = photoPlantnul_mul

    photoPlantnul_ga = PhotoImage(file="학교세특/어디서나/넓소_가.png").subsample(3)
    plant_picGanul = Label(new_windownul, image=photoPlantnul_ga)
    plant_picGanul.pack(side=RIGHT)
    plant_picGanul.image = photoPlantnul_ga

    btn_webnul = Button(new_windownul, text="Naver식물도감", command=open_websitenul)
    btn_webnul.pack(side=BOTTOM)
    btn_exnul = Label(new_windownul, text="이름 : 향나무")
    btn_exnul.pack(side=BOTTOM)

photo_flowerIconnul = PhotoImage(file="학교세특/어디서나/넓소_멀.png").subsample(10)
btn_plantnul = Button(root, image=photo_flowerIconnul, command=open_new_windownul)
btn_plantnul.place(x=250, y=240)
#둥풀
def open_websitedung():
    webbrowser.open("https://terms.naver.com/entry.naver?docId=1922890&cid=46690&categoryId=46690")

def open_new_windowdung():
    new_windowdung = Toplevel()
    new_windowdung.title("식물 이름")

    photoPlantdung_mul = PhotoImage(file="학교세특/어디서나/둥풀_멀.png").subsample(3)
    plant_picMuldung = Label(new_windowdung, image=photoPlantdung_mul)
    plant_picMuldung.pack(side=LEFT)
    plant_picMuldung.image = photoPlantdung_mul

    photoPlantdung_ga = PhotoImage(file="학교세특/어디서나/둥풀_가.png").subsample(3)
    plant_picGadung = Label(new_windowdung, image=photoPlantdung_ga)
    plant_picGadung.pack(side=RIGHT)
    plant_picGadung.image = photoPlantdung_ga

    btn_webdung = Button(new_windowdung, text="Naver식물도감", command=open_websitedung)
    btn_webdung.pack(side=BOTTOM)
    btn_exdung = Label(new_windowdung, text="이름 : 회양목")
    btn_exdung.pack(side=BOTTOM)

photo_flowerIcondung = PhotoImage(file="학교세특/어디서나/둥풀_멀.png").subsample(10)
btn_plantdung = Button(root, image=photo_flowerIcondung, command=open_new_windowdung)
btn_plantdung.place(x=250, y=415)

#시점1
def open_new_windowpov1():
    new_windowpov1 = Toplevel()
    new_windowpov1.title("식물 이름")

    photoPov1 = PhotoImage(file="학교세특/시점/1.png").subsample(3)
    plant_picpov1 = Label(new_windowpov1, image=photoPov1)
    plant_picpov1.pack(side=LEFT)
    plant_picpov1.image = photoPov1

photo_pov1 = PhotoImage(file="학교세특/시점/눈아이콘_1.png").subsample(40)
btn_pov1 = Button(root, image=photo_pov1, command=open_new_windowpov1)
btn_pov1.place(x=563, y=105)
#시점2
def open_new_windowpov2():
    new_windowpov2 = Toplevel()
    new_windowpov2.title("식물 이름")

    photoPov2 = PhotoImage(file="학교세특/시점/2.png").subsample(3)
    plant_picpov2 = Label(new_windowpov2, image=photoPov2)
    plant_picpov2.pack(side=LEFT)
    plant_picpov2.image = photoPov2

photo_pov2 = PhotoImage(file="학교세특/시점/눈아이콘_2.png").subsample(40)
btn_pov2 = Button(root, image=photo_pov2, command=open_new_windowpov2)
btn_pov2.place(x=563, y=139)
#시점3
def open_new_windowpov3():
    new_windowpov3 = Toplevel()
    new_windowpov3.title("식물 이름")

    photoPov3 = PhotoImage(file="학교세특/시점/3.png")
    plant_picpov3 = Label(new_windowpov3, image=photoPov3)
    plant_picpov3.pack(side=LEFT)
    plant_picpov3.image = photoPov3

photo_pov3 = PhotoImage(file="학교세특/시점/눈아이콘_3.png").subsample(40)
btn_pov3 = Button(root, image=photo_pov3, command=open_new_windowpov3)
btn_pov3.place(x=800, y=145)
#시점4
def open_new_windowpov4():
    new_windowpov4 = Toplevel()
    new_windowpov4.title("식물 이름")

    photoPov4 = PhotoImage(file="학교세특/시점/4.png")
    plant_picpov4 = Label(new_windowpov4, image=photoPov4)
    plant_picpov4.pack(side=LEFT)
    plant_picpov4.image = photoPov4

photo_pov4 = PhotoImage(file="학교세특/시점/눈아이콘_4.png").subsample(40)
btn_pov4 = Button(root, image=photo_pov3, command=open_new_windowpov4)
btn_pov4.place(x=1300, y=145)
#시점5
def open_new_windowpov5():
    new_windowpov5 = Toplevel()
    new_windowpov5.title("식물 이름")

    photoPov5 = PhotoImage(file="학교세특/시점/5.png").subsample(3)
    plant_picpov5 = Label(new_windowpov5, image=photoPov5)
    plant_picpov5.pack(side=LEFT)
    plant_picpov5.image = photoPov5

photo_pov5 = PhotoImage(file="학교세특/시점/눈아이콘_5.png").subsample(40)
btn_pov5 = Button(root, image=photo_pov5, command=open_new_windowpov5)
btn_pov5.place(x=1500, y=810)
#시점6
def open_new_windowpov6():
    new_windowpov6 = Toplevel()
    new_windowpov6.title("식물 이름")

    photoPov6 = PhotoImage(file="학교세특/시점/6.png").subsample(3)
    plant_picpov6 = Label(new_windowpov6, image=photoPov6)
    plant_picpov6.pack(side=LEFT)
    plant_picpov6.image = photoPov6

photo_pov6 = PhotoImage(file="학교세특/시점/눈아이콘_6.png").subsample(40)
btn_pov6 = Button(root, image=photo_pov6, command=open_new_windowpov6)
btn_pov6.place(x=1390, y=880)
#시점7
def open_new_windowpov7():
    new_windowpov7 = Toplevel()
    new_windowpov7.title("식물 이름")

    photoPov7 = PhotoImage(file="학교세특/시점/7.png").subsample(3)
    plant_picpov7 = Label(new_windowpov7, image=photoPov7)
    plant_picpov7.pack(side=LEFT)
    plant_picpov7.image = photoPov7

photo_pov7 = PhotoImage(file="학교세특/시점/눈아이콘_7.png").subsample(40)
btn_pov7 = Button(root, image=photo_pov7, command=open_new_windowpov7)
btn_pov7.place(x=563, y=880)
#시점8
def open_new_windowpov8():
    new_windowpov8 = Toplevel()
    new_windowpov8.title("식물 이름")

    photoPov8 = PhotoImage(file="학교세특/시점/8.png").subsample(3)
    plant_picpov8 = Label(new_windowpov8, image=photoPov8)
    plant_picpov8.pack(side=LEFT)
    plant_picpov8.image = photoPov8

photo_pov8 = PhotoImage(file="학교세특/시점/눈아이콘_8.png").subsample(40)
btn_pov8 = Button(root, image=photo_pov8, command=open_new_windowpov8)
btn_pov8.place(x=580, y=688)


# 중일고 구조 도식화
photo_bon = PhotoImage(file="학교세특/학교구조/본관.png").subsample(2)
label_bon = Label(root, image=photo_bon)
label_bon.place(x=620, y= 710)

photo_beul = PhotoImage(file="학교세특/학교구조/별관.png").subsample(2)
label_beul = Label(root, image=photo_beul)
label_beul.place(x=1300, y= 220)

photo_un = PhotoImage(file="학교세특/학교구조/운동장.png").subsample(2)
label_un = Label(root, image=photo_un)
label_un.place(x=620, y= 310)

photo_chae = PhotoImage(file="학교세특/학교구조/체육관.png").subsample(4)
label_chae = Label(root, image=photo_chae)
label_chae.place(x=950, y= 75)

photo_maindoor_road = PhotoImage(file="학교세특/학교구조/정문도로.png")
label_maindoor_road = Label(root, image=photo_maindoor_road)

label_maindoor = Label(root, text="정\n문")
label_maindoor.place(x=470, y=100)

label_maindoor = Label(root, text="후\n문")
label_maindoor.place(x=1550, y=730)

label_maindoor_road.place(x=500, y=100)

root.mainloop()