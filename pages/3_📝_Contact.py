import streamlit as st  

from pathlib import Path


# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Portfolio CV | Vidhu Dhande"
PAGE_ICON = ":wave:"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.header(":mailbox: Lets Connect!")


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "contact_page_style.css"


contact_form = """
<form action="https://formsubmit.co/vidhuwebpage@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="First Name" placeholder="First Name" required>
     <input type="text" name="Last Name" placeholder="Last Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <input type="text" name="Subject" placeholder="Subject" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(css_file)
