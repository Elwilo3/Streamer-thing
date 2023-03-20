import chardet

# detect the encoding of the file
with open('chat_output3.txt', 'rb') as f:
    result = chardet.detect(f.read())

# open the input file using the detected encoding
with open("chat_output8.txt", "r", encoding=result['encoding']) as input_file:
    # open the output file with UTF-8 encoding
    with open("username8.txt", "w", encoding="utf-8") as chat_output:
        for line in input_file:
            chat_message = line.split("]")[1].strip()
            # Do something with the chat_message variable
            # For example, write it to the output file
            chat_output.write(chat_message + "\n")
