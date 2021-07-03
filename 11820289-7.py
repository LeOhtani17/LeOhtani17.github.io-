def compute_bmi():
    print(str(a)+"さん、あなたのBMIは"+str(BMI)+"でした。")
    if BMI<18.5:
        return 1
    elif 18.5<=BMI<25.0:
        return 2
    elif 25.0<=BMI<30.0:
        return 3
    elif 30.0<=BMI:
        return 4
def fatness_judge():
    BMI=compute_bmi()
    if BMI==1:
        print("[分類]:痩せすぎだよーー。もっと食べなきゃなぁ。")
    if BMI==2:
        print("[分類]:標準だね、この調子～")
    if BMI==3:
        print("[分類]:ちょっと際どいぞ…有酸素運動を取り入れよう♪")
    if BMI==4:
        print("[分類]:ヤバいぞ！！！今すぐジムに通うんだ!!")
if __name__=="__main__":
    a=input("氏名を入力 = ")
    b=float(input("身長[cm]を入力 = "))
    c=float(input("体重[kg]を入力 = "))
    BMI=c/((b*0.01)**2)
    fatness_judge()
