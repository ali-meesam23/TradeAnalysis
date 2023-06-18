import os
import streamlit as st

# Function to read HTML files from a directory
def read_html_files(directory):
    html_files = []
    for file in os.listdir(directory):
        if file.endswith(".html"):
            file_path = os.path.join(directory, file)
            with open(file_path, "r") as f:
                html_content = f.read()
                html_files.append(html_content)
    return html_files


# Main function
def main():
    # Set the title of the dashboard
    st.title("HTML Files Dashboard")

    FILENAME = st.text_input("Analysis Folder", value='23Jun17-paper')
    graph_folder = os.path.join(os.getenv("MAIN_DATA_PATH"), 'TradeReports', 'IB', FILENAME)
    
    # Set the directory where the HTML files are located
    directory = graph_folder

    # Read the HTML files from the directory
    html_files = read_html_files(directory)

    # Initialize the index to display the first HTML file
    index = st.number_input("Select HTML File", value=0, min_value=0, max_value=len(html_files)-1, step=1)

    # Display the selected HTML file
    st.write(html_files[index], unsafe_allow_html=True)

    # Add "Prev" and "Next" buttons
    col1, col2 = st.columns(2)
    if index > 0:
        if col1.button("Prev"):
            index -= 1

    if index < len(html_files) - 1:
        if col2.button("Next"):
            index += 1

    # Update and display the selected HTML file
    st.write(html_files[index], unsafe_allow_html=True)

if __name__ == "__main__":
    main()
