
from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
import base64



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Vidyanand Dhande_CV_Online.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
linkedin_pic = current_dir / "assets" / "linkedin_icon.png"
github_pic = current_dir / "assets" / "github_icon.png"
IG_pic = current_dir / "assets" / "IG_icon.png"
Telecom_pic = current_dir / "assets" /"Telecom.jpg"
Bank_pic = current_dir / "assets" /"bank.png"
EPD_pic = current_dir / "assets" /"EPD.jpg"


# Read the image file and convert it to a data URI
with open(linkedin_pic, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()

# Read the image file and convert it to a data URI
with open(github_pic, "rb") as image_file:
    image_data2 = base64.b64encode(image_file.read()).decode()

# Read the image file and convert it to a data URI
with open(IG_pic, "rb") as image_file:
    image_data3 = base64.b64encode(image_file.read()).decode()



st.session_state['resume_file'] = resume_file
st.session_state['current_dir'] = current_dir
st.session_state['css_file'] = css_file
st.session_state['Telecom_pic'] = Telecom_pic
st.session_state['Bank_pic'] = Bank_pic
st.session_state['EPD_pic'] = EPD_pic



# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Portfolio CV | Vidhu Dhande"
PAGE_ICON = ":wave:"
NAME = "Vidyanand Dhande"
DESCRIPTION = """
Lead Data Analyst/MBA. 
I'm a data analyst by trade, but really I'm just a numbers nerd at heart. 
Analyzing data is my passion,and I love using it to help organizations make informed decisions and achieve their goals.
"""
EMAIL = "vidyananddhande@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vidyanand-dhande-1ba02410/",
    "GitHub": "https://github.com/vidhu484",
    "Instagram": "https://www.instagram.com/vidhu_dhande/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

st.session_state['profile_pic'] = profile_pic


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    #st.title(NAME)
    st.markdown(
    f"🟦 <span style='font-size: 2em; font-weight: bold'>{NAME}</span>",
    unsafe_allow_html=True,)
    st.write(DESCRIPTION)
        
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
             
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))
#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #cols[index].write(f"[{platform}]({link})")

# --- SOCIAL LINKS ---
st.write('\n')

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if platform == "LinkedIn":
        #icon_src = "https://icon-library.com/images/linkedin-icon-png/linkedin-icon-png-23.jpg"
        icon_src = f"data:image/png;base64,{image_data}"
    elif platform == "GitHub":
        icon_src = "https://icon-library.com/images/github-icon-png/github-icon-png-27.jpg"
         #icon_src = f"data:image/png;base64,{image_data2}" 
    elif platform == "Instagram":
        #icon_src = "https://icon-library.com/images/instagram-icon-png/instagram-icon-png-26.jpg"
        icon_src =  icon_src = f"data:image/png;base64,{image_data3}" 
    #cols[index].markdown(f"<a href='{link}'><img src='{icon_src}' style='height: 1.5em; display: inline-block;'></a>", unsafe_allow_html=True,)
    cols[index].markdown(f"<a href='{link}'><img src='{icon_src}' style='height: 35px; width: 35px;'></a>", unsafe_allow_html=True,)



st.write('\n')

# --- About ME ---
st.write('\n')
st.subheader("About Me")
st.write(
    """
- ✔️ Highly skilled data professional with over eleven years of experience in data analytics, data management, and software engineering. 
- ✔️ Proficient in a range of technologies including Python, SQL, SAS & Shell, with expertise in data modeling, data warehousing, and business intelligence tools such as SSIS, SSRS, and SSAS. 
- ✔️ Strong problem-solving skills and a track record of success in developing complex reports and dashboards using Tableau and Power BI to drive business growth and success. 
- ✔️ Committed to staying up to date with the latest industry trends and best practices, and eager to take on new challenges and drive continuous improvement.
"""
)

