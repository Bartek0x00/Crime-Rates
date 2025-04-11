import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib.colors import LinearSegmentedColormap as lscmap

@st.cache_data
def load_data(filepath: str) -> pd.DataFrame:
	return pd.read_excel(
		filepath, 
		engine='openpyxl',
		skiprows=2,
		usecols="A:E"
	)

@st.cache_data
def filter_data(data: pd.DataFrame) -> pd.DataFrame:
	data = data[
		data['Jednostka podziału administracyjnego'] == 'Polska'
	].iloc[:, 1:]
	
	for col in data.select_dtypes(include='float64'):
		data[col] = data[col].map('{:.0f}'.format)
	
	return data
	
green_red_cmap = lscmap.from_list(
	'green_red', ['green', 'orange', 'red'], N=256
)
red_green_cmap = lscmap.from_list(
	'red_green', ['red', 'orange', 'green'], N=256
)

def main():
	filepath = 'https://statystyka.policja.pl/download/20/232277/przestepstwa-ogolem-do-2021.xlsx' 	
	
	data = filter_data(load_data(filepath))

	st.title('Crimes in Poland 1999 - 2021')
	st.dataframe(
		data.set_index('Rok').style
		.background_gradient(cmap=red_green_cmap, subset=['% wykrycia'])
		.background_gradient(cmap=green_red_cmap, subset=['Przestępstwa stwierdzone']),
		height=842		
	)
	
	st.subheader('Area chart')
	st.plotly_chart(px.area(
		data,
		x='Rok',		
		y='Przestępstwa stwierdzone',
		title='Crimes identified',
		markers=True
	))

	st.subheader('Column chart')
	st.plotly_chart(px.bar(
		data,
		x='Rok',
		y='Przestępstwa wykryte',
		title='Crimes'
	))

main()

