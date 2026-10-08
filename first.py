import streamlit as st


st.set_page_config(
    page_title="Phishing Awareness Demo",
    page_icon="🛡️",
    layout="centered",
)

st.title("🛡️ Phishing Awareness Demo")
st.caption("A safe, interactive lesson for recognizing suspicious messages.")

st.info(
    "Training only: this demo does not ask for or collect passwords, "
    "personal information, or message submissions."
)

st.subheader("Practice: inspect this suspicious message")
st.markdown(
    """
    > **From:** Account Support `<alerts@account-check.example>`  
    > **Subject:** Urgent: action required  
    > Your account will be closed in 2 hours. Confirm your details now at  
    > `http://account-check.example.invalid/verify` to keep access.
    """
)

st.write("Which warning signs can you spot? Select all that apply.")

with st.form("awareness_quiz"):
    urgent_language = st.checkbox("It uses urgency or threatens account closure.")
    unfamiliar_link = st.checkbox("The link uses an unfamiliar, untrusted domain.")
    asks_for_details = st.checkbox("It pressures me to confirm sensitive details.")
    unverified_sender = st.checkbox("The sender has not been independently verified.")
    submitted = st.form_submit_button("Check my answers")

if submitted:
    correct_signs = {
        "It uses urgency or threatens account closure.": urgent_language,
        "The link uses an unfamiliar, untrusted domain.": unfamiliar_link,
        "It pressures me to confirm sensitive details.": asks_for_details,
    }
    correct_signs["The sender has not been independently verified."] = unverified_sender
    score = sum(correct_signs.values())

    if score == len(correct_signs):
        st.success("Correct — you spotted all the warning signs.")
    else:
        st.warning(f"You identified {score} of 4 warning signs. Review the guidance below.")

    st.markdown(
        """
        **Why this message is suspicious**

        - It creates pressure with a short deadline and a threat.
        - The example link uses an unfamiliar domain. Do not open suspicious links.
        - It asks you to confirm sensitive details through that link.
        - A sender address or display name alone does not prove who sent a message.
        """
    )

st.subheader("Safer next steps")
st.markdown(
    """
    1. Do not click the link or reply with sensitive information.
    2. Visit the service using its official app or a bookmark you already trust.
    3. Verify unexpected requests through a separate, known contact method.
    4. Report the message using your organization's normal reporting process.
    """
)

with st.expander("Run or deploy this demo"):
    st.code("pip install -r requirements.txt\nstreamlit run first.py", language="bash")
    st.write(
        "For Streamlit Community Cloud, push this app and `requirements.txt` "
        "to a GitHub repository, then create an app that runs `first.py`."
    )
