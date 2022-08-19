import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score, classification_report


file = open('to_show_df.pkl', 'rb')
all_toshow_df = pickle.load(file)
file.close()

st.set_page_config(layout="wide")

st.markdown("""
        <style>
            .stApp {
             background-image: url("https://safety4sea.com/wp-content/uploads/2019/11/medical-fraud.png");
             background-size: cover
                }

            .css-18e3th9 {
                padding-top: 0rem;
                padding-bottom: 10rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }

            .css-1d391kg {
                padding-top: 3.5rem;
                padding-right: 1rem;
                padding-bottom: 3.5rem;
                padding-left: 1rem;
            }

            .p
            {
                margin-bottom: 2px;
            }
            .p, ol, ul, dl {
                margin: 0px 0px 0.1rem;
            }
        </style>
        """, unsafe_allow_html=True)


st.title("HealthCare Fraud Detection")


selectbox = st.selectbox(
    "Select The Algorithm",
    ["Select Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "XG Boost", "Extra Tree", "Ada Boost"]
)


if selectbox != "Select Algorithm":
    # st.write(f"You selected the Algorithm: {selectbox}")

    accuracy = accuracy_score(all_toshow_df[selectbox]['Real'],all_toshow_df[selectbox]['Pred'])
    precision = precision_score(all_toshow_df[selectbox]['Real'],all_toshow_df[selectbox]['Pred'])
    recall = recall_score(all_toshow_df[selectbox]['Real'],all_toshow_df[selectbox]['Pred'])
    f1 = f1_score(all_toshow_df[selectbox]['Real'],all_toshow_df[selectbox]['Pred'])

    st.markdown(
        f"""<h5 style="text-weight:600;text-shadow: 1px 1px 1px 1px #FFF;">MODEL Accuracy: {accuracy*100} %<br>
    MODEL Recall Score: {recall}<br>
    MODEL Precision Score: {precision}<br>
    MODEL f1 Score: {f1}<h5>""", unsafe_allow_html=True
    )

    st.write("**Output DF for the Algorithm**")
    # st.write(all_toshow_df[selectbox][['Real', 'Pred']])
    st.write(all_toshow_df[selectbox])

    #Plot Graph
    metrics = ['Accuracy', 'Recall', 'Precision', 'F1 Score']
    values = [accuracy, recall, precision, f1]

    fig = plt.figure(figsize = (8,2))

    # creating the bar plot
    plt.bar(metrics, values)

    plt.xlabel("-- Metrics -->")
    plt.ylabel("-- Value -->")
    plt.title(f"Different Metrics of {selectbox} Model")

    st.pyplot(fig)
