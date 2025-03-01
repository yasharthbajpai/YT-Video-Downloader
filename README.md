# YouTube Video Downloader

A sleek, modern YouTube video downloader application built with Python, CustomTkinter, and pytubefix.

YouTube Downloader

## Features

- **User-friendly Interface**: Clean and intuitive dark-themed GUI
- **High-Quality Downloads**: Automatically selects the highest resolution available
- **Custom Save Location**: Choose where to save your downloaded videos
- **Progress Tracking**: Visual feedback during download process
- **Error Handling**: Comprehensive error messages for troubleshooting

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-video-downloader.git
   cd youtube-video-downloader
   ```

2. Install the required dependencies:
   ```bash
   pip install pytubefix customtkinter CTkMessagebox
   ```

## Usage

1. Run the application:
   ```bash
   python youtube_downloader.py
   ```

2. Enter a valid YouTube URL in the input field
3. Click the "Download Video" button
4. Select a save location and filename
5. Wait for the download to complete


## Technical Details

The application uses:
- `pytubefix`: A fork of pytube with fixes for YouTube API changes
- `customtkinter`: Modern UI toolkit for creating sleek interfaces
- `CTkMessagebox`: Enhanced message boxes for CustomTkinter
- `tkinter.filedialog`: Native file selection dialogs

## Limitations

- Downloads are limited to a single video at a time
- Playlist functionality is not currently supported
- Subject to YouTube's terms of service and API changes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Please respect copyright laws and YouTube's terms of service when downloading content.

