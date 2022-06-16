

## Introduction:

•	Health-care fraud is a sort of white-collar crime that involves filing false health-care claims in order to make money. Anyone, from healthcare funds to fund members like us, can be affected by healthcare fraud. It occurs when someone, such as a healthcare practitioner or an individual, offers inaccurate or incomplete information in order to gain a financial advantage.

•	The fraud can be committed in many ways; double billing, Up-coding, Phantom billing.

•	It is estimated by the National Health Care Anti-Fraud Association that there is a loss of around 68 billion dollars which accounts to 3 percent of nation’s spending in health care. 


## Questions I would like to address:

•	 Total money lost in fraud for both inpatient and outpatieint data

•	Using the claims filed by them, I would like to predict the likely fraudulent providers in healthcare 

•	I would like to find the key aspects that can assist in spotting possibly fraudulent suppliers' behavior
 


## Dataset Source:
Dataset downloaded from Kaggle. These files contain valid information about insurance scheme beneficiaries, patients who were admitted to the hospital and underwent some medical procedure and diagnosis (inpatient data), patients who visited the hospital for some procedure or diagnosis or both but were not admitted (outpatient data), and medical service provider IDs that have been tagged as potential fraud or not.

  ### 1.	Inpatient and outpatient data:
•	ClaimID: This is a one-of-a-kind identifier for each claim submitted.

•	Bene ID: holds the beneficiary's unique identifier for the insurance plan.

•	The id of the physicians who attended the patient is stored in the AttendingPhysician column.

•	The OperatingPhysician: column comprises the ids of the doctors who performed the surgery on the patient.

•	ClmDiagnosisCode: includes Diagnosis Codes for procedures that clinicians execute on patients.

•	ClmProcedureCode: includes codes for procedures that patients go through.

•	Provider: the healthcare providers' unique identifier.

•	Total amount given to the claimant following settlement (InscClaimAmtReimbursed).

•	ClaimStartDt / ClaimEndDt: These columns provide the dates on which claims were submitted and the dates on which claims were settled.

•	AdmissionDt / DischargeDt: The date the patient was admitted to the hospital and the date he or she was discharged.

  ### 2.	Beneficiaries data: 
•	Bene ID: This field holds the beneficiaries' unique identifiers for the insurance programme.

•	DOB: The date of birth of the beneficiaries who have enrolled in the insurance plan.

•	Gender: The gender of the beneficiaries who have signed up for the insurance plan.

•	State/Country: For registered members, this field contains the state/country code.

•	Pre-existing medical conditions: Some columns, such as RenalDiseaseIndicator, ChronicCond Depression, ChronicCond Diabetes, and others, are used to identify whether the individual has any prior medical illnesses.

  ### 3.	Target Data:
•	Service Provider ID: This is a unique identifier for each healthcare practitioner.

•	This column has two values: Yes and No, indicating whether the respective provider has been notified for suspected fraud.


## Models to be used:

I would like to use four machine learning models: logistic regression, decision tree classifier, and random forest classifier and XGBClassifier..
## Evaluation metric to be used:

Our dataset is unbalanced because most of the providers are not prospective fraudsters. Also, while flagging a supplier as a possible fraudster, we must be extremely cautious. The following measures can be used to assess model performance in this scenario:

•	Binary confusion matrix

•	Precision, recall, F1 score

## Outcomes:

With this project I expect to learn how to execute a machine learning project from beginning to end using a real-world problem, feature engineering, working on different classification models and their evaluation.
With this detection of frauds one can feel ease in getting the Medicare they need and lowering the insurance premiums helping every class of society.

