import pyodbc
import pandas as pd
#from regex import D
import decode_AS400
from datetime import date

def main(ITEM_DOWN):
    userName = "PATRICKPHA"
    passWord ="IECI0022"


    connection_string = (
                "Driver={iSeries Access ODBC Driver};" 
                f"System=MILPROD;"
                f"DefaultLibraries=JDETSTDTA;"
                f"Uid={userName};"
                f"Pwd={passWord};"
                "ForceTranslation=0;"
                )

    conn = pyodbc.connect(connection_string)
    print("Done Connect")
    querry =f"""
                SELECT BOMSTID,BOMPIT,BOMSQS,BOMLVL,BOMCIT,BOMGQ0,BOMGQT,BOMSGT,BOMNQT,BOMRAT,BOMCDS,UNMSR,BOMPCL,BOMCCL,BOMSEQ,BOMSQF,PITTYP,ITTYP,BOMUUQ5 
                FROM 
                    RGNFILL.PSTBOMD  GRPORDH 
                WHERE 
                    BXDSTID in ('51') 
                    AND BOMPIT IN {ITEM_DOWN}
                """

    df =pd.read_sql(querry,conn)
    print("DONE QUERRY")
    #decode_AS400.decode_ebcdic_columns(df)
        
    df_fix = decode_AS400.decode_ebcdic_columns(df)
    df_fix 
    return df_fix
    # print("DONE FIX")
    # print(df_fix.head())
    # df_fix[0:100000].to_excel(f"{date.today()}.xlsx")

    # print(f"DONE WRITE TO EXCEL FILE: {date.today()}.xlsx")
        