from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd






#st.title("**RESUME**")
NAME = "PROJECTS"



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

Bank_pic = current_dir / "assets" /"bank.png"


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


with open(Bank_pic, "rb") as f:
    bankbyte = f.read()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:

    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.markdown(
    f"🟦 <span style='font-size: 2em; font-weight: bold'>{NAME}</span>",
    unsafe_allow_html=True,)

    #st.markdown(
    #f"<button style='background-color: blue; color: white; border: 2px solid black; font-size: 0.8em; padding: 0.5em 1em;' download='{resume_file.name}'>📄 Download Resume</button>",
    #unsafe_allow_html=True,)

# --- Project Summary 
st.write('\n')
st.write(
"Welcome to my projects page! On this page, you will find an overview of the projects I have worked on throughout my career, highlighting my skills and experience in data analytics, data management, and software engineering. Each of these projects showcases my ability to apply my expertise to a range of challenges and objectives, in different domains including financial services, environmental protection,and mobile network management.  \n My portfolio includes projects where I worked with Discover Student Loans to conduct regular reviews of production monitoring tools, maintaining/developing the tax (1098E, 1099Misc) calculator, helped the Georgia Environmental Protection Division (EPD) to modernize and streamline processes related to land, air, and water management, and supported mobile service providers with NetAct.  \n Throughout my career, I have consistently demonstrated strong problem-solving skills, a commitment to staying up to date with industry trends and best practices, and a track record of success in developing complex reports and dashboards using tools such as Tableau and Power BI.  \n I am confident that my portfolio will give you a sense of the range and depth of my skills and experience, and I look forward to discussing my work with you further.  \n" )

project_description_1 = """
At Discover Student Loans, we conduct regular reviews of our production monitoring tools to ensure their accuracy and timeliness. Our team utilizes analytical tools such as Tableau and Python to identify and resolve any discrepancies that may arise. Additionally, we have a dedicated Tax project that generates important documents such as 1098E, 1099, IPL, and other letters. Ensuring the accuracy of the data contained in these documents is of the utmost importance to us, and we use SAS to script an internal tax calculator to ensure their accuracy. We take pride in maintaining high standards of quality and reliability in our work, and strive to provide excellent service to our customers
"""

style = """
<style>
    .st-markdown {
        background-color: white;
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

    
st.markdown("<span style='font-size: 1.5em; font-weight: bold; color: #0080FF;'>Discover Student Loans</span>", unsafe_allow_html=True,)
st.markdown("Lead Data Analyst")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(project_description_1)    

with col2:
    
    st.image(bankbyte, width=330)

