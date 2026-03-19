# NBA stats
import pandas as pd
import difflib
import sys
import streamlit as st
import requests
from io import StringIO

urlstats = "https://media.githubusercontent.com/media/moneymanan/NBA-stats/refs/heads/main/Moneymanan/My%20Stuff/Python/NBA%20Stats/PlayerStatistics.csv"
urlgames = "https://media.githubusercontent.com/media/moneymanan/NBA-stats/refs/heads/main/Moneymanan/My%20Stuff/Python/NBA%20Stats/Games.csv"

s = pd.read_csv(urlstats, low_memory=False)
g = pd.read_csv(urlgames, low_memory=False)

st.title(":sunglasses: NBA Stats :sunglasses:", text_alignment = "center")
st.header("Trying to fulfill my NBA dreams", text_alignment = "center")

st.write(s.columns)

# Normalize columns
s.columns = s.columns.str.strip().str.lower()

# Safety check
if "firstname" not in s.columns or "lastname" not in s.columns:
    st.error("Expected columns not found!")
    st.stop()

valid_stats = list(s.columns)
s["player"] = s["firstname"] + " " + s["lastname"]
players = s["player"].unique()
name = st.text_input("Name: ")
while ' ' not in name:
    name = st.text_input('Enter first and last name: ')
while name not in players:
    suggestion = difflib.get_close_matches(name, players, n=1, cutoff=0.6)
    if suggestion:
        opt = st.write(f"Do you mean '{suggestion[0]}'?")
        if st.button("Yes"): #opt.lower() =='y':
            name = suggestion[0]
        elif st.button("No"):
            name = st.text_input("Name: ")
    else:
        sys.exit(':( NAME ERROR :(')

stat = st.text_input("What stat do you want? (points, rebounds, assists, blocks, steals): ").lower()
while stat.lower() not in [col.lower() for col in valid_stats]:
    suggestion = difflib.get_close_matches(stat, valid_stats, n=1)
    if suggestion:
        opt = st.write(f"Do you mean '{suggestion[0]}'?")
        if st.button("Yes"): #opt.lower() == 'y':
            stat = suggestion[0]
        elif st.button("No"):
            stat = st.text_input("Enter stat: ")
    else:
        sys.exit('LAPTOP DESTRUCTION EMINENT\n'*5) 

info = s.loc[
    s["player"] == name,
    stat
].iloc[0]


if name.lower() == 'lebron james':
    name = 'THE GOAT'
    st.write(name + ' had ' + str(int(info)) + ' ' + stat + ' :sunglasses:')
else:
    st.write(s.loc[s['player'] == name, 'playerteamCity'].iloc[0] + ' ' + s.loc[s['player'] == name, 'playerteamName'].iloc[0] + 
      ' player ' + name + ' had ' + str(int(info)) + ' ' + stat + ' :sunglasses:')

