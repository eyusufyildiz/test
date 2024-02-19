import streamlit as st
import pandas as pd

def main():
    st.title('Simple Table Editor')

    # Initialize an empty DataFrame
    data = {'Name': [], 'Age': []}
    df = pd.DataFrame(data)

    # Display the current table
    st.write('## Current Table')
    st.write(df)

    # Add data to the table
    st.write('## Add Data')
    add_name = st.text_input('Enter Name')
    add_age = st.number_input('Enter Age')
    if st.button('Add Data'):
        new_row = {'Name': add_name, 'Age': add_age}
        df = df.append(new_row, ignore_index=True)
        st.write('Data Added Successfully!')
        st.write(df)

    # Edit cell in the table
    st.write('## Edit Cell')
    edit_index = st.number_input('Enter Index to Edit', min_value=0, max_value=len(df)-1, value=0)
    edit_column = st.selectbox('Select Column to Edit', options=df.columns)
    edit_value = st.text_input('Enter New Value')
    if st.button('Edit Cell'):
        df.at[edit_index, edit_column] = edit_value
        st.write('Cell Edited Successfully!')
        st.write(df)

if __name__ == '__main__':
    main()
