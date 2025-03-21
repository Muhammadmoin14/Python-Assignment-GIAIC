import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title="Data Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Data Analysis With Graphs")
st.write("Upload your data file to analyze the data and get insights")
uploaded_file = st.file_uploader("Choose a file",type=['csv','xlsx'],accept_multiple_files=True)


# if uploaded_file is not None:
#     # Load data
#     if uploaded_file.name.endswith('.csv'):
#         df = pd.read_csv(uploaded_file)
#     else:
#         df = pd.read_excel(uploaded_file)
# else:
dataset_option = ["iris",'titanic','daimond']
selected_dataset = st.selectbox('Select a dataset:',dataset_option)
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
else:
    df = sns.load_dataset('diamonds')

st.write(df)

x_axis = st.radio('Select X-Axis for plot:',df.columns)
y_axis = st.radio('Select Y-Axis for plot:',df.columns)
Selected_Graph = st.selectbox('Select the type of plot you want to plot',['line','bar','scatter','countplot','piechart'])

# Plot the data

if Selected_Graph == 'line':
    st.line_chart(df[[x_axis,y_axis]])
elif Selected_Graph == 'bar':
    st.bar_chart(df[[x_axis,y_axis]])
elif Selected_Graph == 'scatter':
    st.scatter_chart(df[[x_axis,y_axis]])
elif Selected_Graph == 'countplot':
    st.bar_chart(df.value_counts())
else:
    st.pie_chart(df)




