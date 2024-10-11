import pandas as pd
import re

# Function to clean the review text
def clean_text(text):
    # Ensure the text is a string to avoid errors
    if isinstance(text, str):
        # Remove any character that's not a letter or space
        text = re.sub(r'[^a-zA-Z\s]', '', text)  
        # Remove double and single quotes
        text = re.sub(r'"', '', text)
        text = re.sub(r"'", '', text)
        # Remove unnecessary spaces
        text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space and strip leading/trailing spaces
    return text

# Load the data
data = pd.read_csv('reviews.csv', header=None, names=["review"], on_bad_lines='skip')

# Clean the reviews
data['review'] = data['review'].apply(clean_text)

# Remove empty lines and lines that were only quotes after cleaning
data = data[data['review'].str.strip() != '']  # Keep only non-empty reviews
data = data[data['review'] != '']  # Remove lines that were only quotes

# Save only the cleaned reviews to a new CSV file
data['review'].to_csv('cleaned_reviews.csv', index=False, header=False)
