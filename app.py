import streamlit as st
import pickle
import pandas as pd


pipe= pickle.load(open("pipe.pkl","rb"))
st.title("IPL WIN PREDICTOR")

teams=[
    'Rajasthan Royals',
    'Royal Challengers Bangalore',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Chennai Super Kings',
    'Gujarat Titans',
    'Lucknow Super Giants',
    'Kolkata Knight Riders',
    'Mumbai Indians',
    'Kings XI Punjab',
]

cities= ['Hyderabad', 'Dubai', 'Jaipur', 'Centurion', 'Johannesburg',
       'Ahmedabad', 'Kimberley', 'Visakhapatnam', 'Cape Town', 'Ranchi',
       'Raipur', 'Nagpur', 'Durban', 'Indore', 'Cuttack', 'Sharjah',
       'Navi Mumbai', 'Port Elizabeth', 'East London', 'Bloemfontein']

cols1, cols2 = st.columns(2)
with cols1:
    batting_team=st.selectbox("Select batting team",sorted(teams))
with cols2:
    boaling_team=st.selectbox("Seclect boaling team",sorted(teams))

city=st.selectbox("Select host city",sorted(cities))

target=st.number_input("Target")

cols3,cols4,cols5 = st.columns(3)
with cols3:
    score=st.number_input("score")
with cols4:
    overs=st.number_input("Overs")
with cols5:
    wickets=st.number_input("Wickets out")

if st.button("Predict probability"):
   runs_left=target-score
   balls_left=120-(overs*6)
   wickets=10-wickets
   crr=score/overs
   rrr=(runs_left*6)/balls_left

   input_df=pd.DataFrame({'BattingTeam':[batting_team], 'BoalingTeam':[boaling_team],'City':[city],
              'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets],
               'total_run_x':[target],'crr':[crr],'rrr':[rrr]})



   result=pipe.predict_proba(input_df)


   loss=result[0][0]
   win=result[0][1]

   st.text(batting_team+'-'+str(round(win*100))+'%')
   st.text(boaling_team + '-'+ str(round(loss*100)) + '%')