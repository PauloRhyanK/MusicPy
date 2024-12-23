import os
from pytube import YouTube
from youtubesearchpython import VideosSearch

def download_video(file_path, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    with open(file_path, 'r') as file:
        music_titles = file.readlines()
    
    for title in music_titles:
        title = title.strip()
        if title:
            try:
                # Use youtube-search-python to search for the video
                videos_search = VideosSearch(title, limit=1)
                video_result = videos_search.result()
                video_url = video_result['result'][0]['link']
                
                yt = YouTube(video_url)
                stream = yt.streams.filter(only_audio=True).first()
                stream.download(output_path=download_dir, filename=f"{title}.mp3")
                print(f"Downloaded {title} successfully")
            except Exception as e:
                print(f"Error downloading {title}: {e}")

file_path = 'Musicas.txt'
download_dir = 'Baixadas'
download_video(file_path, download_dir)