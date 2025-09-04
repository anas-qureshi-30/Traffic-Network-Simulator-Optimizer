import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
def dataProcessing(inputedFileName):
    fileName=inputedFileName
    df=pd.read_csv(fileName)
    #To read data from excel file
    #df=pd.read_excel()
    df=df.drop_duplicates()
    #df=df.drop_duplicates() to drop the duplicate columns from the table
    #df=df.drop(columns="column_name") to drop the particular coulmn

    #df["column_name"]=df["column_name"].str.lstrip("value")
    #df["column_name"]=df["column_name"].str.rstrip("value")
    #To remove the extra value for left and right side

    #df=df.replace() To change the value in whole table
    df["speed_limit"]=df["speed_limit"].str.replace("km/h","")
    return df
