# YouTube Music Downloader

A Python script that downloads videos or playlists using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and extracts audio with FFmpeg. This tool supports both single and multiple downloads, provides colorful log output using [termcolor](https://pypi.org/project/termcolor/), and includes a silent mode to suppress third-party command outputs for a cleaner interface.

## Features

- **Custom Logging:** Uses colored log messages to clearly indicate progress, warnings, and errors.
- **Multiple Download Modes:** Choose to download a single video or multiple videos (comma-separated).
- **Silent Mode Option:** Option to suppress detailed outputs from yt-dlp and FFmpeg.
- **Temporary File Management:** Automatically handles temporary directories and cleans up after downloads.

## Requirements

Before running the script, ensure you have the following:

- [**Python 3.6+**](https://www.python.org/downloads/)
- [**FFmpeg**](https://ffmpeg.org/download.html) The actual FFmpeg binary must be installed and accessible in your system’s PATH.
- **Python Packages:** Listed in the [requirements.txt](#requirementstxt)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aspect22/UtilityScripts.git
   cd UtilityScripts/yt-downloader
   ```

2. **Install the Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure FFmpeg is installed:**

   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - On Windows: Download from [FFmpeg official website](https://ffmpeg.org/) and add it to your PATH.

## Usage

Run the script with:

```bash
python YTDownloader.py
```

The script will prompt you to choose between downloading a single video or multiple videos. It also asks if you want silent mode enabled to suppress the verbose output from yt-dlp and FFmpeg.

### Sample Prompts:

- **Download Mode:**
  - _Download a single file or multiple? (s/m):_
- **Video URL(s):**
  - For multiple downloads, enter URLs separated by commas.
- **Silent Mode:**
  - _Do you want silent mode? (y/n):_

As the script runs, it will display colorful log messages indicating which video is currently being downloaded and other progress updates.

## requirements.txt

```txt
ffmpeg==1.4
termcolor==2.5.0
yt_dlp==2025.1.26
```

install the required packages using the following command:

```bash
pip install -r requirements.txt
```
