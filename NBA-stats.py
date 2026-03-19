# NBA stats
import pandas as pd
import difflib
import sys
import streamlit as st


s = pd.read_csv(r"Moneymanan\My Stuff\Python\NBA Stats\PlayerStatistics.csv", usecols=range(32), dtype={8: "string", 9: "string"})
g = pd.read_csv(r"Moneymanan\My Stuff\Python\NBA Stats\Games.csv", usecols=range(12), dtype={8: "string", 10: "string"})

st.title(":sunglasses: NBA Stats :sunglasses:", text_alignment = "center")
st.header("Trying to fulfill my NBA dreams", text_alignment = "center")

valid_stats = list(s.columns)
s["player"] = s["firstName"] + " " + s["lastName"]
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

