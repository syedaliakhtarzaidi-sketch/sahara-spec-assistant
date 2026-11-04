    st.markdown("### Our Ingredient World")
    st.caption("Explore the premium ingredients supplied by Sahara UK Foods.")

    col1, col2, col3 = st.columns(3, gap="large")

    for col, image, name, description in [
        (col1, DATES_IMAGE, "Dates", "Medjool · Deglet Noor · Pitted Dates"),
        (col2, NUTS_IMAGE, "Nuts", "Almonds · Cashews · Pistachios · Walnuts"),
        (col3, DRIED_FRUITS_IMAGE, "Dried Fruits", "Apricots · Raisins · Figs · Prunes"),
    ]:
        with col:
            with st.container(border=True):
                st.markdown(
                    f'''
                    <div class="ingredient-image-frame">
                        <img src="{html.escape(image, quote=True)}"
                             alt="{html.escape(name, quote=True)}">
                    </div>
                    ''',
                    unsafe_allow_html=True,
                )
                st.markdown(f"**{name}**")
                st.caption(description)
