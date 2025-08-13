import streamlit as st

def show_symbol_card(solid_name, symbol_data):
    st.markdown(f"""
    <div class="symbol-card" style="background-color:{symbol_data['color']};">
        <h2>{symbol_data['symbol']} {solid_name.capitalize()}</h2>
        <h4>Element: {symbol_data['element']}</h4>
        <p><em>{symbol_data['meaning']}</em></p>
    </div>
    """, unsafe_allow_html=True)
