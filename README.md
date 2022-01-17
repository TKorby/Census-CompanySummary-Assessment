# Census-CompanySummary-Assessment
## Introduction
This project's focus covers data retrieval from a secured API, data cleaning and transformation as wellas creating useful visuals via Python based visual libraries such as matplotlib and pandas.
In the project, we analysed the United States Census Bureau's Census API in which we pulled data pertaining to the Annual Business Survey. We covered a few direct areas related to the demographics of the survey as well as varying bussiness qualities recorded.

## Process / Run Instructions
You will need to create a config.py file that has a dictionary with the "key" set to "API_key_string". The "API_key_string" will require you to sign up for the census API at this address: https://api.census.gov/data/key_signup.html. Once signed up, you will have to validate your account via an e-mail sent to the address you used to request your personal "API_key_string".

Example:
  File: config.py
    API_key_string = '9s821j20cjc0202l11ms0129'  # Key should be around 40 characters long
    
Localize the config.py file with the Jupyter notebook provided and you should now be able to run the first cell to collect the data required to transform and visualize.

