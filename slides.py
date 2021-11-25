import streamlit as st
import qrcode

st.set_page_config(page_title='IANCU colloquium', layout='wide')
st.title('離開天文所後，我如何藉由Python與天文繼續維持關係')
st.header('蘇羿豪@中央大學天文所 2021-12-3')

if st.button('開始'):
	_, col, _ = st.columns(3)
	with col:
		qr = qrcode.QRCode()
		qr.add_data(
			data='https://www.facebook.com/groups/1022708484514663'
		)
		qr_img = qr.make_image(fill='black', back_color='white')
		qr_img.save('./qrcode.png')
		st.subheader('「Python在天文領域的應用」FB社團')
		st.image('./qrcode.png')

st.sidebar.selectbox(
	'',
	[
		'選擇要分享的內容',
		'為何改用Python進行研究工作？',
		'可以用Python解決哪些問題？',
		'如何藉由Python與天文維持關係？',
		'揪團用Python拉近群眾與星空的距離'
	]
)