import streamlit as st
import random
import pandas as pd
from questions import QUIZ_DATA
from fpdf import FPDF

# --- CERTIFICATE GENERATOR ---
def create_certificate(name, score):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_line_width(2)
    pdf.rect(10, 10, 277, 190)
    pdf.set_font("Arial", "B", 35)
    pdf.cell(0, 50, "CERTIFICATE OF COMPETENCY", ln=True, align="C")
    pdf.set_font("Arial", "", 20)
    pdf.cell(0, 15, "This is to certify that", ln=True, align="C")
    pdf.set_font("Arial", "B", 30)
    pdf.cell(0, 25, name.upper(), ln=True, align="C")
    pdf.set_font("Arial", "", 18)
    pdf.cell(0, 15, "has successfully passed the Advanced Assessment for:", ln=True, align="C")
    pdf.set_font("Arial", "B", 22)
    pdf.cell(0, 15, "OHS ACT 85 OF 1993 & REGULATIONS", ln=True, align="C")
    pdf.set_font("Arial", "I", 16)
    pdf.cell(0, 25, f"Final Score: {score:.0f}%", ln=True, align="C")
    return pdf.output()

# --- INITIALIZATION ---
if 'quiz_state' not in st.session_state:
    st.session_state.quiz_state = 'intro'
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.report_data = []
    st.session_state.shuffled_qs = []

def main():
    st.set_page_config(page_title="OHS Master Class", layout="centered")

    if st.session_state.quiz_state == 'intro':
        st.title("⚖️ Introduction to OHS ACT 85 of 1993")
        st.write("Welcome to the Advanced OHS Act Competency Platform.")
        st.markdown("""
        **About this Assessment:**
        * Covers OHS Act 85 of 1993 and applicable Regulations.
        * Questions are shuffled for every attempt.
        * Pass rate: **85% to 100%** for Certification.
        * A full **Learning Report** is available at the end.
        """)
        if st.button("Start Assessment"):
            st.session_state.shuffled_qs = random.sample(QUIZ_DATA, len(QUIZ_DATA))
            st.session_state.quiz_state = 'quiz'
            st.rerun()

    elif st.session_state.quiz_state == 'quiz':
        q_idx = st.session_state.current_q
        q_list = st.session_state.shuffled_qs
        q = q_list[q_idx]

        st.subheader(f"Question {q_idx + 1} of {len(q_list)}")
        st.progress(q_idx / len(q_list))
        st.info(q["question"])
        
        choice = st.radio("Select the correct provision:", q["options"], key=f"q_{q_idx}")

        if st.button("Submit Answer"):
            is_correct = (choice == q["answer"])
            if is_correct: st.session_state.score += 1
            
            st.session_state.report_data.append({
                "Question": q["question"],
                "Your Answer": choice,
                "Correct Answer": q["answer"],
                "Result": "✅" if is_correct else "❌",
                "Legal Explanation": q["explanation"]
            })
            
            if q_idx < len(q_list) - 1:
                st.session_state.current_q += 1
            else:
                st.session_state.quiz_state = 'results'
            st.rerun()

    elif st.session_state.quiz_state == 'results':
        st.header("🏁 Assessment Summary")
        score_pct = (st.session_state.score / len(st.session_state.shuffled_qs)) * 100
        st.metric("Final Grade", f"{score_pct:.0f}%")

        col1, col2 = st.columns(2)
        
        with col1:
            df = pd.DataFrame(st.session_state.report_data)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📊 Download Learning Report", csv, "OHS_Learning_Report.csv", "text/csv")

        with col2:
            contact_email = "neva.basson@liebengroup.co.za"
            subject = "OHS Quiz Inquiry"
            body = f"Hello Safety Officer, I have a question regarding my score of {score_pct:.0f}%."
            mail_link = f"mailto:{contact_email}?subject={subject}&body={body}"
            st.markdown(f'<a href="{mail_link}" target="_blank" style="text-decoration: none;"><button style="border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; background-color: #008CBA; border-radius: 8px;">📧 Contact Safety Officer</button></a>', unsafe_content_html=True)

        if 85 <= score_pct <= 100:
            st.success("COMPETENT: You have qualified for a certificate.")
            name = st.text_input("Enter Full Name for Certificate:")
            if name:
                cert_bytes = create_certificate(name, score_pct)
                st.download_button("📜 Download Certificate", cert_bytes, f"OHS_Cert_{name}.pdf", "application/pdf")
        else:
            st.error("NOT YET COMPETENT: A score of 85% is required for certification.")

        if st.button("Restart & Shuffle Questions"):
            st.session_state.quiz_state = 'intro'
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.report_data = []
            st.rerun()

if __name__ == "__main__":
    main()
