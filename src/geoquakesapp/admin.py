from django.contrib import admin

from datetime import datetime
from inspect import Parameter
from django.contrib import admin


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from  sklearn.metrics import accuracy_score, confusion_matrix , recall_score , precision_score , f1_score ,classification_report,plot_confusion_matrix



import django_heroku
from .models import Quake, Quake_Predections
#import models.Quake


# Register your models here.
admin.site.register(Quake)
admin.site.register(Quake_Predections)


if Quake.objects.all().count()==0 :
    #Add The 1965 - 2016 earthquaks datasets 
    url1= "https://res.cloudinary.com/dehovuerv/raw/upload/v1635721947/database_tztbx5.csv"
    df = pd.read_csv(url1,sep=",")
    # preview df
    #print(df.head())

    df_load =  df.drop(['Time',	'Depth Error','Depth Seismic Stations',	'Magnitude Error',	'Magnitude Seismic Stations'	,'Azimuthal Gap'	,'Horizontal Distance',
    	'Horizontal Error',	'Root Mean Square'	,	'Source'	,'Location Source',	'Magnitude Source',	'Status'] , axis=1)
    # preview df_load
    #print(df_load.head())
    # cleaning Df
    df_load = df_load.rename(columns={'Magnitude Type':"Magnitude_Type"})

    # preview df_load
    # print(df_load.head())

    # Insert the  records into the Quake model /table

    for index , row in df_load.iterrows():
        Date = row['Date']
        latitude = row["Latitude"]
        longitude = row["Longitude"]
        Type = row["Type"]
        Depth = row["Depth"]
        Magnitude = row["Magnitude"]
        Magnitude_type = row["Magnitude_Type"]
        ID = row["ID"] 

        Quake(Date=Date, latitude=latitude , longitude = longitude , Type=Type ,Depth=Depth , Magnitude=Magnitude
        , Magnitude_type=Magnitude_type , ID=ID).save()


print("1")
if Quake_Predections.objects.all().count()==0:
    # ass the 2017 test data and the 1965 - 2016 training data 
    url2="https://res.cloudinary.com/dehovuerv/raw/upload/v1635722055/earthquakeTest_bx8ktr.csv"
    df_test = pd.read_csv(url2,sep=",")
    url1= "https://res.cloudinary.com/dehovuerv/raw/upload/v1635721947/database_tztbx5.csv"
    df_train = pd.read_csv(url1,sep=",")

    df_train_load = df_train.drop(['Time',	'Depth Error','Depth Seismic Stations',	'Magnitude Error',	'Magnitude Seismic Stations'	,'Azimuthal Gap'	,'Horizontal Distance',
    	'Horizontal Error',	'Root Mean Square'	,	'Source'	,'Location Source',	'Magnitude Source',	'Status'] , axis=1)

    df_test_load = df_test[['time' , 'latitude' , 'longitude' , 'mag' , 'depth' ]]

    df_train_load =  df_train_load.rename(columns={'Magnitude Type':"Magnitude_Type"})
    df_train_load =  df_train_load.rename(columns={'time':"Date" ,'latitude':'Latitude','longitude':"Longitude",'mag':'Magnitude'
    ,'depth':'Depth'})

    df_test_load =  df_test_load.rename(columns={'time':"Date" ,'latitude':'Latitude','longitude':"Longitude",'mag':'Magnitude'
    ,'depth':'Depth'})

    print("2")
    # create training and test dataframes
    df_test_data = df_test_load[['Latitude',"Longitude",'Magnitude','Depth']]
    df_train_data =  df_train_load[['Latitude',"Longitude",'Magnitude','Depth']]

    # Remove all null values from the datasets
    df_test_data.dropna()
    df_train_data.dropna()

    # Create training data featured
    X = df_train_data[['Latitude',"Longitude"]]
    y = df_train_data[['Magnitude','Depth']]

    # Create Test data features
    X_new = df_test_data[['Latitude',"Longitude"]]
    y_new = df_test_data[['Magnitude','Depth']]

    # Split our training data into training and testing data 
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # Create the random forest regressor model
    model_reg = RandomForestRegressor(random_state=50)
    # Train the model using  the training data 
    model_reg.fit(X_train,y_train)
    # Use The trained model to predict the training test data 
    model_reg.predict(X_test)
    print("3")
    # # improve the model accuracy by autonating hyperparameter tuning
    # Parameters = {'n_estimators':[10,20,50,100,200,500]}
    # # Create the gridsearchcv model 
    # grid_obj = GridSearchCV(model_reg,Parameters)
    # # train the model using the training data
    # grid_fit = grid_obj.fit(X_train, y_train)
    # # select the best fit model
    # best_fit = grid_fit.best_estimator_
    # #Use the best fit model to make the prediction on our training test data
    # results = best_fit.predict(X_test)
    # score = (best_fit.score(X_test,y_test)*100)+50
    # print(score)
    print("4")
    # Use the best fit model to make prediction on out out of sample test data (quakes for year 2017)
    final_results = model_reg.predict(X_new)
    # Evaluate the model accuracy
    final_score = model_reg.score(X_new,y_new)*100
    #Sotre  the prediction results into lsits
    lst_Magnitudes =  []
    lst_Depth =  []
    i=0

    # Loop through our predicted magnitude and depth values and then store them in our lists

    for r in final_results.tolist():
        lst_Magnitudes.append(final_results[i][0])
        lst_Depth.append(final_results[i][1])
        i+=1

    # create our predicted earthquakes dataframe
    print("5")
    df_results = X_new[['Latitude',"Longitude"]]
    df_results['Magnitude']=lst_Magnitudes
    df_results['Depth']=lst_Depth
    df_results['Score'] = final_score
    
    # Preview the prediction data set
    print(df_results.head())
    print("6")
    # Insert the  predicted dataset into the Quake_Predections model /table
    for index , row in df_results.iterrows():
        Latitude = row["Latitude"]
        Longitude = row["Longitude"]
        Magnitude = row["Magnitude"]
        Depth = row["Depth"]
        Score= row['Score']
 

        Quake_Predections( latitude=Latitude , longitude = Longitude  , Magnitude=Magnitude  ,Depth=Depth
        , Score=Score).save()


    




