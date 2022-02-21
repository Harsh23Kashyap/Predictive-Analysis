# -*- coding: utf-8 -*-
"""Assi3.ipynb
HARSH KASHYAP
101917088
Thapar Institute of Engineering and Technology
Installing pycaret
"""

!pip install pycaret &> /dev/null
print ("Pycaret installed sucessfully!!")

"""Importing pandas and pycaret"""

import pandas as pd
from pycaret.datasets import get_data
from pycaret.classification import *

"""Importing output file"""

prompt = input("Type in your File name: ")
 data=pd.read_csv(prompt)

"""# NORMALIZATION

DATA WITHOUT ANY NORMALIZATION**
"""

setup(data=data, target='Target', silent=True) # Change the target parameter in every setup function in the code i.e. it will not be 'Class variable', it will be 'Target' in the whole code.
model = compare_models()

"""Extracting the accuracy of dataset"""

callout=pull()
noNormalise=callout[["Accuracy"]]

"""ZScore Normalisation of data and finding the accuracy of dataset"""

setup(data=data,target='Target',normalize = True, normalize_method = 'zscore', silent=True)
model = compare_models()
callout=pull()
zscore=callout[["Accuracy"]]

"""MinMax Normalisation of data and finding the accuracy of dataset"""

setup(data=data,target='Target',normalize = True, normalize_method = 'minmax', silent=True)
model = compare_models()
callout=pull()
minmax=callout[["Accuracy"]]

"""Maxabs Normalisation of data and finding the accuracy of dataset"""

setup(data=data,target='Target',normalize = True, normalize_method = 'maxabs', silent=True)
model = compare_models()
callout=pull()
maxabs=callout[["Accuracy"]]

"""Robust Normalisation of data and finding the accuracy of dataset"""

setup(data=data,target='Target',normalize = True, normalize_method = 'robust', silent=True)
model = compare_models()
callout=pull()
robust=callout[["Accuracy"]]

model=list(noNormalise.index)
#MAKE Model headings
mod=pd.DataFrame({'model':model},index=model)
#Make and join all normalisation
file1 = [mod,noNormalise,zscore,minmax,maxabs,robust]
columnheading=["Model","Accuracy without Normalization","Normalization(z-score)","Normalization(min-max)","Normalization (maxabs)","Normalization (robust)"]

#concatinating 
file_normalisation=pd.concat(file1,axis=1).set_axis(columnheading, axis=1)
file_normalisation.to_csv("output-101917088-Normalization.csv",index=False)

"""# FEATURE EXTRACTION

Feature extraction classic 0.2
"""

setup(data=data,target='Target',feature_selection = True, feature_selection_method = 'classic', feature_selection_threshold = 0.2, silent=True)
model = compare_models()
callout=pull()
classic2=callout[["Accuracy"]]

"""Feature extraction classic 0.5"""

setup(data=data,target='Target',feature_selection = True, feature_selection_method = 'classic', feature_selection_threshold = 0.5, silent=True)
model = compare_models()
callout=pull()
classic5=callout[["Accuracy"]]

"""Feature extraction boruta 0.2"""

setup(data=data,target='Target',feature_selection = True, feature_selection_method = 'boruta', feature_selection_threshold = 0.2, silent=True)
model = compare_models()
callout=pull()
boruta2=callout[["Accuracy"]]

"""Feature extraction boruta 0.5"""

setup(data=data,target='Target',feature_selection = True, feature_selection_method = 'boruta', feature_selection_threshold = 0.5, silent=True)
model = compare_models()
callout=pull()
boruta5=callout[["Accuracy"]]

model=list(noNormalise.index)
#MAKE Model headings
mod=pd.DataFrame({'model':model},index=model)
#Make and join all normalisation
file2 = [model,noNormalise,classic2,classic5,boruta2,boruta5]
columnheading=["Model","Accuracy without Feature Selection","Feature Selection. (Classic=0.2)","Feature Selection. (Classic=0.5)","Feature Selection. (Boruta=0.2)","Feature Selection. (Boruta=0.5)"]
#concatinating 
file_featureselect=pd.concat(file2,axis=1).set_axis(columnheading, axis=1)
file_featureselect.to_csv("output-101917088-FeatureSelection.csv",index=False)

"""# **Removing Outliers**

Threshold 0.02
"""

setup(data=data,target='Target',remove_outliers = True, outliers_threshold = 0.02, silent=True)
model = compare_models()
callout=pull()
thresh2=callout[["Accuracy"]]

"""Threshold 0.04"""

setup(data=data,target='Target',remove_outliers = True, outliers_threshold = 0.04, silent=True)
model = compare_models()
callout=pull()
thresh4=callout[["Accuracy"]]

"""Threshold 0.06"""

setup(data=data,target='Target',remove_outliers = True, outliers_threshold = 0.06, silent=True)
model = compare_models()
callout=pull()
thresh6=callout[["Accuracy"]]

"""Threshold 0.08"""

setup(data=data,target='Target',remove_outliers = True, outliers_threshold = 0.08, silent=True)
model = compare_models()
callout=pull()
thresh8=callout[["Accuracy"]]

model=list(noNormalise.index)
#MAKE Model headings
mod=pd.DataFrame({'model':model},index=model)
#Make and join all normalisation
file3 = [mod,noNormalise,thresh2,thresh4,thresh6,thresh8]
columnheading=["Model","Accuracy without Outlier Removal","Outlier Removal. (Treshhold=0.02)","Outlier Removal. (Treshhold=0.04)","Outlier Removal. (Treshhold=0.06)","Outlier Removal. (Treshhold=0.08)"]
#concatinating 
file_removeOutlier=pd.concat(file3,axis=1).set_axis(columnheading, axis=1)
file_removeOutlier.to_csv("output-101917088-OutlierRemoval.csv",index=False)

"""# **PCA **

Linear PCA
"""

setup(data=data,target='Target',pca = True, pca_method = 'linear', silent=True)
model = compare_models()
callout=pull()
linear=callout[["Accuracy"]]

"""Kernel PCA"""

setup(data=data,target='Target',pca = True, pca_method = 'kernel', silent=True)
model = compare_models()
callout=pull()
kernel=callout[["Accuracy"]]

"""Incremental PCA"""

setup(data=data,target='Target',pca = True, pca_method = 'incremental', silent=True)
model = compare_models()
callout=pull()
incremental=callout[["Accuracy"]]

model=list(noNormalise.index)
#MAKE Model headings
mod=pd.DataFrame({'model':model},index=model)
#Make and join all normalisation
file4 = [mod,noNormalise,linear,kernel,incremental]
columnheading=["Model","Accuracy without PCA","PCA -(Method - Linear)","PCA -(Method - Kernel)","PCA -(Method - Incremental)"]
#concatinating 
file_PCA=pd.concat(file4,axis=1).set_axis(columnheading, axis=1)
file_PCA.to_csv("output-101917088-PCA.csv",index=False)

"""# **Confusion Matrix**

Comparing various Models
"""

setup(data=data, target='Target', silent=True)
modelCompare = compare_models()
plot_model(modelCompare, plot='confusion_matrix',save=True)

import os  
os.rename('Confusion Matrix.png','output-101917088-ConfusionMatrix.png')

plot_model(modelCompare, plot='auc',save=True)
os.rename('AUC.png','output-rollnumber-AUC.png')

plot_model(modelCompare, plot='boundary',save=True)
os.rename('Decision Boundary.png','output-rollnumber-Decision Boundary.png')

plot_model(modelCompare, plot='feature',save=True)
os.rename('Feature Importance.png','output-rollnumber-FeatureImportance.png')

plot_model(modelCompare, plot='learning',save=True)
os.rename('Learning Curve.png','output-rollnumber-LearningCurve.png')
