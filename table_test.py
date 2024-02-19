import streamlit as st
import pandas as pd
import numpy as np

# Function to generate a random DataFrame
def generate_random_data(rows, cols):
    data = np.random.randn(rows, cols)
    df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(cols)])
    return df

# Function to edit a cell in the DataFrame
def edit_cell(df, row_index, col_index, new_value):
    df.iloc[row_index, col_index] = new_value
    return df

# Main function
def main():
    st.title("Random Number Table Editor")

    # Generate random data
    rows = st.slider("Number of Rows", min_value=1, max_value=20, value=5)
    cols = st.slider("Number of Columns", min_value=1, max_value=10, value=3)

    df = generate_random_data(rows, cols)

    # Display the DataFrame
    st.write("Original DataFrame:")
    st.write(df)

    # Edit a cell
    st.subheader("Edit Cell")
    row_index = st.number_input("Row Index (0-based)", min_value=0, max_value=rows-1, value=0)
    col_index = st.number_input("Column Index (0-based)", min_value=0, max_value=cols-1, value=0)
    new_value = st.number_input("New Value", value=df.iloc[row_index, col_index])

    if st.button("Edit Cell"):
        df = edit_cell(df, row_index, col_index, new_value)
        st.write("Updated DataFrame:")
        st.write(df)

if __name__ == "__main__":
    main()
