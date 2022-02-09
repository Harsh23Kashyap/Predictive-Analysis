
#HARSH KASHYAP
#101917088
#CSE 4
#Thapar Institute of Engineering and Technology
#8051625669

#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
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
f.write("New Execution\n")

f.write("FOR QUESTION 2\n")

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
        if(df.shape[1]!=7):
            raise Columns
        #if it has three columns and the columns are not Roll No., Submission and Marks
        if(not(df.columns[0]=='RollNumber' and df.columns[1]=='P1' and df.columns[2]=='P2' and df.columns[3]=='P3' and df.columns[4]=='P4' and df.columns[5]=='P5' and df.columns[6]=='P6')):
            raise DoesNotMatch
    #if the file path given is wrong
    except FileNotFoundError as Argument:
        print("File Not Found")
        f.write(date+ str("- \tWrong file path\n"))
        f.write(date+ str("- \t")+str(Argument)+"\n")
    #if its not a csv file
    except ParameterError:
        f.write(date+ str("- \tNot a csv file.")+prompt+str("Please enter a csv file\n"))
        print("Please Enter a correct csv file")
    #if it doesnt have desired no. of columns
    except Columns:
        f.write(date+ str("- \tNot a correct csv file.")+prompt+str("- \tNumber of Columns not right. Expected 3. Got "+str(df.shape[1])+str("\n")))
        print("Please Enter a correct csv file")
    except DoesNotMatch:
        f.write(date+ str("- \tNot the correct csv file.")+prompt+str(" Columns expected to be [RollNumber, Submission, Marks]. Instead got "+str(df.columns)))
        print("Please Enter a correct csv file")
    else:
        break

#GENERATING VARIOUS STATTISTICS
#Statistics file
stat = open("101917088-statistics.txt", "a")
stat.write("Harsh Kashyap\n101917088\nThapar\n")
stat.write("--------------------------------------------------------------------------\n")

#COUNT NON NUMERIC VALUES 
add=0;
nonNumeric=[]
stat.write("\n\nNon numerical Values Count :\n")
for i in range(1,7):
  col="P"+str(i)
  mask=pd.to_numeric(df[col], errors='coerce').isna()
  curr=mask.sum()
  nonNumeric.append(curr)
  add=add+curr
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add)+"\n")
stat.write("--------------------------------------------------------------------------\n")

#Adding string values as error to log files
try:
  now = datetime.now()
  date = now.strftime("%d/%m/%Y %H:%M:%S")
  #add exception if there are values with 'X'
  if(add>0):
    raise XValues
except XValues:
    f.write(date+ str("- \tThe file contains X values. Replacing them with median.\n"))

#COUNT NULL VALUES
add=0;
nullVal=[]
stat.write("\nNull Values Count :\n")
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].isnull().sum()
  add=add+curr
  nullVal.append(curr)
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add)+"\n")
stat.write("--------------------------------------------------------------------------\n")
#Adding null values as error to log files
try:
  now = datetime.now()
  date = now.strftime("%d/%m/%Y %H:%M:%S")
  #Add exception if there are null values
  if add>0:
    raise Empty
except Empty:
    f.write(date+ str("- \tThe file contains empty values. Replacing them with median.\n"))

df=df.replace('-',0)
df=df.replace('X',0)
df=df.replace('NAN',0)
df=df.replace(np.nan,0)
#CHANGING ANY STR TO NO.
for i in range(1,df.shape[1]):
  col="P"+str(i)
  df[col]=df[col].astype(int)

#COUNT MEAN FOR EACH COLUMN
add=0;
stat.write("\nMEAN Values Count :\n")
meanValues=[];
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].mean()
  add=add+curr
  meanValues.append(curr)
  stat.write("For Column "+col +" : "+str(curr)+"\n")

tot=add/df.shape[0]
meanValues.append(tot)
stat.write("For Total : "+str(tot)+"\n")
stat.write("--------------------------------------------------------------------------\n")

#COUNT MEDIAN FOR EACH COLUMN
stat.write("\nMEDIAN Values Count :\n")
medianValues=[];
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].median()
  #print(curr)
  medianValues.append(curr)
  add=add+curr
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add/df.shape[0])+"\n")
stat.write("--------------------------------------------------------------------------\n")

#COUNT MIN FOR EACH COLUMN
stat.write("\nMINIMUM Values  :\n")
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].min()
  add=add+curr
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add/df.shape[0])+"\n")
stat.write("--------------------------------------------------------------------------\n")

#COUNT MAX FOR EACH COLUMN
stat.write("\nMAXIMUM Values  :\n")
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].max()
  add=add+curr
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add/df.shape[0])+"\n")
stat.write("--------------------------------------------------------------------------\n")

#COUNT STANDARD DEVIATION FOR EACH COLUMN
stat.write("\nSTANDARD DEVIATION  Values  :\n")
for i in range(1,df.shape[1]):
  col="P"+str(i)
  curr=df[col].std()
  #print(curr)
  add=add+curr
  stat.write("For Column "+col +" : "+str(curr)+"\n")


stat.write("For Total : "+str(add/df.shape[0])+"\n")
stat.write("--------------------------------------------------------------------------\n")

#MAKING GRAPHS
position=["P1","P2","P3","P4","P5","P6","Total"]

#MAKING Bar Plot OF MEANS of P1, P2,P3, P4 ,P5, P6 and total
import seaborn as sns
plt.figure(figsize=(8, 6), dpi=80)
plt.bar(position,meanValues,color='pink')
plt.grid()
plt.xlabel("Submissions")
plt.ylabel("Mean Marks")
plt.title("Means Marks (by Harsh Kashyap)")
plt.savefig("101917088-bar(Mean Marks).png")

#MAKING Bar Plot OF Median of P1, P2,P3, P4 ,P5, P6
import seaborn as sns
plt.figure(figsize=(8, 6), dpi=80)
plt.bar(position[:-1],medianValues,color='cyan')
plt.grid()
plt.xlabel("Submissions")
plt.ylabel("Median Marks")
plt.title("Median Marks  (by Harsh Kashyap)")
plt.savefig("101917088-bar(Median Marks).png")

#Histogram PLOT FOR MAXIMUM FOR EACH ROLL NO.
plt.figure(figsize=(8, 6), dpi=80)
plt.grid()
plt.xlabel("Maximum Marks")
plt.ylabel("No. of Students")
plt.title("Histogram Of No. of Students having Maximum Marks greater than or equal to ")
maximumPerRoll=df.iloc[:,1:].max(axis=1)
plt.hist(maximumPerRoll,color='orange')
plt.savefig("101917088-histogram(Maximum Marks).png")

#Histogram PLOT FOR MAXIMUM FOR EACH ROLL NO.
plt.figure(figsize=(8, 6), dpi=80)
plt.grid()
plt.xlabel("Maximum Marks")
plt.ylabel("No. of Students")
plt.title("Histogram Of No. of Students having Minimum Marks greater than or equal to  (by Harsh Kashyap)")
minimumPerRoll=df.iloc[:,1:].min(axis=1)
plt.hist(maximumPerRoll,color='purple')
plt.savefig("101917088-histogram(Minimum Marks).png")

#Histogram PLOT FOR Standard variation/ Mean Marks FOR EACH SUBMISSION.
plt.figure(figsize=(8, 6), dpi=80)
plt.grid()
plt.xlabel("Submission")
plt.ylabel("Marks")
plt.title("Standard Variation/ Mean of Marks with respect to Submission  (by Harsh Kashyap)")
standard=df.std()
meanmarks=df.mean()
plt.plot(standard[1:],color='red',marker='*',label="Standard Variation")
plt.plot(meanmarks[1:],color='green',marker='o',label="Mean Marks")
plt.legend()
plt.savefig("101917088-line.png")

#Non Numeric Values in each Submission
plt.figure(figsize=(8, 6), dpi=80)
myexplode = [0.1, 0, 0, 0, 0, 0]
plt.title("Non Numeric value %age in each Submission  (by Harsh Kashyap)")
plt.pie(nonNumeric, labels = position[:-1], explode = myexplode, autopct='%1.2f%%',shadow = True)
plt.show() 
plt.savefig("101917088-pie(Non Numeric Count).png")

#Null Values in each Submission
plt.figure(figsize=(8, 6), dpi=80)
plt.title("Null value %age in each Submission  (by Harsh Kashyap)")
plt.pie(nullVal, labels = position[:-1], explode = myexplode, autopct='%1.2f%%',shadow = True)
plt.show() 
plt.savefig("101917088-pie(Null Count).png")


stat.close()
f.close()
