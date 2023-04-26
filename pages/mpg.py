import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.title('🚗MPG 자동차연비🚗')
st.sidebar.markdown("# MPG 🚗")

st.write("""
### 자동차 연비
""")

# mpg = sns.load_dataset("mpg")  # 내장 데이터셋 사용
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/raw/mpg.csv'
mpg = pd.read_csv(url)  # Github 링크로 사용

st.sidebar.header('검색하기')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max())))
   )

sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)