import os

# Set the folder containing the chat data text files
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

# Print the top 3 users who typed the most
for i in range(min(3, len(sorted_chat_counts))):
    print(f'{sorted_chat_counts[i][0]}: {sorted_chat_counts[i][1]} chats')
