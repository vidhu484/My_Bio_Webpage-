from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd

# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Portfolio CV | Vidhu Dhande"
PAGE_ICON = ":wave:"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


NAME = "Resume"

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
parent_dir = current_dir.parent

resume_file = parent_dir / "assets" / "Vidyanand Dhande_CV_Online.pdf"
profile_pic = parent_dir / "assets" / "profile-pic.png"
css_file = parent_dir / "styles" / "main.css"

#resume_file = st.session_state['resume_file']
#current_dir = st.session_state['current_dir'] 
#profile_pic = st.session_state['profile_pic'] 
#css_file = st.session_state['css_file'] 

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Profile Image SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.markdown(
    f"🟦 <span style='font-size: 2em; font-weight: bold'>{NAME}</span>",
    unsafe_allow_html=True,)

    #st.markdown(
    #f"<button style='background-color: blue; color: white; border: 2px solid black; font-size: 0.8em; padding: 0.5em 1em;' download='{resume_file.name}'>📄 Download Resume</button>",
    #unsafe_allow_html=True,)

        
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",           
    )

    


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, NumPy, Streamlit, Pandas), SQL, Shell, Unix
- 📊 Data Visulization: Tableau, PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, Decision Trees, ARIMA, Facebook Prophet
- 🗄️ Databases: MySQL, MSSQL SERVER, Oracle, Snowflake, Teradata
"""
)

# --- Education --- 

st.write('\n')
st.subheader("Education")
st.write("---")
# --- Masters 
st.write("🏫", "**Master of Business Administration**")
st.write("Illinois State University, Normal, IL (United States)")
st.write("Aug 2012 - May 2015")
st.write('\n')

# --- Bachelors 

st.write("🏫", "**Bachelor of Technology in Electronics and Communication Jawaharlal Nehru Technological University**")
st.write("Sep 2003 - May 2007")
st.write("Jawaharlal Nehru Technological University, Hyderabad (India)")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Lead Data Analyst | Discover Bank, Full Time**")
st.write("Location: Atlanta, GA, USA")
st.write("Jul 2021 - Present")
st.write(
    """
- ► Utilized SQL, SAS, and Python to analyze and transform large datasets of Student Loans, resulting in improved accuracy in capturing any exceptions on the accounts and resulting in a 95% decrease in false positives.
- ► Utilized Airﬂow to automate the SQL and Python scripts and schedule data pipelines, resulting in a 50% reduction in manual work and a 15% increase in data processing eﬃciency.
- ► Conducted a comprehensive analysis of student loan data using statistical methods such as Linear regression analysis using Python packages (pandas, NumPy, Sklearn), resulting in the development of recommendations to optimize repayment plans and reduce default rates.
- ► Performed A/B testing to optimize the design and messaging of student loan repayment communications, resulting in a 25% increase in response rates.
- ► Implemented an ARIMA model to forecast interest rates for deposit accounts, resulting in improved decision-making and risk management for the Discover deposits.
- ► Created interactive dashboards using Tableau, Python Tkinter, and Dash libraries to visualize and communicate key insights to stakeholders.
- ► Mentored junior data analysts and provided technical guidance as needed.
"""
)

# --- JOB 2
st.write("🚧", "**Business Intelligence Analyst | RapidIT Inc, Full Time**")
st.write("Location: Atlanta, GA, USA")
st.write("Feb 2019 - Jul 2021")
st.write(
    """
- ► Developed and maintained ETL pipelines using Python and SQL to transform and clean data from disparate sources and load it into a data lake for analysis.
- ► Implemented ETL processes to extract data from CRM and ﬁnancial systems, apply business rules and transformations, and load the data into a reporting database for use in business intelligence dashboards using Power BI
- ► Developed a Python Dash web-based application for the project to capture the data for the field engineers. 
- ► Wrote complex T-SQL queries to extract and manipulate data from multiple sources, including the use of advanced techniques such as subqueries, stored procedures, window functions, and dynamic SQL for critical KPIs and cohort analysis. 
"""
)

# --- JOB 3
st.write("🚧", "**Business Intelligence Analyst | Anchor Infotech**")
st.write("Location: Atlanta, GA, Oakland,CA, USA")
st.write("Jun 2015 - Feb 2019")
st.write(
    """
- ► Migrated from Sybase to SQL Server 2014 using the SSMA tool and demonstrated expertise in identifying and troubleshooting issues and documenting root cause analysis.
- ► Conducted database management, performance measurement, and performance tuning using tools like SQL Proﬁler, Data Engine Tuning Advisor, and index tuning wizard.
- ► Utilized SSIS to design and implement ETL processes to extract data from various sources, transform the data, and load it into a data warehouse. Created SSIS packages to extract data from flat files, databases, and APIs, and used transformations such as data cleansing, data merging, and data aggregation to prepare the data for analysis and reporting. In addition, used Power BI OLAP cubes to efficiently store and query data. 
- ► Created and modiﬁed interactive dashboards and 30+ visualizations by identifying leading and lagging metrics and key KPIs for the project using Power BI. 
- ► Developed tabular reports using SSAS, and SSRS, including drill-down, drill-through, and parameterized reports, and deployed and subscribed to reports to generate daily, weekly, and monthly reports.
"""
)

# --- JOB 4
st.write("🚧", "**Graduate Research Assistant | Illinois State University**")
st.write("Location: Normal,IL, USA")
st.write("Aug 2012 - May 2015")
st.write(
    """
- ► Assisted MBA faculty with research and literature searches.
- ► Conducted database management, performance measurement, and performance tuning using tools like SQL Proﬁler, Data Engine Tuning Advisor, and index tuning wizard.
- ► Hands-on experience with data analysis using models such as linear regression, Anova/Ancova, time series, decision tree, and simulation-based analysis using SPSS and statistical software tools like MiniTab v.16.
"""
)

# --- JOB 5
st.write("🚧", "**External Consultant | Wipro Limited, Full Time**")
st.write("Location: Espoo,Finland")
st.write("May 2010 - Apr 2011")
st.write(
    """
- ► Coordinated tasks with oﬀshore development center and elicited requirements from stakeholders, analyzed processes, documented requirements using UML and Visio, migrated application design documents, monitored performance metrics, facilitated Joint Requirement Planning and Joint Application Development sessions, supported system performance and RF engineers, and assisted with change and defect management and user acceptance testing.
"""
)

# --- JOB 6
st.write("🚧", "**Sr. Software Engineer | Wipro Limited, Full Time**")
st.write("Location: Hyderabad, Telangana,India")
st.write("Jun 2007  - May 2010")
st.write(
    """
- ► Designed and developed software solutions for various internal and external clients using T-SQL, Shell, Perl, and C++.
- ► Implemented data transformation and cleansing logic using SSIS expressions, variables, and tasks, and utilized SSIS debugging and error handling capabilities to troubleshoot and resolve issues.
- ► Implemented unit tests and automated testing frameworks to ensure the quality of the codebase.
- ►	Participated in daily stand-up meetings, sprint planning, and retrospectives using agile development methodologies.
- ►	Provided prompt solutions and proactive troubleshooting on applications to resolve subtle and complex issues, achieving 95% customer satisfaction rate. 
"""
)

# --- HONORS AND AWARDS ---
st.write('\n')
st.subheader("HONORS AND AWARDS")
st.write("---")

# --- Accomplishment 1
st.write("🏆", "**Consumer Banking Excellence Award 2022**")

st.write("Discover Bank | Aug 2022")


# --- Accomplishment 2
st.write('\n')
st.write("🏆", "**Microsoft Certiﬁed in “Azure Fundamentals**")
st.write("Microsoft | Sep 2020")



# --- Accomplishment 3
st.write('\n')
st.write("🏆", "**MCSE: Data Management and Analytics**")
st.markdown("Microsoft Certification ID: 14953374 | Aug 2018")
st.write(
    """
- ► Microsoft Certified in “Designing Business Intelligence Solutions with Microsoft SQL Server 2016”
- ► Microsoft Certified in “Querying Data with Transact-SQL with Microsoft SQL Server 2016”
- ► Microsoft Certified in “Developing SQL Databases”

"""
)


