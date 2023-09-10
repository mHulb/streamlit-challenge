import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

#fig, ax = plt.subplots(2, 2)
#ax[0][0].plot(np.arange(10), np.random.randn(10))

st.header('st.write')

# Example 1
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

st.write(df)

# Example 4
st.write('Below is a dataframe: :poop:', df, 'Above is a dataframe.')

# Example 5
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)