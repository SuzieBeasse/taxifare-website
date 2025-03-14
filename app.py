import streamlit as st
import datetime
import requests

'''
# TaxiFare
'''

st.markdown('''
Let's find out how much this ride will cost you 🚕
''')
'''
## Your ride


'''
col_1, col_2, col_3 = st.columns(3)

with col_1:
    d = st.text_input('Pick-up time:', '2024-07-06 19:18:00')

with col_2:
    lat_p = st.number_input('Pick-up latitude:', -73.950655)

with col_3:
    lon_p = st.number_input('Pick-up longitude:', 40.783282)

col_4, col_5, col_6 = st.columns(3)
with col_4:
    p = st.number_input('Number of passenger:', 1)

with col_5:
    lat_d = st.number_input('Drop-off latitude:', -73.984365)

with col_6:
    lon_d = st.number_input('Drop-off longitude:', 40.769802)


# Let's call our API with these inputs
url = 'https://taxifare.lewagon.ai/predict'
params = {'pickup_datetime': d,
          'pickup_longitude': lon_p,
          'pickup_latitude': lat_p,
          'dropoff_longitude': lon_d,
          'dropoff_latitude': lat_d,
          'passenger_count': int(p)
          }

fare = requests.get(url=url, params=params).json()

'''
## Predicted fare
'''

col1, col2, col3 = st.columns(3)
col2.metric('Fare', f"${round(fare['fare'], 2)}")
