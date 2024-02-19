import streamlit as st
import pandas as pd

# Create a function to add data to the table
def add_data(df, name, age):
    new_data = {'Name': name, 'Age': age}
    df = df.append(new_data, ignore_index=True)
    return df

# Create a function to edit a cell in the table
def edit_cell(df, index, column, new_value):
    df.at[index, column] = new_value
    return df

def main():
    st.title('Table Editor')

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
        df = add_data(df, add_name, add_age)
        st.write('Data Added Successfully!')
        st.write(df)

    # Edit cell in the table
    st.write('## Edit Cell')
    edit_index = st.number_input('Enter Index to Edit', min_value=0, max_value=len(df)-1, value=0)
    edit_column = st.selectbox('Select Column to Edit', options=df.columns)
    edit_value = st.text_input('Enter New Value')
    if st.button('Edit Cell'):
        df = edit_cell(df, edit_index, edit_column, edit_value)
        st.write('Cell Edited Successfully!')
        st.write(df)

if __name__ == '__main__':
    main()
