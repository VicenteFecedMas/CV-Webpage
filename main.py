from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
#profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Vicente Feced Mas"
NAME = "Vicente Feced Mas"
DESCRIPTION = """
AI engineer | Machine Learning engineer
"""
SOCIALS = [
    ("https://www.linkedin.com/in/vicente-feced-1a1794174/", "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTIgMmM1LjUxNCAwIDEwIDQuNDg2IDEwIDEwcy00LjQ4NiAxMC0xMCAxMC0xMC00LjQ4Ni0xMC0xMCA0LjQ4Ni0xMCAxMC0xMHptMC0yYy02LjYyNyAwLTEyIDUuMzczLTEyIDEyczUuMzczIDEyIDEyIDEyIDEyLTUuMzczIDEyLTEyLTUuMzczLTEyLTEyLTEyem0tMiA4YzAgLjU1Ny0uNDQ3IDEuMDA4LTEgMS4wMDhzLTEtLjQ1LTEtMS4wMDhjMC0uNTU3LjQ0Ny0xLjAwOCAxLTEuMDA4czEgLjQ1MiAxIDEuMDA4em0wIDJoLTJ2Nmgydi02em0zIDBoLTJ2Nmgydi0yLjg2MWMwLTEuNzIyIDIuMDAyLTEuODgxIDIuMDAyIDB2Mi44NjFoMS45OTh2LTMuMzU5YzAtMy4yODQtMy4xMjgtMy4xNjQtNC0xLjU0OHYtMS4wOTN6Ii8+PC9zdmc+"),
    ("https://github.com/VicenteFecedMas", "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTIgMmM1LjUxNCAwIDEwIDQuNDg2IDEwIDEwcy00LjQ4NiAxMC0xMCAxMC0xMC00LjQ4Ni0xMC0xMCA0LjQ4Ni0xMCAxMC0xMHptMC0yYy02LjYyNyAwLTEyIDUuMzczLTEyIDEyczUuMzczIDEyIDEyIDEyIDEyLTUuMzczIDEyLTEyLTUuMzczLTEyLTEyLTEyem0wIDZjLTMuMzEzIDAtNiAyLjY4Ni02IDYgMCAyLjY1MSAxLjcxOSA0LjkgNC4xMDQgNS42OTMuMy4wNTYuMzk2LS4xMy4zOTYtLjI4OXYtMS4xMTdjLTEuNjY5LjM2My0yLjAxNy0uNzA3LTIuMDE3LS43MDctLjI3Mi0uNjkzLS42NjYtLjg3OC0uNjY2LS44NzgtLjU0NC0uMzczLjA0MS0uMzY1LjA0MS0uMzY1LjYwMy4wNDIuOTIuNjE5LjkyLjYxOS41MzUuOTE3IDEuNDAzLjY1MiAxLjc0Ni40OTkuMDU0LS4zODguMjA5LS42NTIuMzgxLS44MDItMS4zMzMtLjE1Mi0yLjczMy0uNjY3LTIuNzMzLTIuOTY1IDAtLjY1NS4yMzQtMS4xOS42MTgtMS42MS0uMDYyLS4xNTMtLjI2OC0uNzY0LjA1OC0xLjU5IDAgMCAuNTA0LS4xNjEgMS42NS42MTUuNDc5LS4xMzMuOTkyLS4xOTkgMS41MDItLjIwMi41MS4wMDIgMS4wMjMuMDY5IDEuNTAzLjIwMiAxLjE0Ni0uNzc2IDEuNjQ4LS42MTUgMS42NDgtLjYxNS4zMjcuODI2LjEyMSAxLjQzNy4wNiAxLjU4OC4zODUuNDIuNjE3Ljk1NS42MTcgMS42MSAwIDIuMzA1LTEuNDA0IDIuODEyLTIuNzQgMi45Ni4yMTYuMTg2LjQxMi41NTEuNDEyIDEuMTExdjEuNjQ2YzAgLjE2LjA5Ni4zNDcuNC4yODggMi4zODMtLjc5MyA0LjEtMy4wNDEgNC4xLTUuNjkxIDAtMy4zMTQtMi42ODctNi02LTZ6Ii8+PC9zdmc+"),
]
PROJECTS = {

}

JOBS = {
    "job_1": {
        "title": "Artificial Intelligence engineer",
        "start_date": "03/2023",
        "end_date": "Present",
        "description": """
- Description 1
""",
    },

}


def add_job(job):

    st.write('\n')
    st.write(f"**{job['title']}**")
    st.write(f"{job['start_date']} - {job['end_date']}")
    st.write(job['description'])

st.set_page_config(page_title=PAGE_TITLE)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --- HERO SECTION ---
st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)
st.write(f"[![Title]({SOCIALS[0][0]})](www.google.com)")
for i, col in enumerate(st.columns(len(SOCIALS))):
    with col:
        st.write(f"[![]({SOCIALS[i][1]})]({SOCIALS[i][0]})")

# --- WORK HISTORY ---
for key in JOBS.keys():
    add_job(JOBS[key])

# --- SOCIAL LINKS ---

# --- EXPERIENCE & QUALIFICATIONS ---

# --- SKILLS ---

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")