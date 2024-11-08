import streamlit as st
import dd_info
import pandas as pd

def about_me_section():
    st.header("About Me")
    st.image(dd_info.profile_picture, width=200)
    st.write(dd_info.about_me)
    st.write("---")

about_me_section()

# Sidebar
def links_section():
    st.sidebar.header("Links")

    linkedin_link=f'<a href="{dd_info.my_linkedin_url}">Connect with me on LinkedIn</a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    linkedin_image = st.sidebar.image(dd_info.linkedin_image_url, width=64)

    github_link=f'<a href="{dd_info.my_github_url}">Find me on Github</a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    github_image = st.sidebar.image(dd_info.github_image_url, width=64)

    email_link=f'<a href="{dd_info.my_email_url}">Email</a>'
    st.sidebar.markdown(email_link, unsafe_allow_html=True)
    email_image = st.sidebar.image(dd_info.email_image_url, width=64)

links_section()

# Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f'**{education_data["Institution"]}**')
    st.write(f'**Degree:** {education_data["Degree"]}')
    st.write(f'**Concentration:** {education_data["Concentration"]}')
    st.write(f'**Graduation Date:** {education_data["Graduation Date"]}')

    st.subheader("Relevant Coursework")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "Skills"},
        hide_index=True,)

education_section(dd_info.education_data, dd_info.course_data)


#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
        
experience_section(dd_info.experience_data)


# Projects
def project_section(projects_data):
    st.header("Projects")
    for project_name, (projects_description, link) in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(projects_description)
        expander.link_button("🔗 Take me there", link)
    st.write("---")

project_section(dd_info.projects_data)

# Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f'{skill} {dd_info.programming_icons.get(skill)}')
        st.progress(percentage)
    
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f'{spoken} {dd_info.spoken_icons[spoken]} - {proficiency}')

skills_section(dd_info.programming_data, dd_info.spoken_data)


# Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    t1, t2 = st.tabs(["Leadership", "Community Service"])
    with t1:
        st.subheader("Leadership")
        for title, details in leadership_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
        
    with t2:
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    
    st.write("---")

activities_section(dd_info.leadership_data, dd_info.activity_data)