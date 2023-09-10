import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Slider')

age = st.slider('How old are you boy?', 0, 130, 25)
st.write("I'm", age, 'years old, boy.')

# Example 2
st.subheader('Range slider')

values = st.slider(
    'Dude, just select a range of values!',
    0.0, 100.0, (25.0, 75.0))

st.write('The shit you selected:', str(values[0]), ' - ', str(values[1]))

# Example 4
st.subheader('Datetime slider')
start_time = st.slider(
    'When the fuck do we start?',
    value=datetime(2043, 1, 1, 9, 30),
    format="DD/MM/YY - hh:mm"
)

st.write("Seriously, we start at", start_time, "??? :poop:")