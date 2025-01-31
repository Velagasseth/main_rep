import streamlit as st
project1_page=st.Page (
    page="portfolio.py",
    title="About",
    icon="🏠"
)

project2_page=st.Page(
        page="2_Resume.py",
        title="Resume",
        icon="📄"
)

project3_page=st.Page(
        page="4_Work samples.py",
        title="Work samples",
        icon="⚒️"
)
project4_page=st.Page(
        page="5_Contact.py",
        title="Contact me",
        icon="☎️"
)



pg=st.navigation(
    {
        "Home":[project1_page],
        "Info":[project2_page,project4_page],
        "Projects":[project3_page]
    }
)
pg.run()