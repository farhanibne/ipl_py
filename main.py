from tkinter import *
import requests
from bs4 import BeautifulSoup

root =Tk()

url = "https://www.cricbuzz.com/"

title = Label(root, text='IPl', font=("Haveltica 30 bold"))
title.grid(row=1, padx=5)
root.title('IPL')

teams = Label(root, font=("Haveltica 20 bold"))
teams.grid(row=1, padx=5)

scores = Label(root, font=("Haveltica 20 bold"))
scores.grid(row=2, padx=5)

def get_score():
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    team_1 = soup.find_all(class_ ="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team_2 = soup.find_all(class_ ="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()

    team_1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
    team_2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

    teams.config(text=f"{team_1}\t\t{team_2}")
    scores.config(text=f"{team_1_score}\t{team_2_score}")

    scores.after(1000,get_score)





    get_score()
    root.mainloop()