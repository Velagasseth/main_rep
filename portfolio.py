import streamlit as st
import os
col1, col2=st.columns(2)
with col1:
    st.subheader("Welcome to My :red[Data Science Portfolio]👋")
    st.write("""
              Hello and thank you for visiting my portfolio! I am :blue[SETH ODERO], 
               a passionate data scientist student with a keen interest in transforming data into actionable insights.
              """)
with col2:
    image=st.image(os.path.join(os.getcwd(), "static", "profile.png"))
st.markdown(">With a background in :blue[Bsc.Applied Computer Science] , I have honed my skills in :blue[data analysis, machine learning , and data visualization ]"
                 )
st.write("Throughout my studies, I have had the opportunity to work on diverse projects that range from predictive analytic to natural language processing, my goal is to leverage data to solve complex problems and help organization make informed decision")
st.markdown(">A highly motivated and detail-oriented :blue[machine learning student at Kisii University with strong skills in data manipulation, data visualization, and web scraping]. Seeking an internship or entry-level position to apply my knowledge and skills in a practical environment.")