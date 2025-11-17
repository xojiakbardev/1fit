from termcolor import colored
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class FitnessTools:
    def __init__(self, user):
        self.user = user


    def calculate_bmi(self):
        clear()
        height_m = self.user["height"] / 100
        bmi = self.user["weight"] / (height_m ** 2)
        print(colored(f"\n📊 Sizning BMI: {bmi:.2f}", "cyan"))
        if bmi < 18.5:
            print(colored("⚠️ Siz ozg‘insiz. Ko‘proq ovqatlaning!", "yellow"))
        elif 18.5 <= bmi < 25:
            print(colored("💪 Sizning vazningiz ideal!", "green"))
        elif 25 <= bmi < 30:
            print(colored("⚠️ Siz biroz ortiqcha vaznga egasiz.", "yellow"))
        else:
            print(colored("🚨 Siz semiz toifadansiz, diyetologga murojaat qiling!", "red"))
        
    
