import streamlit as st
import random
import numpy as np
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt

def source_info(path: str):
    st.page_link(
        path,
        label="Get Source",
        icon=":material/download:",
        help="Download source document"
    )

def crimes_detected_identified_page():
	df = pd.read_csv("data/total.csv")

	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Crimes Detected"], color="blue", marker="o", label="Crimes Detected", linewidth=3)
	ax.plot(df["Year"], df["Crimes Identified"], color="red", marker="o", label="Crimes Identified", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Crimes detected & identified", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ticks = np.arange(start=(df["Crimes Detected"].min() // 5000 * 5000), stop=(df["Crimes Identified"].max() + 5000), step=5000)
	ax.set_yticks(ticks)
	ax.set_yticklabels([f"{x//1000}K" for x in ticks])
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)
	
	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/232277/przestepstwa-ogolem-do-2021.xlsx")	

def detection_rate_page():
	df = pd.read_csv("data/total.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Detection Rate"], color="purple", marker="o", label="Detection rate", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Crime detection rates over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ticks = np.arange(start=(df["Detection Rate"].min() // 5 * 5), stop=(df["Detection Rate"].max() + 5), step=5)
	ax.set_yticks(ticks)
	ax.set_yticklabels([f"{x}%" for x in ticks])
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/232277/przestepstwa-ogolem-do-2021.xlsx")

def districts_page():
	st.subheader("Crime count by districts")
	df = pd.read_csv("data/districts.csv")
	column_layer = pdk.Layer(
		"ColumnLayer",
		data=df,
		get_position="[lon, lat]",
		get_elevation="value",
		elevation_scale=2,
		radius=1000,
		get_fill_color="[((value - 100) / (3000 - value)) * 255, (1 - ((value - 100) / (3000 - value))) * 255, 0, 100]",
	)
	
	df["value_str"] = df["value"].astype(str)
	text_layer = pdk.Layer(
		"TextLayer",
		data=df,
		get_position="[lon, lat]",
		get_text="value_str",
		get_color=[255, 255, 255],
		get_size=16,
		get_alignment_baseline="'top'",
		get_text_anchor="'middle'",
		get_pixel_offset="[5, 15]"
	)

	view_state = pdk.ViewState(
		latitude=df["lat"].mean(),
		longitude=df["lon"].mean(),
		zoom=10,
		pitch=45
	)

	st.pydeck_chart(pdk.Deck(
		layers=[column_layer, text_layer],
		initial_view_state=view_state,
		map_style="mapbox://styles/mapbox/dark-v11"
	))
	source_info("https://strazmiejska.waw.pl/statystyki/statystyki-z-podzialem-na-miesiace/8741-2025-03-interwencje-wlasne-straznikow-miejskich-z-podzialem-na-dzielnice")

def car_theft_page():
	df = pd.read_csv("data/car_theft.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Car Theft"], color="blue", marker="o", label="Car Thefts", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Car Thefts over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Car Theft"].min() // 100 * 100, stop=(df["Car Theft"].max() + 500), step=500))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/359930/kradziezesamochodow2013-2022.xlsx")

def piracy_page():
	df = pd.read_csv("data/piracy.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Piracy Act"], color="green", marker="o", label="Piracies", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Piracies over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Piracy Act"].min() // 100 * 100, stop=(df["Piracy Act"].max() + 200), step=200))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)

	source_info("https://statystyka.policja.pl/download/20/364186/prawo-autorskie-i-prawa-pokrewne-1999-2023.xlsx")

def battery_page():
	df = pd.read_csv("data/battery.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Battery"], color="brown", marker="o", label="Batteries", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Batteries over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Battery"].min() // 100 * 100, stop=(df["Battery"].max() + 100), step=100))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/338166/przestepstwa-przy-uzyciu-broni-2002-2023.xlsx")

def robbery_page():
	df = pd.read_csv("data/robbery.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Robbery"], color="pink", marker="o", label="Robberies", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Robberies over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Robbery"].min() // 400 * 400, stop=(df["Robbery"].max() + 400), step=400))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)	
	source_info("https://statystyka.policja.pl/download/20/338166/przestepstwa-przy-uzyciu-broni-2002-2023.xlsx")

def animal_abuse_page():
	df = pd.read_csv("data/animal_abuse.csv")

	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Animal Abuse"], color="yellow", marker="o", label="Animal Abuses", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Animal Abuse cases over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Animal Abuse"].min() // 100 * 100, stop=(df["Animal Abuse"].max() + 100), step=100))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/364187/ochrona-zwierzat-1999-2023.xlsx")

def murder_page():
	df = pd.read_csv("data/murder.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Murder Cases"], color="orange", marker="o", label="Murder Cases", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Murder cases over the years", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Murder Cases"].min() // 5 * 5, stop=(df["Murder Cases"].max() + 5), step=5))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
	source_info("https://statystyka.policja.pl/download/20/338166/przestepstwa-przy-uzyciu-broni-2002-2023.xlsx")

def main():
    st.set_page_config(page_title="Crime in Warsaw")

    pages = {
		"Crimes Detected & Identified": crimes_detected_identified_page,
        "Crime Detection Rate": detection_rate_page,
        "Crime in Districts": districts_page,
		"Car Theft": car_theft_page,
		"Piracy": piracy_page,
		"Battery": battery_page,
		"Robbery": robbery_page,
		"Animal Abuse": animal_abuse_page,
		"Murder": murder_page
    }

    choice = st.selectbox("Choose a page:", ["--Select--"] + list(pages.keys()))
    if choice != "--Select--":
        st.session_state["selected_page"] = choice
    else:
        if "selected_page" in st.session_state:
            del st.session_state["selected_page"]

    if st.button("Pick randomly"):
        st.session_state["selected_page"] = random.choice(list(pages.keys()))

    st.sidebar.header("Pages")
    for page in list(pages.keys()):
        if st.sidebar.button(page, key=f"sidebar_{page}"):
            st.session_state["selected_page"] = page

    if "selected_page" in st.session_state:
        pages[st.session_state["selected_page"]]()

main()
