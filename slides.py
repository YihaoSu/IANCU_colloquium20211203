import streamlit as st

st.set_page_config(page_title='IANCU colloquium', layout='wide')
st.title('離開天文所後，我如何藉由Python與天文繼續維持關係')

st.header('蘇羿豪@中央大學天文所 2021-12-3')

st.sidebar.selectbox(
	'', ['選擇次標題', '次標題1', '次標題2', '次標題3']
)