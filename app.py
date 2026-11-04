
# -------------------- HERO SECTION --------------------

if page == "AI Intelligence":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">SAHARA AI INTELLIGENCE</div>
        <div class="hero-title">
            Intelligence behind<br>
            every ingredient.
        </div>
        <div class="hero-text">
            Your central workspace for product specifications,
            food quality intelligence, technical documentation
            and compliance analysis.
        </div>
        <div class="hero-company">SAHARA UK FOODS</div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------- AI WORKSPACE --------------------

    st.markdown(
        '<div class="section-heading">AI Intelligence Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="workspace">
        <div class="workspace-title">
            What would you like to analyse?
        </div>
        <div class="workspace-description">
            Ask questions about product specifications,
            quality parameters, allergens or compliance documents.
        </div>
    </div>
    """, unsafe_allow_html=True)

    question = st.text_input(
        "Your question",
        placeholder="e.g. What is the aflatoxin level in this product?",
        label_visibility="collapsed",
        key="sahara_question"
    )

    if st.button("Start Analysis", key="start_analysis"):
        if question.strip():
            st.info(
                "Design preview: AI analysis engine is not connected yet."
            )
        else:
            st.warning("Please enter a question first.")
