import streamlit as st
import pandas as pd
import numpy as np
from annotated_text import annotated_text

st.set_page_config(
    page_title = 'Streamlit',
    # page_icon = '✅',
    layout = 'wide'
)

head1, head2 = st.columns(2)

with head1:
    st.title ("Streamlit Data App")
    st.markdown("### Sample app to demonstrate usage of streamlit as a data app")

# --------------- Lottie animation-------------------------

from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with head2:
    file_url = 'https://assets10.lottiefiles.com/packages/lf20_sytxvxgf.json'
    lottie_book = load_lottieurl(file_url)
    st_lottie(lottie_book, speed=1, height=200, key="initial")

# ----------------------------------------------------------

st.markdown("## Visual 1")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "42.2 million", "12%")
col2.metric("Gross margin", "10 million", "-8%")
col3.metric("Margin", "20%", "10%")

st.markdown("## Visual 2")
chart1, chart2 = st.columns(2)

with chart1:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with chart2:
    chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

st.markdown("<hr/>",unsafe_allow_html=True)

st.markdown("## Visual 3")
from streamlit_player import st_player
# Embed a youtube video
st_player("https://www.youtube.com/watch?v=OkodDZxsN1I&t=195s")
st.markdown("<hr/>",unsafe_allow_html=True)

st.markdown("## Visual 4")
chart3, chart4 = st.columns(2)

from bokeh.plotting import figure, show

with chart3:
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')

    p.line(x, y, legend_label='Trend', line_width=2)
    st.bokeh_chart(p, use_container_width=True)

with chart4:
    # prepare some data
    x = [1, 2, 3, 4, 5]
    y1 = [6, 7, 2, 4, 5]
    y2 = [2, 3, 4, 5, 6]
    y3 = [4, 5, 5, 7, 2]

    # create a new plot with a title and axis labels
    p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")

    # add multiple renderers
    p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
    p.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")
    p.circle(x, y3, legend_label="Objects", color="yellow", size=12)

    # show the results
    st.bokeh_chart(p, use_container_width=True)

st.markdown("<hr/>",unsafe_allow_html=True)

# -------------------------------------------------------------
st.markdown("## Visual 5")

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)