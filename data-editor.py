import streamlit as st
import pandas as pd


# Create a session variable
if 'boq' not in st.session_state:
    st.session_state['boq'] = pd.DataFrame()


def page():
    st.write("# Test")

    # If button is pressed, assign a pre-built dataframe to the variable.
    if st.button("Analyze", type="primary"):
        st.session_state['boq'] = pd.DataFrame(
            data={
                "ANALYZE": [True, False, True],
                "CAT": ["Car", "Truck", "Bike"],
                "TYPE": ["blue", False, "yellow"],
                "DESC": ["two door", "four door", "single"],
            }
        )

    # If variable is not empty, construct a data_editor.
    if not st.session_state['boq'].empty:
        edited_df = st.data_editor(
            st.session_state['boq'],
            height=700
        )

        # If column "ANALYZE" is set to False, set the value of
        # "TYPE" to None. Be sure to update column "TYPE" only if
        # there are changes to column "ANALYZE".
        is_equal = edited_df['ANALYZE'].equals(st.session_state['boq']['ANALYZE'])
        if not is_equal:
            edited_df.loc[edited_df["ANALYZE"] == False, "TYPE"] = None
            edited_df.ffill(inplace=True)
            st.session_state['boq'] = edited_df  # update the variable

            # Set streamlit to rerun the script from top to bottom
            # to update the data editor.
            st.rerun()

page()
