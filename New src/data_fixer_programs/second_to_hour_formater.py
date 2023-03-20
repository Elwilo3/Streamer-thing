def time_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(":")
    return int(hours)*3600 + int(minutes)*60 + int(seconds)

with open("output_file.txt", "r") as input_file, open("output_formated.txt", "w") as output_file:
    for line in input_file:
        time_str = line.strip()
        seconds = time_to_seconds(time_str)
        output_file.write(str(seconds) + "\n")
