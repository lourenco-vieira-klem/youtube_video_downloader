import sys
import re
import os
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError
from custom_errors import ConfigError, CustomError


class Downloader():
    def __init__(self, youtube_url: str) -> None:
        self.youtube_url = youtube_url
    
    def show_download_options(self, video):
        fmt_streams = video.streams.fmt_streams
        for index, stream in enumerate(fmt_streams):
            print(f'option_id: {index} | mime_type: {stream.mime_type} | resolution: {stream.resolution} | file_size_in_mb {stream.filesize_mb} | file_codecs: {stream.codecs}')
    
    def create_download_folder_if_not_exists(self):
        if not os.path.exists('./downloads'): 
            os.mkdir('./downloads')
    
    def validate_chosen_option(self, chosen_option: str, video):
        try:
            chosen_option = int(chosen_option)
        except:
            raise ConfigError(message="invalid option_id")
        
        if chosen_option > len(video.streams.fmt_streams):
            raise ConfigError(message="invalid option_id")
    
    def download_stream(self, video, chosen_option: str):
        video_stream = video.streams.get_by_itag(int(video.streams.fmt_streams[int(chosen_option)].itag))
        video_stream.download('./downloads/')

class VideoDownloader(Downloader):
    def start_video_download(self):
        video = YouTube(self.youtube_url)
        self.show_download_options(video)
        
        chosen_option = input("choose an option from the options_ids: ")
        self.validate_chosen_option(chosen_option, video)
        self.download_stream(video, chosen_option)

class PlaylistDownloader(Downloader):
    def start_playlist_download(self):
        playlist = Playlist(self.youtube_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        for video in playlist.videos:
            self.show_download_options(video)
            chosen_option = input("choose an option from the options_ids: ")
            self.validate_chosen_option(chosen_option, video)
            self.download_stream(video, chosen_option)

if __name__ == '__main__':
   try:
        youtube_url = sys.argv[1]
        
        if not re.search(r'playlist', youtube_url):
            downloader = VideoDownloader(
                youtube_url=youtube_url
            )
            
            downloader.start_video_download()
        
        else:
            downloader = PlaylistDownloader(
                youtube_url=youtube_url
            )
            
            downloader.start_playlist_download()
            
   except CustomError as ex:
       print(ex.message)

   except RegexMatchError:
       print("Invalid video url.")
       
   except Exception as ex:
       print(ex)
