import streamlit as st
import main
import pandas as pd
import io

st.title("DOWN BOM BY ITEM")
df = pd.DataFrame()
st.header("INPUT AREA")
querry_ITEM_TEXT = "( "
dem_Dung = 0 
ITEM = st.text_input("ITEM DOWN: ")


if st.button("SHOW DATA"):
    split_ITEM = ITEM.split(" ")
    for i in split_ITEM:
        if dem_Dung < len(split_ITEM)-1:
            dem_Dung = dem_Dung + 1
            querry_ITEM_TEXT = querry_ITEM_TEXT + "'"+i+"',"
        else:
            querry_ITEM_TEXT = querry_ITEM_TEXT + "'"+i+"')"

    print(querry_ITEM_TEXT)
    df =  main.main(ITEM_DOWN=querry_ITEM_TEXT)
    st.dataframe(df)
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
if st.download_button("DOWN BOM" ,data=buffer.getvalue(),file_name=f"processed.xlsx"):
    st.write("DONE")
