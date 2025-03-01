from pytubefix import YouTube
from pytubefix.cli import on_progress
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog

# Function to download video
def download_video(url, file_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        downloaded_file = stream.download(output_path=file_path.rsplit("/", 1)[0], filename=file_path.rsplit("/", 1)[1])
        CTkMessagebox(title="Download Complete", message=f"Video downloaded to:\n{downloaded_file}", icon="check")
    except Exception as e:
        CTkMessagebox(title="Error", message=f"An error occurred:\n{e}", icon="cancel")

# Function to select file save location
def select_save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save Video As",
        defaultextension=".mp4",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    return file_path

# Function to start video download
def start_download():
    video_url = url_entry.get().strip()
    if not video_url:
        CTkMessagebox(title="Input Error", message="Please enter a valid YouTube URL.", icon="warning")
        return
    save_file_path = select_save_file()
    if not save_file_path:
        CTkMessagebox(title="File Selection", message="No file selected. Please select a file name and location to save the video.", icon="warning")
        return
    download_video(video_url, save_file_path)

# Main GUI setup using CustomTkinter
if __name__ == "__main__":
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue") 

    root = ctk.CTk()
    root.title("YouTube Video Downloader (Enhanced)")
    root.geometry("500x300")

    # Title Label
    ctk.CTkLabel(root, text="Enter YouTube Video URL:", font=("Arial", 14)).pack(pady=20)

    # URL Entry Field
    url_entry = ctk.CTkEntry(root, width=400, font=("Arial", 12))
    url_entry.pack(pady=10)

    # Download Button
    download_button = ctk.CTkButton(root, text="Download Video", font=("Arial", 14), command=start_download)
    download_button.pack(pady=30)

    root.mainloop()
