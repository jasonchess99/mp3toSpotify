import os

def list_audio_files(directory, extensions=('mp3', 'wav', 'ogg')):
    audio_files = []

    # Walk through the directory tree
    for root, _, files in os.walk(directory):
        # Filter files based on extensions
        for file_name in files:
            if file_name.lower().endswith(extensions):
                audio_files.append(file_name)

    return audio_files

def save_to_text_file(file_list, output_file='audio_files.txt'):
    with open(output_file, 'w') as file:
        # Write only the file names (without extensions) to the text file
        file.write("\n".join(os.path.splitext(file)[0] for file in file_list))

# Replace 'your_directory' with the path to your music directory
music_directory = '/home/jason/Projects/mp3toSpotify/music_library/'
audio_files_list = list_audio_files(music_directory)

# Replace 'your_output_file.txt' with the desired output file name
save_to_text_file(audio_files_list, 'your_output_file.txt')
