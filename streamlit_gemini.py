from vertexai.preview.generative_models import GenerativeModel
import streamlit as st


@st.cache_data
def call_gemini(prompt):
    model = GenerativeModel("gemini-1.0-pro")
    response = model.generate_content(prompt)

    return response.candidates[0].content.parts[0].text


def streamlit_app():
    st.markdown("## User")

    prompt = st.text_input(
        label="Your Prompt",
        label_visibility="hidden",
        value="Why do cars have four wheels?",
    )
    response = call_gemini(prompt)

    st.markdown("## Gemini")
    st.markdown(response)


streamlit_app()


# necessary installs:
## pip install streamlit
## pip install vertexai

# streamlit run /Users/brettleighton/Code/streamlit_gemini.py --server.port 8080
