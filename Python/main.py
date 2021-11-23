import streamlit as st
import pandas as pd
from PIL import Image

st.write("""# Vegan Snack Recommender""")

st.image("https://latestvegannews.com/wp-content/uploads/2019/07/91FFqqXvBhL._SL1500_.jpg")

st.write("""Hello snack fellow, let's check out what you might like...""")

# Success button for food preferences
status = st.radio("Select food preferences: ", ('Vegan Snack Lover', 'Not a Vegan Snack Lover'))
 
if (status == 'Vegan Snack Lover'):
    st.success("Yay, let's start!")
else:
    st.error("Get ready to find your perfect vegan snack anyways!")
    

# Create a button, that when clicked, shows a text
if(st.button("START")):
    st.text("Please select the product you would like to snack right now.")


# Loading dataframe
df = pd.read_csv('df_clusters.csv')

# function for a random sample of products
def random_sample():
    
    cl_0 = df[df['cluster'] == 0].sample(1)
    cl_1 = df[df['cluster'] == 1].sample(1)
    cl_2 = df[df['cluster'] == 2].sample(1)
    cl_3 = df[df['cluster'] == 3].sample(1)
    cl_4 = df[df['cluster'] == 4].sample(1)
    cl_5 = df[df['cluster'] == 5].sample(1)
    cl_6 = df[df['cluster'] == 6].sample(1)
    cl_7 = df[df['cluster'] == 7].sample(1)
    cl_8 = df[df['cluster'] == 8].sample(1)
    cl_9 = df[df['cluster'] == 9].sample(1)
    
    
    new_df = pd.concat([cl_0, cl_1, cl_2, cl_3, cl_4, cl_5, cl_6, cl_7, cl_8, cl_9], axis=0)
    
    return new_df

new_df = random_sample()


    
st.write("Product Nr.1 :") # cluster 0
st.image('https://kokku-online.de//bilder/350x350/11921/plamil-dark-cocoa-bites-im-glas.auto', width = 400)

#st.dataframe(new_df)

#st.write("Product cluster 0:")
#st.image(new_df['photo_link'].values[0]), width = 400)