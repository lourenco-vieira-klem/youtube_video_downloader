import sys
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import re
from custom_errors import ConfigError, CustomError
import os


class VideoDownloader():
    def __init__(self, video_url: str) -> None:
        self.video_url = video_url
    
    def show_download_options(self, video):
        fmt_streams = video.streams.fmt_streams
        for index, stream in enumerate(fmt_streams):
            print(f'option_id: {index} | mime_type: {stream.mime_type} | resolution: {stream.resolution} | file_size_in_mb {stream.filesize_mb} | file_codecs: {stream.codecs}')
    
    def create_download_folder_if_not_exists(self):
        if not os.path.exists('./downloads'): 
            os.mkdir('./downloads')
            
    def start_download(self):
        video = YouTube(self.video_url)
        self.show_download_options(video)
        
        chosen_option = input("choose an option from the options_ids: ")
        
        try:
            chosen_option = int(chosen_option)
        except:
            raise ConfigError(message="invalid option_id")
        
        if chosen_option > len(video.streams.fmt_streams):
            raise ConfigError(message="invalid option_id")
        
        video_stream = video.streams.get_by_itag(int(video.streams.fmt_streams[chosen_option].itag))
        video_stream.download('./downloads/')

if __name__ == '__main__':
   try:
        video_url = sys.argv[1]
        
        if not re.search(r'playlist', video_url):
            downloader = VideoDownloader(
                video_url=video_url
            )
            
            downloader.start_download()
   
   except CustomError as ex:
       print(ex.message)

   except RegexMatchError:
       print("Invalid video url.")
       
   except Exception as ex:
       print(ex)
