import subprocess
import os

def create_reversed_video(input_file, output_file):
    # Create a temporary reversed video file
    reversed_file = "reversed.mp4"

    # Command to create the reversed video
    reverse_command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'reverse',
        '-preset', 'ultrafast',
        reversed_file
    ]

    # Execute the command to create the reversed video
    subprocess.run(reverse_command, check=True)

    # Command to concatenate original and reversed videos
    concat_command = [
        'ffmpeg',
        '-i', input_file,
        '-i', reversed_file,
        '-filter_complex', '[0:v][1:v]concat=n=2:v=1:a=0',
        output_file
    ]

    # Execute the command to concatenate videos
    subprocess.run(concat_command, check=True)

    # Clean up temporary reversed file
    os.remove(reversed_file)

if __name__ == "__main__":
    input_video = "input.mp4"  # Replace with your input file name
    output_video = "output.mp4"  # Replace with your desired output file name

    try:
        create_reversed_video(input_video, output_video)
        print(f"Successfully created {output_video}")
    except Exception as e:
        print(f"An error occurred: {e}")
