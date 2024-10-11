import csv

# Define input and output file paths
input_file = "google-sanepadelight.csv"  # Replace with your input CSV file path
output_file = 'reviews.csv'  # Output CSV file for extracted reviews

# Open the input CSV file
with open(input_file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Open the output CSV file in append mode
    with open(output_file, 'a', newline='', encoding='utf-8') as newfile:
        csvwriter = csv.writer(newfile)
        
        # Skip the header of the original file
        next(csvreader)
        
        # Loop through each row in the input CSV file
        for row in csvreader:
            # Extract the review text (7th column, index 6)

            review = row[6]
            
            # Write the extracted review into the new CSV file
            csvwriter.writerow([review])

print(f"Reviews successfully appended to {output_file}")
