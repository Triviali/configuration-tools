import streamlit as st
import pandas as pd
import plotly.express as px
import pyperclip as pc
from PIL import Image
from streamlit_extras.let_it_rain import rain
st.set_page_config(page_title="Configuration Dashboard", page_icon="💻", layout="wide")
rain(
    emoji="💻",
    font_size=40,
    falling_speed=3,
    animation_length="1",
)

@st.cache_data

def get_data_from_excel():
    dfUser = pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="C:J, Q:V",
        nrows=250,
    )
    return dfUser
def get_data_from_excel_2():
    dfFilter = pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="J:P",
        nrows=250,
    )
    return dfFilter
def get_data_from_excel_3():
    dfSearch = pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="A:D, W:Y",
        nrows=250,
    )
    return dfSearch
def get_data_from_excel_4():
    dfGpumake =pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="Q",
        nrows=250,
    )
    return dfGpumake
def get_data_from_excel_5():
    dfGpumodel =pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="R",
        nrows=250,        
    )
    return dfGpumodel
def get_data_from_excel_6():
    dfGpumodel =pd.read_excel(
        io="Database.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="S",
        nrows=250,        
    )
    return dfGpumodel
dfUser = get_data_from_excel()
dfFilter = get_data_from_excel_2()
dfSearch = get_data_from_excel_3()
dfGpumake = get_data_from_excel_4()
dfGpumodel = get_data_from_excel_5()
dfGpumem = get_data_from_excel_6()



# Sidebar
# st.sidebar.header("Enter your second-page options here.")

# adapter = st.sidebar.selectbox(
#     "Select Adapter",
#     options=dfFilter["adapterIncluded"].unique(),
# )

# screen = st.sidebar.selectbox(
#     "Select LCD Condition",
#     options=dfFilter["screenCondition"].unique(),

# )

# keyboard = st.sidebar.selectbox(
#     "Select Keyboard Condition",
#     options=dfFilter["keyboardCondition"].unique(),
# )

# os = st.sidebar.selectbox(
#     "Select Operating System",
#     options=dfFilter["operatingSystem"].unique(),
# )

# battery_condition = st.sidebar.selectbox(
#     "Select Battery Condition",
#     options=dfFilter["battCond"].unique(),
# )

# cycle_count = st.sidebar.number_input(
#     "Select Cycle Count",
#     min_value=0,
#     max_value=1000,
# )

# gpu_make = st.sidebar.selectbox(
#     "Select GPU Make",
#     options=dfGpumake["gpuMake"].unique(),
# 
# )

# gpu_model = st.sidebar.selectbox(
#     "Select GPU Model",
#     options=dfGpumodel["gpuModel"].unique(),

# )

# gpu_mem = st.sidebar.selectbox(
#     "Select GPU Memory",
#     options=dfGpumem["gpuMem"].unique(),

# )
text_search = st.text_input("Type your entry in the box below to search for a configuration.", value='')
# lenovo_copy = st.sidebar.button("Copy 2nd Page for Lenovo Configuration")
# apple_copy = st.sidebar.button("Copy 2nd Page for Apple Configuraton")
# if lenovo_copy == True:
#     pc.copy(adapter + '\n' + screen + '\n' + keyboard + '\n' + os + '\n' + gpu_make + '\n' + gpu_model + '\n' + gpu_mem)
 #    lenovo_copy == False
#     st.toast("Copied to clipboard!")
# if apple_copy == True:
#     pc.copy(adapter + '\n' + screen + '\n' + keyboard + '\n' + os + '\n' + battery_condition + '\n' + str(cycle_count) + '\n' + gpu_make)
#     apple_copy == False
#     st.toast("Copied to clipboard!")

#dfFilter_selection = dfFilter.query(
#    "adapterIncluded == @adapter & screenCondition == @screen & keyboardCondition == @keyboard & operatingSystem == @os & battCond == @battery_condition"
# )

m1 = dfSearch["model"].str.contains(text_search)
m2 = dfSearch["cpuModel"].str.contains(text_search)
m3 = dfSearch["make"].str.contains(text_search)
m4 = dfSearch["machType"].str.contains(text_search)
m5 = dfSearch["appleFailcode"].str.contains(text_search)
m6 = dfSearch["comment"].str.contains(text_search)
m7 = dfSearch["tags"].str.contains(text_search)
df_result = dfUser[m1 | m2 | m3 | m4 | m5 | m6 | m7].transpose()

# Need to make records selectable
if text_search:
    st.dataframe(data=df_result, height=550, use_container_width=True)
