from model import download_yt_video, process_video
from tkinter import Tk, Label, Entry, Button
import os

# Process Video
def start_processing():
        global video_path
        video_url = entry.get()
        video_path = download_yt_video(video_url)
        if video_path:
            process_video(video_path)

# Tkinter Window
root = Tk()
root.title("Load URL video")
root.geometry("350x150")
Label(root, text="Insert Youtube URL video: ").pack(pady=20)
entry = Entry(root, width=50)
entry.pack(padx=5, anchor="center")
Button(root, text="Load and Process",command=start_processing).pack(pady=10, padx=20, anchor="e")
root.mainloop()


def main():
# Delete video
    if os.path.exists(video_path):
        os.remove(video_path)
        print(f"Video deleted: {video_path}")
    root.mainloop()

if __name__ == "__main__":
    main()