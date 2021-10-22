#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
import seaborn as sns
import joblib


# In[2]:


park_data = pd.read_csv('liver.csv', encoding="ISO-8859-1")


# ## Analyzing the Dataset

# In[3]:


# park_data.head()


# In[4]:


# park_data.shape


# In[5]:


# park_data.info()


# In[6]:


# park_data.isnull().sum()


# In[7]:


park_data.dropna(inplace=True)
park_data.reset_index(inplace=True)


# In[8]:


# park_data.isnull().sum()


# In[9]:


# park_data.describe()


# Check for number of people having parkinsons and number of people who don't. The status column gives the data of people with and without Parkinson's Disease. The status **1** represents person has the disease and the stauts **0** represents that the person doesn't

# In[10]:


# park_data['result'].value_counts()


# In[11]:


# plt.title("Liver Disease Analyzer")
# sns.countplot(x='result', data=park_data)


# #### Correlation Heatmap
# 
# A correlation heatmap is a heatmap that shows a 2D correlation matrix between two discrete dimensions, using colored cells to represent data from usually a monochromatic scale. The values of the first dimension appear as the rows of the table while of the second dimension as a column. The color of the cell is proportional to the number of measurements that match the dimensional value. This makes correlation heatmaps ideal for data analysis since it makes patterns easily readable and highlights the differences and variation in the same data. A correlation heatmap, like a regular heatmap, is assisted by a colorbar making data easily readable and comprehensible.

# In[12]:


# plt.figure(figsize = (25, 25))
# sns.heatmap(park_data.corr(), annot=True, cmap='YlGnBu')


# Now, we group the data by the status and find the mean of all the attributes for better understanding

# In[13]:


# park_data.groupby(['result']).mean()


# ## Preprocessing
# 
# Separating the target (status) from rest of the features

# In[14]:


x = park_data.drop(columns=['result'])
y = park_data['result']


# In[15]:


# x


# In[16]:


# y


# Split the original full data into training data into testing data. Here, test size represents the percentage of data we want for testing. For example, test_size = 0.2 means that 20% of the data goes into testing and 80% goes to training. <br><br>
# The random_state attribute is used to reproduce the same result from earlier. The train_test_split randomly splits the data into training part and testing part. Now, if we do random_state = 1, then everytime we or anyone performs train_test_split on our code by keeping random_state as 1 will get same data for the training and testing data. Same goes with any other integer with random_state value. If random_state = 2, then values that we get might be diffrent from the values we got for random_state = 1, but everytime we will perform train_test_split by using random_state = 2, we will get same value.

# In[17]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)


# In[18]:


# print(x.shape, x_train.shape, x_test.shape) # second + third = first


# ## Data Standardization
# We need to standardize the data before moving forward. Our table has 22 features (after removing _name_ and _status_ columns). Now, we should standardize them to a range, without making them lose their meaning. The process of doing this is called **data standardization**. This is done by using the **StandardScaler()** that we imported above. It uses normal distribution (z = (x - μ) / σ)

# In[19]:


scaler = StandardScaler()


# In[20]:


# Fitting the data to be standardized into scaler, since we cannot randomly standardize

# scaler.fit(x_train)
# x_train = scaler.transform(x_train)

x_train = scaler.fit_transform(x_train)

# We don't fit the data into x_test since we want to test the data and if we put then model will get trained on test
# data as well
x_test = scaler.transform(x_test)


# In[21]:


# x_train # All values are in the range of -1 to 1.


# ## Model Training (Using SVM Model)

# In[22]:


model = RandomForestClassifier(max_depth=7, random_state=2) # SVC = Support Vector Classifier  Also has SVR (R for regressor)
# The list of kernels is ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ (Default is rbf (radial basis function))


# In[23]:


# Training the SVM Model with training data
model.fit(x_train, y_train)


# ## Model Evaluation

# In[24]:


# Find accuracy score on training data
# y_pred_train = model.predict(x_train)
# training_acc = accuracy_score(y_train, y_pred_train)


# In[25]:


# training_acc # Accuracy score above 0.75 (75%) is considered to be a good accuracy score (Too much is bad - overfitting)


# In[26]:


# y_pred_test = model.predict(x_test)
# test_acc = accuracy_score(y_test, y_pred_test)


# In[27]:


# test_acc # Accuracy score close to training accuracy shows that model is good. Else, it might be sign of overfitting


# In[28]:


# cm = confusion_matrix(y_test, y_pred_test)
# fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Blues)
# plt.xlabel('Predictions', fontsize=18)
# plt.ylabel('Actuals', fontsize=18)
# plt.title('Confusion Matrix', fontsize=18)
# plt.show()


# In[ ]:

filename = 'Liver.sav'
joblib.dump(model, filename)


