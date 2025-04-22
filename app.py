
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Industrial Engineering Elective Flowchart</h1>", unsafe_allow_html=True)

# Use HTML/CSS layout to position buttons over the image
st.write("""
<style>
.container {
    position: relative;
    width: 1200px;
    height: 950px;
    margin: auto;
}
.bg {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    z-index: 0;
}
.button {
    position: absolute;
    background-color: rgba(0, 255, 0, 0.4);
    border: none;
    color: transparent;
    padding: 8px;
    font-size: 14px;
    cursor: pointer;
    z-index: 1;
}
#dataAnalytics { left: 470px; top: 370px; width: 111px; height: 71px; }
#imseElective1 { left: 910px; top: 480px; width: 111px; height: 71px; }
#imseElective2 { left: 1030px; top: 270px; width: 111px; height: 71px; }
#engineeringElective1 { left: 620px; top: 680px; width: 121px; height: 81px; }
#engineeringElective2 { left: 750px; top: 680px; width: 111px; height: 81px; }
</style>

<div class="container">
    <img src="https://raw.githubusercontent.com/ecshulda/IE-Elective-Flowchart/main/ie_flowchart_home.png" class="bg">
    <form action="?button=Data%20Analytics"><button id="dataAnalytics" class="button">Data Analytics</button></form>
    <form action="?button=IMSE%20Elective%201"><button id="imseElective1" class="button">IMSE Elective 1</button></form>
    <form action="?button=IMSE%20Elective%202"><button id="imseElective2" class="button">IMSE Elective 2</button></form>
    <form action="?button=Engineering%20Elective%201"><button id="engineeringElective1" class="button">Engineering Elective 1</button></form>
    <form action="?button=Engineering%20Elective%202"><button id="engineeringElective2" class="button">Engineering Elective 2</button></form>
</div>
""", unsafe_allow_html=True)

# Display elective info based on query param
query_params = st.query_params
button_clicked = query_params.get("button", [None])[0]

if button_clicked:
    st.markdown(f"<h3 style='text-align: center;'>{button_clicked} Options</h3>", unsafe_allow_html=True)
    if button_clicked == "Data Analytics":
        st.markdown("""<ol>
            <li><b>IMSE 441 – Experimental Design</b><br>
            <b>Offered in:</b> Fall and Spring<br>
            <b>Overview:</b> Design experiments and analyze results.<br>
            <b>Technical Skills:</b> ANOVA, factorial design, statistical testing<br>
            <b>Durable Skills:</b> Data analysis, precision, critical thinking<br>
            <b>⚠️ Note:</b> This course can only be selected once—either as a Data Analytics or IMSE elective.</li><br>
            <li><b>STAT 705 – Regression and ANOVA</b><br>
            <b>Offered in:</b> Fall<br>
            <b>Overview:</b> Regression modeling and ANOVA techniques.<br>
            <b>Technical Skills:</b> Linear models, diagnostics<br>
            <b>Durable Skills:</b> Statistical reasoning, modeling</li><br>
            <li><b>STAT 511 – Statistical Methods I</b><br>
            <b>Offered in:</b> Fall and Spring<br>
            <b>Overview:</b> Core stats for data analysis.<br>
            <b>Technical Skills:</b> Descriptive stats, hypothesis testing<br>
            <b>Durable Skills:</b> Quantitative reasoning, critical thinking</li>
        </ol>""", unsafe_allow_html=True)
    elif button_clicked == "IMSE Elective 1":
        st.markdown(f"""{elective_1_html_full}""", unsafe_allow_html=True)
    elif button_clicked == "IMSE Elective 2":
        st.markdown(f"""{elective_2_html_full}""", unsafe_allow_html=True)
    elif button_clicked == "Engineering Elective 1":
        st.markdown(f"""{eng_elective_1_html}""", unsafe_allow_html=True)
    elif button_clicked == "Engineering Elective 2":
        st.markdown(f"""{eng_elective_2_html}""", unsafe_allow_html=True)
