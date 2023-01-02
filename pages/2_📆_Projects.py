from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd


# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Portfolio CV | Vidhu Dhande"
PAGE_ICON = ":wave:"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#st.title("**RESUME**")
NAME = "PROJECTS"

resume_file = st.session_state['resume_file']
current_dir = st.session_state['current_dir'] 
profile_pic = st.session_state['profile_pic'] 
css_file = st.session_state['css_file'] 

Telecom_pic = st.session_state['Telecom_pic']
Bank_pic = st.session_state['Bank_pic']
EPD_pic = st.session_state['EPD_pic']

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(Bank_pic, "rb") as f:
    bankbyte = f.read()

with open(EPD_pic, "rb") as g:
    epdbyte = g.read()

with open(Telecom_pic, "rb") as h:
    wipbyte = h.read()

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

    
st.markdown("<span style='font-size: 1.5em; font-weight: bold; color: #0080FF;'>Discover Student Loans</span>", unsafe_allow_html=True,)
st.markdown("Lead Data Analyst")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(project_description_1)    

with col2:
    
    st.image(bankbyte, width=330)

st.write('\n')

project_description_2 = """
The Georgia Environmental Protection Division (EPD) is a state agency dedicated to protecting and restoring the environment. As part of this mission, the EPD has designed a project to create applications for the land, air and water department. These applications will be used to facilitate a range of activities, including the processing of water, air and land permit applications, the collection of fees, the performance of compliance investigations, the development of withdrawal permits, and the maintenance of permit files and databases. The EPD's efforts to modernize and streamline these processes will help the agency to more effectively carry out its important work of protecting and preserving Georgia's natural resources
"""

    
st.markdown("<span style='font-size: 1.5em; font-weight: bold; color: #0080FF;'>EPD IT</span>", unsafe_allow_html=True,)
st.markdown("Business Intelligence Analyst")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(project_description_2)    

with col2:

    st.image(epdbyte, width=330)

            

project_description_3 = """
NetAct is a comprehensive solution offered by Nokia Siemens Networks that helps mobile service providers to efficiently launch and manage mobile network services. It is designed to optimize the use of the mobile network while minimizing operational costs. NetAct covers the network management and service management layers within the TMN (Telecommunications Management Network) framework, and also functions as an Element Management System for certain vendors. With the ability to support multiple technologies (such as 2G BSS & NSS, Packet Core, and 3G RAN) and vendors, NetAct provides a range of functionality for the five key FCAPS (Fault, Configuration, Accounting, Performance, and Security) areas. Overall, NetAct is a valuable tool that enables mobile service providers to effectively manage and optimize their mobile networks
"""

    
st.markdown("<span style='font-size: 1.5em; font-weight: bold; color: #0080FF;'>NetAct App</span>", unsafe_allow_html=True,)
st.markdown("Sr.Software Engineer")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(project_description_3)    

with col2:

    st.image(wipbyte, width=350)

            
            

project_description_4 = """
The Nokia Siemens Networks (NSN) SGSN (Serving GPRS Support Node) is a key component that acts as a link between the packet core network and 2G General Packet Radio Service (GPRS) and 3G Universal Mobile Telecommunications System (UMTS) and Unlicensed Mobile Access (UMA) radio networks. In the 2G GPRS domain, the SGSN serves as a connection between the GSM, EDGE/GSM, or EGPRS-136 radio network and the packet core network, which is used to carry packet-based data traffic and provide access to external data networks. The project focuses on developing and enhancing the SGSN application, which consists of eight logical service blocks or modules that handle the complete 2G and 3G radio networks.
"""

    
st.markdown("<span style='font-size: 1.5em; font-weight: bold; color: #0080FF;'>NSN SGSN Packet Core</span>", unsafe_allow_html=True,)
st.markdown("Sr.Software Engineer")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(project_description_3)    

with col2:

    st.image(wipbyte, width=350)

#This is the end of the page here

            
  