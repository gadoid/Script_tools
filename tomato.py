import time 
import os 
import sys

print("欢迎来到番茄时间！")
print("每一个番茄时间将会为你赢得5块钱的奖励！")
try:
    with open ("value.txt","r") as file :
        content = file.read()
        print(f"当前剩余奖励{content}")
except FileNotFoundError or ValueError:
    pass
else:
    with open ("value.txt","w") as file :
        file.write("0")
    value = 0 

value = content
try :
    while True:
        tomato_second = 00
        tomato_minute = 25
        rest_minute = 5
        rest_second = 00
        while True :
            learn_content=input("本次番茄时间目标：")
            start_time_record= time.strftime('%H:%M:%S', time.localtime())
            while tomato_minute >= 0 :
                print(f"番茄时间现在还有 00:{tomato_minute}:{tomato_second} \n当前奖励为 {value}")
                time.sleep(1)
                os.system("cls")
                if tomato_second > 0 :
                    tomato_second-=1
                else :
                    tomato_second = 59
                    tomato_minute-=1
            end_time_record= time.strftime('%H:%M:%S', time.localtime())
            value=int(value)
            value+=5
            print(f"现在，你已获得奖励！当前剩余奖励数额度是 {value} !")
            with open ("value.txt","w") as fb :
                fb.write(str(value))
            with open(f"{time.strftime('%Y-%m-%d', time.localtime())}.txt","a") as file_object :
                file_object.write(f"内容：\t{learn_content}\t时间段:\t{start_time_record}-{end_time_record}\n")
            while rest_minute >= 0 :
                print(f"休息时间还有 00:{rest_minute}:{rest_second}")
                time.sleep(1)
                os.system("cls")
                if rest_second > 0 :
                    rest_second-=1
                else :
                    rest_second = 59
                    rest_minute-=1
            if tomato_minute < 0  and rest_minute < 0 : 
                break
except KeyboardInterrupt :
    print("\n程序关闭...")
finally :
    with open ("value.txt","w") as fb :
        fb.write(str(value))
    with open(f"{time.strftime('%Y-%m-%d', time.localtime())}.txt","r") as file_object :
        content = file_object.readlines()
        number = len(content)*25
        print(f"今天使用了 {number} 分钟进行学习")
        print(f"学习内容为：")
        for item in content :
            print(f"\t{item}",end="")
        print(f"日志文件\"{time.strftime('%Y-%m-%d', time.localtime())}.txt\"已保存在\"{os.getcwd()}\"目录下")
print("按任意键退出")
input()

