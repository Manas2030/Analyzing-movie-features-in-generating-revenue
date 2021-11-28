# Analyzing the influence of different parameters over the revenue of a movie
by **Ananya Singh, Devika Mittal, Manas Gupta and Prashasti Agarwal** <br>
**Machine Learning (CSE343, ECE343)** at **Indraprastha Institute of Information Technology, Delhi**. 

## Introduction 
The aim of our project was to predict revenue of a movieand study how different parameters like genre, title, description  keywords,  run-time,  etc,  affect  its  success. Through several machine learning techniques, we have tried to verifyour preconceived notions about various factors which mightbe important in determining revenue. We have tried several hyperparameter tuned models to finally reach the one thatbest models our data in predicting revenues.

## Description and Implementation Details
We used Kaggle’s [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) for our analysis.This is a labelled dataset containing entries of about 45,000 movies listed at IMDB. We have used the following 3 of the 7 files in the dataset for our analysis:
- moviesmetadata:  contains 45,466 entries each containing  24  features  namely: adult,  belongstocollection, budget, genres, homepage, id, imdbid, originallanguage, originaltitle, overview, popularity, posterpath, productioncompanies, productioncountries,releasedate,revenue,runtime,spokenlanguages, status, tagline, title, video, voteaverage,votecount
- keywords: contains movie IDs and the keywords used todescribe their plot.
- credits: contains movie IDs with the cast as well as crew involved in the movie


## Running the models
Download the entire repository and extract all the files to a folder. 
Open a terminal in this folder and run the below command:
`python download.py`
This command would download a zip file to the data folder.
Then:
1. Run the file preprocessing.ipynb
     - This will extract the data from /data folder
     - It will extract all the required features from the datasets
     - It will generate and process the features
     - After all this processing preprocessed.csv is saved in /data folder and can be used for training and predictions.
2. Run the file visualisations.ipynb
     - This helps in plotting of various features against revenue
     - This helps in estimation of the data
     - It tells us the idstibution of data and determine which models might be useful.
3. Run the file all_models.ipynb 
     - This notebook has been documented and commented and runs each model one by one
     - After each training a prediction is made on the testing set
     - R2 Score, RMSE are printed
     - Scatter plots of true vs predicted value for training as well as testing set are made for predition visualisation. 
    
## Contact 
For any further queries feel free to reach out the following contributors. 

Ananya Singh (ananya19144@iiitd.ac.in) </br>
Devika Mittal (devika19463@iiitd.ac.in) </br> 
Manas Gupta (manas19368@iiitd.ac.in) </br>
Prashasti Agarwal (prashasti19075@iiitd.ac.in) </br>

## Final Report 
![Page 1](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_1.png)
![Page 2](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_2.png)
![Page 3](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_3.png)
![Page 4](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_4.png)
![Page 5](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_5.png)
![Page 6](https://github.com/Manas2030/Analyzing-movie-features-in-generating-revenue/blob/main/ML_Group_24_Final_Report/ML_Group_24_Final_Report_6.png)

