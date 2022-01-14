from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import numpy as np
import matplotlib.pyplot as plt


#_content = 'NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,FIRMPDEMP'
_key = '16effcabd5d51ae74821b3639db3844d8c7f1beb'
_area = 'us' # 'us'
_url = f'https://api.census.gov/data/2018/abscs?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,VET_GROUP,VET_GROUP_LABEL,EMPSZFI,EMPSZFI_LABEL,YEAR,FIRMPDEMP,FIRMPDEMP_F,RCPPDEMP,RCPPDEMP_F,EMP,EMP_F,PAYANN,PAYANN_F,FIRMPDEMP_S,FIRMPDEMP_S_F,RCPPDEMP_S,RCPPDEMP_S_F,EMP_S,EMP_S_F,PAYANN_S,PAYANN_S_F&for={_area}:*&key={_key}'

_columns = ['GEO_ID','NAME','NAICS2017','NAICS2017_LABEL','SEX','SEX_LABEL','ETH_GROUP','ETH_GROUP_LABEL','RACE_GROUP','RACE_GROUP_LABEL','VET_GROUP','VET_GROUP_LABEL','EMPSZFI','EMPSZFI_LABEL','YEAR','FIRMPDEMP','FIRMPDEMP_F','RCPPDEMP','RCPPDEMP_F','EMP','EMP_F','PAYANN','PAYANN_F','FIRMPDEMP_S','FIRMPDEMP_S_F','RCPPDEMP_S','RCPPDEMP_S_F','EMP_S','EMP_S_F','PAYANN_S','PAYANN_S_F']

#_get = f'?get={_content}&for=us:*&NAICS2017=00&key={_key}'
r = requests.get(_url).json()

filename = 'census_data_2018.json'
with open(filename,'wt') as census:
    json.dump(r, census)

# Creates dataframe from json file
census_df = pd.read_json(filename)

# Renames the headers
census_df.rename(columns=census_df.iloc[0],inplace=True)
census_df.drop(0,inplace=True)

# drop unnecessary columns
census_df_dropped = census_df.drop(columns=['us','NAICS2017','SEX','GEO_ID','ETH_GROUP','RACE_GROUP','EMP_F','FIRMPDEMP_F','VET_GROUP','EMP_S','FIRMPDEMP_S','FIRMPDEMP_S_F','PAYANN_S','RCPPDEMP_S','RCPPDEMP_F','RCPPDEMP_S_F','EMP_S_F','PAYANN_S_F','PAYANN_F'],axis=1)



# What do we want to compare?
# Age, sex, geolocation, race, ethnicity, payann, vet_group, 
# Link to documentation on variable/column naming info: https://www2.census.gov/programs-surveys/abs/technical-documentation/api/API2019-company-summary-1-26-2021.pdf

# Ray
# Age -> geo location * 
# Age -> ethnicity
# Age -> payann

# Hang
# EMP -> age
# EMP -> gender
# EMP -> ethnicity

# Ted
# geolocation -> rcppdemp * Top 5 and bottom 5 for summed state sales
# geolocation -> race
# geolocation -> vet_group


# Dalton
# Race -> rcppdemp
# Race -> payann
# Race -> emp

#plotEMP()
#race_emps = race_emps[(race_emps['RACE_GROUP_LABEL'] != 'Classifiable') & (race_emps['RACE_GROUP_LABEL'] != 'Unclassifiable') & (race_emps['RACE_GROUP_LABEL'] != 'Nonminority') & (race_emps['RACE_GROUP_LABEL'] != 'Minority') & (race_emps['RACE_GROUP_LABEL'] != 'Equally minority/nonminority')]