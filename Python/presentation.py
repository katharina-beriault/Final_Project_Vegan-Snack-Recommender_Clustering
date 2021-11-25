import streamlit as st
import pandas as pd
from PIL import Image

st.write("""# Vegan Snack Recommender""")

st.image("https://latestvegannews.com/wp-content/uploads/2019/07/91FFqqXvBhL._SL1500_.jpg")

st.markdown('#')
st.markdown('#')

st.write("### Hello snack fellow, let's check out what you might like...")

st.markdown('#')
st.markdown('#')

# Success button for food preferences
status = st.radio("Select food preferences: ", ('Vegan Snack Lover', 'Not a Vegan Snack Lover'))
 
if (status == 'Vegan Snack Lover'):
    st.success("Yay, let's start!")
else:
    st.error("Get ready to find your perfect vegan snack anyways!")

st.markdown('#')
st.markdown('#')
    
# Loading dataframe
df = pd.read_csv('df_clusters.csv')

# function for a random sample of products
def random_sample(df):

    cl_0 = df[df['cluster_2'] == 0].sample(1)
    cl_1 = df[df['cluster_2'] == 1].sample(1)
    cl_2 = df[df['cluster_2'] == 2].sample(1)
    cl_3 = df[df['cluster_2'] == 3].sample(1)

    new_df = pd.concat([cl_0, cl_1, cl_2, cl_3], axis=0)

    return new_df

# function to get photo link of products
def get_details(df, pos):

    new_df = random_sample(df)

    link = new_df['photo_link'].values[pos]
    name = new_df['product'].values[pos]

    return link, name

# getting details
cl_0 = get_details(df, 0)
cl_1 = get_details(df, 1)
cl_2 = get_details(df, 2)
cl_3 = get_details(df, 3)

# getting photo links
cl_0_link = cl_0[0]
cl_1_link = cl_1[0]
cl_2_link = cl_2[0]
cl_3_link = cl_3[0]

# getting products
cl_0_name = cl_0[1]
cl_1_name = cl_1[1]
cl_2_name = cl_2[1]
cl_3_name = cl_3[1]

    
# Create a button, that when clicked, shows a text
if(st.button("START")):
    st.markdown('##')
    st.text("Please select the snack that looks most tasty to you. If you don't like these snack options, just click start again.")
    st.text("If you don't like these snack options, just click start again.")

    # create grid for photos
    col1, col2 = st.columns(2)

    col1.header("Product no. 1")
    col1.write(cl_0_name)
    col1.image(cl_0_link)

    col2.header("Product no. 2")
    col2.write(cl_1_name)
    col2.image(cl_1_link)
    
    # create grid for photos
    col3, col4 = st.columns(2)
    
    col3.header("Product no. 3")
    col3.write(cl_2_name)
    col3.image(cl_2_link)

    col4.header("Product no. 4")
    col4.write(cl_3_name)
    col4.image(cl_3_link)
    
    
    st.markdown('##')

    
    option = st.selectbox("Select your favorite snack from this sample:", ('Choose a snack', cl_0_name, cl_1_name, cl_2_name, cl_3_name))
    
    
    if len(option) == 0 or option == 'Choose a snack':
        st.write("We can understand the decision is difficult :P")
    
    else:
        st.write('You selected:', option)