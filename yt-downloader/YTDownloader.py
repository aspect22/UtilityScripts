import os
import yt_dlp
import ffmpeg
from termcolor import colored


def log(message, level="info"):
    colors = {"info": "blue", "success": "green", "warning": "yellow", "error": "red"}
    print(colored(f"[{level.upper()}] {message}", colors.get(level, "blue")))


# Global set to track which videos have been logged
logged_titles = set()


def progress_hook(d):
    # Log the video title only once when it starts downloading
    if d.get("status") == "downloading":
        title = d.get("info_dict", {}).get("title")
        if title and title not in logged_titles:
            log(f"Downloading: {title}", "info")
            logged_titles.add(title)


# Custom logger for yt-dlp that respects silent mode
class YTDLPLogger:
    def __init__(self, silent):
        self.silent = silent

    def debug(self, msg):
        if not self.silent:
            print(colored(f"[YTDLP DEBUG] {msg}", "blue"))

    def info(self, msg):
        if not self.silent:
            print(colored(f"[YTDLP INFO] {msg}", "blue"))

    def warning(self, msg):
        if not self.silent:
            print(colored(f"[YTDLP WARNING] {msg}", "yellow"))

    def error(self, msg):
        if not self.silent:
            print(colored(f"[YTDLP ERROR] {msg}", "red"))


log("Starting the download script", "info")


# Ask user if they want to download a single file or multiple files
mode = (
    input(colored("Download a single song/playlist or multiple? (s/m): ", "cyan"))
    .strip()
    .lower()
)

# Ask user if they want silent mode for yt-dlp and ffmpeg commands
silent_mode_input = (
    input(colored("Do you want silent mode? (y/n): ", "cyan")).strip().lower()
)
silent_mode = True if silent_mode_input == "y" else False
log(f"Silent mode is {'enabled' if silent_mode else 'disabled'}", "info")

if mode == "m":
    urls_input = input(
        colored("Enter the video or playlist URL separated by commas: ", "cyan")
    )
    video_urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    log(f"Selected multiple download mode with {len(video_urls)} URL(s)", "info")
else:
    video_url = input(colored("Enter the video or playlist URL: ", "cyan")).strip()
    video_urls = [video_url]
    log("Selected single download mode", "info")

temp_folder = os.path.join(os.getenv("TEMP"), "yt-dlp_temp")
os.makedirs(temp_folder, exist_ok=True)
log(f"Temporary folder created at: {temp_folder}", "info")

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
        {"key": "EmbedThumbnail"},
        {"key": "FFmpegMetadata"},
    ],
    "outtmpl": os.path.join(temp_folder, "%(title)s.%(ext)s"),
    "writethumbnail": True,
    "convert_thumbnails": "jpg",
    "quiet": silent_mode,  # Suppress yt-dlp output when in silent mode
    "no_warnings": silent_mode,  # Suppress warnings as well
    "logger": YTDLPLogger(silent_mode),
    "progress_hooks": [progress_hook],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        log("Initiating download process...", "info")
        ydl.download(video_urls)
    log("Download process completed", "success")
except Exception as e:
    log(f"An error occurred during download: {str(e)}", "error")

# Move downloaded mp3 files to the current working directory
try:
    for file in os.listdir(temp_folder):
        if file.endswith(".mp3"):
            src = os.path.join(temp_folder, file)
            dst = os.path.join(os.getcwd(), file)
            os.rename(src, dst)
            log(f"Moved file {file} to current directory", "info")
    log("All mp3 files moved successfully", "success")
except Exception as e:
    log(f"An error occurred while moving files: {str(e)}", "error")

# Clean up temporary folder
try:
    for file in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, file))
    os.rmdir(temp_folder)
    log("Temporary folder cleaned up", "success")
except Exception as e:
    log(f"An error occurred during cleanup: {str(e)}", "error")

log("Downloads processed successfully!", "success")
