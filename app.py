import streamlit as st

# Title of the application
st.title("Deon Ethics Checklist for Data Science")

# Introduction
st.write("""
This checklist ensures that ethical considerations are addressed in data science projects.
Below is the detailed breakdown for this project.
""")

# Display the checklist
st.header("1. Data Collection and Consent")
st.write("""
- **Was informed consent obtained from individuals whose data is being used?**
  - The surveys were filled out by the data subjects with information on how it will be used. By taking the survey, the survey subject is consenting to the use of their data for the project design.
- **Are individuals aware of how their data will be used and the scope of data collection?**
  - The project outline is explained to the subject.
- **Is there an option for users to opt-out of data collection?**
  - Yes, they would not take the survey. When the model is in use, there could be a notification sent to the students and guardians about the potential use of the model to determine the risk level of the student.
""")

st.header("2. Privacy and Confidentiality")
st.write("""
- **Are measures in place to protect the privacy and confidentiality of individuals' data?**
  - The subjects are given anonymous identification numbers within the data, and no personal identifiers are shared.
- **Are there safeguards against unauthorized access or data breaches?**
  - The students are anonymized before their data enters the model system, ensuring their data remains secure even in the case of a breach.
""")

st.header("3. Transparency and Accountability")
st.write("""
- **Are the methods and purpose of the project transparent to stakeholders?**
  - The use and project outline are explained to users, along with a disclosure that the project should not be used in isolation.
- **Is there a clear accountability structure for ethical concerns?**
  - Ethical concerns are the responsibility of the school district and instructors using the project.
- **Can the results of the analysis be audited for ethical and methodological rigor?**
  - Yes, student performance before and after using the model can be monitored to ensure no negative impacts.
""")

st.header("4. Fairness and Non-discrimination")
st.write("""
- **Does the data or algorithm introduce any bias that could lead to discrimination?**
  - The dataset distribution reflects the school demographics and includes warnings for potential biases.
- **Are the outcomes fair and unbiased across different demographic groups?**
  - While the dataset is representative, any biases due to underrepresented groups should be monitored and addressed by users.
""")

st.header("5. Purpose and Justifiability")
st.write("""
- **Is the purpose of the data analysis justifiable, and does it align with ethical goals?**
  - Yes, the purpose is to help educators prioritize support for at-risk students.
- **Could this project cause harm or benefit society?**
  - The project benefits society by improving student retention, provided biases are accounted for and managed.
""")

st.header("6. Safety and Security")
st.write("""
- **Are measures in place to ensure the project does not put individuals or society at risk?**
  - The project avoids using personal identifiers and supports traditional instructor methods.
- **Are there clear steps for mitigating risks if they arise?**
  - Biases or risks should be investigated and corrected by retraining the model or updating data.
""")

st.header("7. Impact on Stakeholders")
st.write("""
- **Who could be impacted by the project, both positively and negatively?**
  - Instructors, students, their families, and the school district.
- **Are vulnerable populations considered in the project design and analysis?**
  - Efforts are made to include all demographics and flag potential underrepresentation.
""")
