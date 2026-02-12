import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="OHS Act 85 of 1993 Advanced Quiz", page_icon="⚖️")

# --- QUESTION DATABASE ---
# You can expand this list with more sections and regulations
quiz_data = [
    {
        "question": "Under Section 37(2), an employer is liable for the conduct of a mandatary unless which condition is met?",
        "options": [
            "The employer provides all tools and equipment.",
            "A written agreement is signed acknowledging the mandatary's duty to comply with the Act.",
            "The mandatary has their own Letter of Good Standing.",
            "The inspector grants a verbal exemption."
        ],
        "answer": "A written agreement is signed acknowledging the mandatary's duty to comply with the Act.",
        "reference": "Section 37(1) & (2): Acts or omissions by employees or mandataries."
    },
    {
        "question": "What is the legal threshold for the 'Reasonably Practicable' standard as defined in Section 1?",
        "options": [
            "Cost is never a factor in safety.",
            "Absolute safety must be guaranteed regardless of cost.",
            "A balance between the severity of the hazard and the cost/utility of the measures.",
            "Compliance with international ISO standards only."
        ],
        "answer": "A balance between the severity of the hazard and the cost/utility of the measures.",
        "reference": "Section 1: Definitions - 'Reasonably Practicable'."
    },
    {
        "question": "In terms of Section 17, at what employee count threshold must an employer appoint Health and Safety Representatives?",
        "options": [
            "More than 5 employees",
            "More than 10 employees",
            "More than 20 employees",
            "Only in high-risk factories"
        ],
        "answer": "More than 20 employees",
        "reference": "Section 17(1): Designation of health and safety representatives."
    }
]

# --- SESSION STATE INITIALIZATION ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False

# --- APP UI ---
st.title("⚖️ OHS Act 85 of 1993")
st.subheader("Advanced Certification Quiz")

if not st.session_state.quiz_complete:
    # Progress Bar
    progress = (st.session_state.current_question) / len(quiz_data)
    st.progress(progress)
    
    # Display Question
    q_index = st.session_state.current_question
    item = quiz_data[q_index]
    
    st.markdown(f"**Question {q_index + 1}:**")
    st.write(item["question"])
    
    # Selection
    user_choice = st.radio("Select the correct legal provision:", item["options"], key=f"q{q_index}")
    
    if st.button("Submit Answer"):
        if user_choice == item["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer was: {item['answer']}")
            st.info(f"**Legal Reference:** {item['reference']}")
        
        # Move to next or end
        if st.session_state.current_question < len(quiz_data) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.quiz_complete = True
            st.rerun()

else:
    # Final Score Screen
    st.balloons()
    st.header("Quiz Complete!")
    final_score = (st.session_state.score / len(quiz_data)) * 100
    st.metric("Final Score", f"{final_score}%")
    
    if final_score >= 80:
        st.success("Competency Demonstrated: You have a strong grasp of the OHS Act.")
    else:
        st.warning("Further study of the General Administrative Regulations is recommended.")
    
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()