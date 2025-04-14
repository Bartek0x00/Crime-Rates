import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def source_info(path: str):
    st.page_title(
        path,
        label="Get Source",
        icon=":material/download:",
        help="Download source document"
    )

def detection_rate_page():
	df = pd.read_csv("data/total.csv")
	
	plt.style.use("dark_background")

	fig, ax = plt.subplots(figsize=(8, 4))
	ax.plot(df["Year"], df["Detection Rate"], color="purple", marker="o", label="Detection rate (%)", linewidth=3)
	ax.set_xlabel("Year", fontsize=12)
	ax.set_title("Crime detection rates over time", fontsize=16)
	ax.legend()

	ax.set_xticks(df["Year"])
	ax.set_yticks(np.arange(start=df["Detection Rate"].min(), stop=(df["Detection Rate"].max() + 4), step=4))
	ax.tick_params(axis="x", rotation=315)
	fig.tight_layout()
	ax.grid(True, linestyle="--", alpha=0.5)

	st.pyplot(fig)
    source_info("https://statystyka.policja.pl/download/20/232277/przestepstwa-ogolem-do-2021.xlsx")

def districts_page():
    df = pd.read_csv("data/districts.csv")
    
    source_info("districts")

def main():
    st.set_page_config(
        page_title="Crime in Warsaw",
        layout="wide",
        theme={
            "backgroundColor": "#2C3E50",
            "secondaryBackgroundColor": "#34495E",
            "primaryColor": "#CC44EE"
        }
    )

    pages = {
        "Detection rate": detection_rate_page,
        "Districts": districts_page
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
