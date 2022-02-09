

#HARSH KASHYAP
#101917088
#CSE 4
#Thapar Institute of Engineering and Technology
#8051625669

#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import logging
from datetime import datetime

#Creating customized exception classes to handle all the exceptions presented as per the question.
#
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ParameterError(Error):
    """Raised when input is not a csv file"""
    pass


class Columns(Error):
    """Raised when no. of columns is not 3"""
    pass

class Empty(Error):
    """Raised when cells are null"""
    pass

class XValues(Error):
    """Raised when cells are X"""
    pass

class DoesNotMatch(Error):
    """Raised when a different csv file is entered"""
    pass

# importing the module

# Creating a log file with my roll no to store all the errors
f = open("101917088-log.txt", "a")
f.write("\n--------------------------------------------------------------------------\n")
#Writing log errors of all kind
f.write("\nHARSH KASHYAP\nLOG ERRORS OF ALL KIND WITH TIME\n\n")
f.write("New Execution\n")

f.write("FOR QUESTION 1\n")


while True:
    #to store the timr when a particular error occured and was handled
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    prompt = input("\nHello to Output Generator,""\nType in your File path: ")
    try:
      #if its not a csv extension then
        if(prompt[-4:]!=".csv"):
           raise ParameterError
        df=pd.read_csv(prompt)
        #if it doesnt have 3 columns
        if(df.shape[1]!=3):
            raise Columns
        #if it has three columns and the columns are not Roll No., Submission and Marks
        if(not(df.columns[0]=='RollNumber' and df.columns[1]=='Submission' and df.columns[2]=='Marks')):
            raise DoesNotMatch
    #if the file path given is wrong
    except FileNotFoundError as Argument:
        print("File Not Found")
        f.write(date+ str("- \tWrong file path\n"))
        f.write(date+ str("- \t")+str(Argument)+"\n")
    #if its not a csv file
    except ParameterError:
        f.write(date+ str("- \tNot a csv file. -'")+prompt+str("' . - Please enter a csv file\n"))
        print("Please Enter a correct csv file")
    #if it doesnt have desired no. of columns
    except Columns:
        f.write(date+ str("- \tNot a correct csv file. '-")+prompt+str("'- \tNumber of Columns not right. Expected 3. Got "+str(df.shape[1])+str("\n")))
        print("Please Enter a correct csv file")
    except DoesNotMatch:
        f.write(date+ str("- \tNot the correct csv file. '")+prompt+str("' . Columns expected to be [RollNumber, Submission, Marks]. Instead got "+str(df.columns)))
        print("Please Enter a correct csv file")
    else:
        break

#to count no. of null values
a=df.isnull().sum()
try:
  now = datetime.now()
  date = now.strftime("%d/%m/%Y %H:%M:%S")
  #Add exception if there are null values
  if [a>0]:
    raise Empty
except Empty:
    f.write(date+ str("- \tThe file contains empty values.\n"))

try:
  now = datetime.now()
  date = now.strftime("%d/%m/%Y %H:%M:%S")
  #add exception if there are values with 'X'
  if(df["Marks"]=='X').bool:
    raise XValues
except XValues:
    f.write(date+ str("- \tThe file contains X values.\n"))


#Make a new Dataframe with only unique roll no.
uniqueRoll=df['RollNumber'].unique()
newDf=pd.DataFrame(uniqueRoll,columns=["RollNumber"])

#Make colums for each submission and assign them with value zero
newDf['P1']=0
newDf['P2']=0
newDf['P3']=0
newDf['P4']=0
newDf['P5']=0
newDf['P6']=0
#Make roll no. as index
newDf=newDf.set_index('RollNumber')

#For each roll no and each submission add them to the particular row and column 
for i in range(df.shape[0]):
  roll=df.iloc[i,0]
  submission=df.iloc[i,1]
  marks=df.iloc[i,2]
  newDf.loc[roll,submission]=marks

#Reset the roll no. index
newDf.reset_index(level=0, inplace=True)

#Saving the csv file
newDf.to_csv(r'101917088-output.csv',index=False,header=True)

#Closing file
f.close()
