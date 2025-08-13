import streamlit as st

def show_symbol_card(solid_name, symbol_data):
    st.markdown(f"""
    <div style="text-align:center; padding:10px; border-radius:10px; background-color:{symbol_data['color']}; color:white;">
        <h2>{symbol_data['symbol']} {solid_name.capitalize()}</h2>
        <h4>Element: {symbol_data['element']}</h4>
        <p><em>{symbol_data['meaning']}</em></p>
    </div>
    """, unsafe_allow_html=True)

# import streamlit as st

# def show_symbol_card(solid_data):
#     st.markdown(f"""
#     ### {solid_data['symbol']} {solid_data['element']}
#     **Meaning**: {solid_data['meaning']}
#     """)
