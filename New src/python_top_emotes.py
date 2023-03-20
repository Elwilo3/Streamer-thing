import os

# Set the folder containing the chat data text files to the current working directory
folder = os.getcwd()

# Initialize a dictionary to store chat counts for each user
chat_counts = {}

# Loop through each file in the folder
for filename in os.listdir(folder):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Open the file
        with open(os.path.join(folder, filename), 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Get the username from the line
                username = line.strip()
                # If the username is not already in the dictionary, add it with a count of 0
                if username not in chat_counts:
                    chat_counts[username] = 0
                # Increment the chat count for the user
                chat_counts[username] += 1

# Sort the chat counts in descending order
sorted_chat_counts = sorted(chat_counts.items(), key=lambda x: x[1], reverse=True)

# Calculate the total number of chats
total_chats = sum(chat_counts.values())

# Initialize a list to store the output data
output_data = []

# Initialize a counter for the percentage
percent = 0

# Loop through each user and their chat count
for user, count in sorted_chat_counts:
    # Calculate the percentage of chats the user has sent compared to others
    user_percent = count / total_chats * 100
    # Add the user, their chat count, and their percentage to the output data
    output_data.append([percent, count, user_percent])
    # Increment the percentage counter
    percent += user_percent

# Write the output data to a CSV file
with open('chat_data_output.csv', 'w') as file:
    # Write the column headers
    file.write('Percent, Chat Count, User Percent\n')
    # Loop through each row of data
    for row in output_data:
        # Write the row to the file as a CSV line
        file.write(','.join(str(x) for x in row) + '\n')
