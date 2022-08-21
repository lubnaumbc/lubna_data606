# Health Care Provider Fraud Detection
![Alt text](https://github.com/lubnaumbc/DATA602/blob/main/Project/image/chicagoskyline.PNG)

This project is dedicated to doing some cool data analysis, visualization,eda and modelling on the already curated dataset.
## Repo Contents
  <li><b>Data:</b>This folder  contains a data set from the Chicago Police department for crimes committed from Nov 7 2020 to Nov 6 2021                      https://github.com/lubnaumbc/DATA602/tree/main/Project/Data</li>
  <li><b>Visualization:</b>Data visualizations were created through the super awesome Python libraries matplotlib.
   I have performed many visualizations and saved the jupyter notebook
https://github.com/lubnaumbc/DATA602/blob/main/Project/Final_Project_Visualizations.ipynb
https://github.com/lubnaumbc/DATA602/blob/main/Project/Map_Visualizations_.ipynb</li>
  <li><b>Main Code Notebooks:</b>
https://github.com/lubnaumbc/DATA602/blob/main/Project/Lubna_Shereen_Data_602_Final_Project_Lubna_.ipynb
  
  In the below notebook cyclic representation of day,week and hour was used
https://github.com/lubnaumbc/DATA602/blob/main/Project/Extra__Lubna_Shereen_Data_602_Final_Project_Lubna_.ipynb</li>
  <li><b>Presentation:</b>
https://github.com/lubnaumbc/DATA602/blob/main/Project/602%20ppt%20-%20Copy.pptx</li>
  <li><b>Youtube Video:</b>
https://github.com/lubnaumbc/DATA602/blob/main/Project/602%20ppt%20-%20Copy.pptx</li>
<h1>Install</h1>
This project requires Python and the following Python libraries installed:

<li>NumPy</li>

<li>Pandas</li>

<li>matplotlib</li>

<li>scikit-learn</li>

We will also need to have software installed to run and execute a Jupyter Notebook.
If we do not have Python installed yet, it is highly recommended that we install the Anaconda distribution of Python, which already has the above packages and more included.
## PROJECT OVERVIEW:
<li>INTRODUCTION
<li>BUSINESS PROBLEM
<li>BUSINESS CONSTRAINTS
<li>DATASET
<li>MACHINE LEARNING MODELS USED
<li>METRICS USED
<li>MODEL RESULTS
<li>WEB APPLICATION
<li>FUTURE WORK
<li>REFERENCES

## INTRODUCTION:

Health care fraud is a white-collar crime that entails filing false medical claims to make money. It occurs when a person, such as a healthcare provider, gives misleading information or withholds information to benefit financially.
Fraud by Healthcare Providers include

•	submitting several claims for the same service in double billing

•	Phantom billing is when a patient is charged for services or materials they never received.

•	submitting numerous invoices for the same service (unbundling)

•	Upcoding is when a patient is billed for a more expensive service than they received.

Tens of billions of dollars are lost annually as a result for both businesses and individuals. It might lead to more expensive health insurance, the requirement for unnecessary medical procedures, and more outstanding taxes. According to the government, it is evident that the number of people and amount of loss has been increasing yearly over the years. The numbers haven't gone down all these years and are rising at a much higher rate in this modern world. It isn't easy to analyze all the submitted claims and act accordingly manually.

An insurance company is required by U.S. law to pay a valid medical claim within 30 days. Therefore, there is not much time to look at this thoroughly. Due to all this, the claims of genuine people are getting delayed and making the whole process even more complicated. So, my motto is to develop a model to detect potentially fraudulent claims.

## BUSINESS PROBLEM:
•	The institutions most at risk from these unethical practices are insurance companies. Health insurance is like a backbone for those living in a nation with numerous challenges and medical uncertainties. Governments and private insurance providers offer health insurance plans on some premiums that can be paid in installments to lessen the stress of paying astronomical medical expenditures. Fraud in claims, which results in significant losses for the insurance carriers, is one of the most critical issues facing the insurance sector.

•	 Statistics indicate that fraudulent claims account for 15% of all Medicare expenses. Due to this scam, government services like Medicare do not reach out to individuals who deserve them. 

•	 The government also loses money by paying phony claims made by doctors and other service providers.

•	 This project aims to "predict the potentially fraudulent providers" based on the submitted claims. I also developed a search-based application to provide a list of fake providers, eventually alerting users to these services.

## BUSINESS CONSTRAINTS:
1. Misclassification carries a hefty price tag. The insurer will suffer a significant financial loss if fraudulent providers are anticipated to be non-fraudulent, and the agency's reputation will suffer if genuine providers are predicted to be fraudulent. False Negative and False Positive should be as low as possible.

2. For valid claims, the insurer must reimburse the provider with the claim amount within 30 days. There are no such strict latency limits, but it shouldn't take more than a day because the agency may need to set up an investigation depending on the model's output.

3. Because the agency or insurer must defend the fraudulent behavior and may need to conduct a manual inquiry, model interpretability is crucial. It shouldn't be a prediction of the "black box" variety.
## DATASET:

The Dataset is given on Kaggle's website. Please find the link below:

https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis

There are four Datasets and below is a brief explanation of all of them:
1. Beneficiary Dataset: These details include the beneficiary's DOB, DOD, gender, race, and any
 The chronic illness they may have is their state and country of residence.
2. Inpatient Dataset: The claim information for the patients admitted to the hospital is included. Thus, it has three additional columns—dates of admission, release, and diagnosis group code.
3. Outpatient Dataset: It includes the claim information for patients who just paid visits to the hospital and were not admitted.
4. Target Dataset/provider dataset: It has provider IDs labeled as potential fraud or not.
## MACHINE LEARNING MODELS USED:
I have used the following models for my work:
1. LOGISTIC REGRESSION MODEL: predicts the likelihood of a categorical dependent variable using a machine learning classification technique. The dependent variable in logistic regression is a binary variable that only accepts data that is either coded as 1 (yes, success, etc.) or 0 (no) (no, failure, etc.). In other words, P(Y=1) is predicted as a function of X by the logistic regression model.
2. DECISION TREE MODEL: Decision Trees are a sort of supervised machine learning in which the training data is continually segmented based on a particular parameter, with you describing the input and the associated output. Decision nodes and leaves are the two components that can be used to explain the tree. The data is divided at the decision nodes. The leaves represent the choices or results.
3. RANDOM FOREST MODEL: Supervised machine learning algorithms like random forest are frequently employed in classification and regression issues. On various samples, it constructs decision trees and uses their average for classification and majority vote for regression.
4. XG BOOST: Based on decision trees, the ensemble machine learning algorithm XGBoost uses the gradient boosting framework. Artificial neural networks frequently perform better than other algorithms or frameworks in prediction problems involving unstructured data (pictures, text, etc.). But decision tree-based algorithms are now regarded as best-in-class for handling small- to medium-sized structured/tabular data.
This technique sequentially generates decision trees. In XGBoost, weights are significant. All independent variables are given weights, subsequently used to feed information into the decision tree that forecasts outcomes. After increasing the tree's weight incorrectly predicted variables, the second decision tree is then provided with these variables. These independent classifiers and predictors are combined to create a robust and accurate model. It can solve problems including regression, classification, ranking, and user-defined predictions.
5. EXTRA TREE CLASSIFIER: Extremely Randomized Trees Classifier, also known as Extra Trees Classifier, is a form of ensemble learning technique that combines the findings of various de-correlated decision trees in a "forest" to produce its classification outcome. The only way it differs conceptually from a Random Forest Classifier is in how the decision trees in the forest are built.
6. ADA BOOST CLASSIFIER: The Boosting technique known as AdaBoost algorithm, sometimes called Adaptive Boosting, is used as an Ensemble Method in machine learning. The weights are redistributed to each instance, with higher weights given to mistakenly categorized cases, hence the name "adaptive boosting." For supervised learning, boosting is used to lower bias and variation. It operates under the premise that students advance in stages. Each student after the first is developed from a prior learner, except for the first. Said, weak students are transformed into strong ones.
## METRICS USED: 
I have used the following metrics for my work:
1. F1_SCORE: The F1-score evaluates the precision of a model on a dataset. It is used to assess binary classification systems, which label examples as "positive" or "negative."
2. ROC AND AOC CURVE: The performance of a classification model at each classification threshold is depicted on a graph called a ROC curve (receiver operating characteristic curve). The area under the ROC Curve is referred to as AUC. This means that AUC evaluates the entire two-dimensional region beneath the complete ROC curve, from (0,0) to (1,1). (1,1). The performance across all potential classification criteria is measured overall by AUC.
3. PRECISION AND RECALL: Performance indicators for pattern recognition and classification in machine learning include precision and recall. While increasing recall will reduce the number of false negatives, increasing precision will reduce the number of false positives. Building a flawless machine learning model that produces more precise and accurate results requires understanding these ideas.
4. ACCURACY: Its accuracy metric often describes the model's performance across all classes. When every class is equally important, it is useful. It is determined by dividing the total number of guesses by the number of correct predictions.
## MODEL RESULTS:
  
From all the used machined learning models, the extra tree performed better among all the models, with an f1_score of 83.82 percent.

## WEB APPLICATION:
To make the customer aware of the fraudulent list, I have developed an application using StreamLit, which displays all the fraudulent upon search.
StreamLit: Data scientists can easily create interactive dashboards and machine learning web apps using the free, open-source, all-Python Streamlit framework, which doesn't require any prior front-end web programming knowledge. If you are familiar with Python, you are ready to utilize StreamLit to create and share your web apps, so don't wait weeks to get started
## FUTURE WORK:
I'll broaden my research and use deep learning to uncover fresh insights. I want to leverage dropouts and other activation methods, like Relu, to prevent overfitting. I have two choices for the top layer because this is a binary classification problem: sigmoid or softmax.
## REFERENCES:
1.	“Big Data fraud detection using multiple Medicare data sources”
 https://journalofbigdata.springeropen.com/articles/10.1186/s40537-018-0138-3#Tab1
2. “Predicting Healthcare Fraud in Medicaid: A Multidimensional Data Model and Analysis           Techniques for Fraud Detection."
https://www.sciencedirect.com/science/article/pii/S2212017313002946
3. "Medicare Fraud Detection Using Machine Learning Methods."
https://ieeexplore.ieee.org/abstract/document/8260744
4. “A Comprehensive Study of Healthcare Fraud Detection based on Machine Learning."
https://www.ripublication.com/ijaer18/ijaerv13n6_140.pdf
5. https://www.fbi.gov/scams-and-safety/common-scams-and-crimes/health-care-fraud
6. https://docs.streamlit.io/library/get-started/create-an-app


## PROJECT PPT LINK : 

## PRESENTATION RECORDING YOUTUBE LINK : https://www.youtube.com/watch?v=8m5B0tmLSTU
