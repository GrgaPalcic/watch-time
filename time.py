import os
from tinytag import TinyTag

# set folder path
folder_path = "."
# add more extensions if needed
video_extensions = ['.mp4', '.avi']

def get_total_video_duration(folder_path):
    total_duration = 0

    for root, dirs, files in os.walk(folder_path):
        # exclude subdirectories starting with _
        dirs[:] = [d for d in dirs if not d.startswith('_')]

        for file in files:
            if any(file.lower().endswith(ext) for ext in video_extensions):
                file_path = os.path.join(root, file)
                try:
                    tag = TinyTag.get(file_path)
                    if tag.duration:
                        total_duration += tag.duration
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    
    return total_duration

def format_duration(seconds):
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == "__main__":
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory")
        exit(1)
    
    total = get_total_video_duration(folder_path)
    print(f"Total duration of all videos: {format_duration(total)}")
