import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.writer import generate_spin
from agents.reviewer import review_text
from agents.editor import final_edit

st.title("Book Chapter Refinement Interface")

text_input = st.text_area("Paste original or AI-written text below", height=300)

if st.button("Generate Spin (AI Writer)"):
    st.session_state['spin'] = generate_spin(text_input)
    st.success("Spin complete")

if 'spin' in st.session_state:
    st.subheader("AI Writer Output")
    st.text_area("Spun Text", value=st.session_state['spin'], height=300)

if st.button("Review Text (AI Reviewer)"):
    st.session_state['reviewed'] = review_text(st.session_state['spin'])
    st.success("Review complete")

if 'reviewed' in st.session_state:
    st.subheader("AI Reviewer Output")
    st.text_area("Reviewed Text", value=st.session_state['reviewed'], height=300)

if st.button("Final Edit (AI Editor)"):
    final = final_edit(st.session_state['reviewed'])
    st.text_area("Final Output", value=final, height=300)
