import streamlit as st
import qrcode
import graphviz as graphviz


st.set_page_config(page_title='IANCU colloquium', layout='wide')
topic = st.sidebar.selectbox(
	'',
	[
		'選擇要分享的內容',
		'為何改用Python進行研究工作？',
		'可以用Python解決哪些問題？',
		'如何藉由Python與天文維持關係？',
		'揪團用Python拉近群眾與星空的距離'
	]
)

if topic == '選擇要分享的內容':
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

if topic == '為何改用Python進行研究工作？':
	st.header('為何改用Python進行研究工作？')
	with st.expander('我的程式語言經歷'):
		st.subheader('我的程式語言經歷')
		graph = graphviz.Digraph()
		graph.edge('C、Linux shell script', 'IDL')
		graph.edge('IDL', 'HTML、CSS、JavaScript、PHP、SQL')
		graph.edge('IDL', 'MATLAB')
		graph.edge('MATLAB', 'Python')
		st.graphviz_chart(graph)

	with st.expander('在研究工作上改用Python的契機與成果'):
		st.subheader('在研究工作上改用Python的契機與成果')
		st.markdown('* 在國際天文會議及workshop耳聞Python')
		st.markdown('* 修「電波天文學」時用來分析資料的軟體CASA需要用到Python')
		st.markdown('* 看到[Why Astronomers Should Program in Python](http://bellm.org/blog/2011/05/27/why-astronomers-should-program-in-python/)這篇文章')
		st.markdown('* 2015年暑假為了帶高能天文Lab新生，編寫教材「[Python 基本語法與科學計算套件的使用](https://github.com/Astrohackers-TW/IANCUPythonAdventure/wiki/Python-%E5%9F%BA%E6%9C%AC%E8%AA%9E%E6%B3%95%E8%88%87%E7%A7%91%E5%AD%B8%E8%A8%88%E7%AE%97%E5%A5%97%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8)」')
		st.markdown('* 2015年參與紐約天文黑客松[Astro Hack Week](http://astrohackweek.org/2020/)的小成就：[Python Wrapper for Hilbert–Huang Transform MATLAB Package](https://github.com/HHTpy/HHTpywrapper)')
		st.markdown('* 基於開放科學精神，企圖將博班研究工作整理成[QPOpytracker](https://github.com/YihaoSu/QPOpytracker)')

if topic == '可以用Python解決哪些問題？':
	st.header('可以用Python解決哪些問題？')
	st.subheader('從天文所網頁工讀生轉職為承接網站開發及資料科學相關案子的遠距工作者')
	st.markdown('* PTT SOHO板上的[徵才文](https://www.ptt.cc/bbs/soho/M.1417694394.A.7F7.html)')
	st.markdown('* [卡米爾公司](https://cameo.tw/tw/)')

	st.subheader('從遠距工作經驗分享可以用Python解決哪些問題')
	with st.expander('網頁資料擷取(網路爬蟲)'):
		st.markdown('* 台經院的[FINDIT](https://findit.org.tw/index.aspx)網站需要抓取國內外群眾募資網站資料來分析趨勢')
		st.markdown('* 相關Python套件： [requests](https://docs.python-requests.org/en/latest/)、[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)、[Selenium](https://selenium-python.readthedocs.io/)、[Scrapy](https://scrapy.org/)')

	with st.expander('網站及API開發'):
		st.markdown('* 澎湖民宿[屋光拾舍Hygge](https://hygge.tw/)的網站')
		st.markdown('* 「[探索科博尋寶趣](https://cobofun.nmns.edu.tw/index.html)」app的內容上稿後台')
		st.markdown('* 文化資產災害示警系統')
		st.markdown('* 相關Python套件： [Django](https://www.djangoproject.com/)、[Django REST framework](https://www.django-rest-framework.org/)、[Flask](https://flask.palletsprojects.com/en/2.0.x/)、[FastAPI](https://fastapi.tiangolo.com/)')

	with st.expander('資料分析及視覺化'):
		st.markdown('* 分析IoT資料找出空氣汙染事件')
		st.markdown('* 相關Python套件： [Pandas](https://pandas.pydata.org/)、[GeoPandas](https://geopandas.org/en/stable/)、[Plotly](https://plotly.com/python/)、[Streamlit](https://streamlit.io/)')

	with st.expander('更多應用'):
		st.markdown('* 自動寄發Email及Line通知、自動讀寫Google Sheets和Drive上的檔案資料、...')
		st.markdown('* 歡迎參加[台灣Python年會](https://tw.pycon.org/2021/zh-hant)')
