# Chicago Crimes Arrest prediction

## Project motivation:

I have chosen this topic because it requires working on a real-world dataset that is updated
regularly. The dataset available is not curated for a specific Machine Learning task and is sufficient to play with.

•	Chicago is one of the largest cities in the USA and has the highest crime rate increasing every year in every category of crime.

•       The goal of applying machine learning is to provide the Chicago Police Department with insights that will assist them prevent future crimes in that area.

## Questions I would like to address:

•	I would like to predict the likelihood of an arrest occurring in the city of Chicago.

•	By the use of this openly available data. I will try to find patterns in these criminal activities (patterns like: is one kind of crime more frequently than others? Is one area of Chicago more unsafe than the other? Etc.) And come up with models that will help us in predicting whether criminals were arrested or not.

## Dataset Source:

•	The dataset has been downloaded from the state government website
	https://data.cityofchicago.org/Public-Safety/Crimes-One-year-prior-to-present/x2n5-8w5q/data
	
•	I looked at crime data from the “Chicago Crime dataset report” which contains information on crimes committed in the city of Chicago.
	
•	Dataset has 213,627records and 17 columns

•	It has attributes like'CASE#', 'DATE  OF OCCURRENCE', 'BLOCK', ' IUCR', 'PrimaryDescription'     ' SECONDARY_DESCRIPTION', ' LOCATION_DESCRIPTION', 'ARREST', 'DOMESTIC',  'BEAT', 'WARD', 'FBI CD', 'X COORDINATE', 'Y COORDINATE', 'LATITUDE',  'LONGITUDE', 'LOCATION'

•	I would like to drop not so useful columns while performing exploratory data analysis and consider the subset of attributes useful for my analysis. As of now, I observe the location column to be a pair of latitude and longitude, so it can be dropped.
## Unit of Analysis:

My unit of analysis would be the crimes that took place in the city of chicago and each crime case reported would be an observation.
## Target variables and features:

For my analysis, I would like to consider the ARREST column as my target variable.'ARREST' is a categorical column.It has two different categories Y if the criminal was arrested and N if the criminal was not arrested.
## Models to be used:

I would like to use three machine learning models: logistic regression, decision tree classifier, and random forest classifier.
## Evaluation metric to be used:

I would like to compare the performance of my models using the f1_score metrics used when false negatives and false positives are equally important and have a greater impact. I would argue that in this case, both false positives and false negatives are worse. For example, if a crime company or the Chicago PD was to predict whether someone would get arrested or not, if an innocent gets arrested or criminal escapes from an arrest both the situations are highly risky.
## Outcomes:

With this project I expect to learn how to execute a machine learning project from beginning to end using a real-world dataset, feature engineering, working on different classification models and their evaluation using the F1 score metric.

