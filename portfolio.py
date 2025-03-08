import streamlit as st
# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Define the navigation bar
st.sidebar.title("User Info Here 👤")
page = st.sidebar.radio("Go to", ["Home 🏠", "About ℹ️", "Contact 📞", "Aim 🎯"])

# Home Page
if page == "Home 🏠":
    st.title("Welcome to My Portfolio! 🚀")
    st.write("""
    Hello! I'm **Kamran Muntazar Abro**. I am a passionate developer who loves building amazing projects. 💻
    This is my portfolio where you can learn more about me, my skills, and how to get in touch with me. 🤝
    """)
    st.image("kamran.jpg", caption="That's Me! 😎", width=200)
    
   
# About Page
elif page == "About ℹ️":
    st.title("About Me 🧑‍💻")
    st.write("""
    I am a software developer experienced in various web technologies. 🌐
    I enjoy solving complex problems and building scalable applications. Thank you! 🙏
    """)
    st.subheader("Skills 🛠️")
    st.write("- Python 🐍")
    st.write("- JavaScript 📜")
    st.write("- Streamlit 🎈")
    st.write("- Data Analysis 📊")
    st.write("- Machine Learning 🤖")

# Contact Page
elif page == "Contact 📞":
    st.title("Contact Me 📨")
    st.write("""
    Feel free to reach out to me if you have any questions or if you'd like to collaborate on a project. 🤗
    I will be happy to work with you. Let's grow together! 🌱
    """)
    st.subheader("Contact Information 📇")
    st.write("📧 Email: kamranmuntazarabro@gmail.com")
    st.write("📞 Phone: +923235708382")
    st.write("📱 WhatsApp: +923444505301")
    st.write("🔗 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/example)")
    st.write("🐙 GitHub: [My GitHub Profile](https://github.com/example)")

# Aim Page
elif page == "Aim 🎯":
    st.title("My Aim 🌟")
    st.write("""
    My aim is to continuously improve my skills and contribute to meaningful projects that make a positive impact. 🌍
    I strive to learn new technologies and apply them to solve real-world problems. 💡
    """)
    st.write("""
    I am particularly interested in:
    - Web development 🌐
    - Riding 🏍️
    - Teaching programming 👨‍🏫
    - Artificial Intelligence 🤖
    - Data Science 📈
    - Open Source Contributions 👐
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2023 My Portfolio. All rights reserved. 🚀")