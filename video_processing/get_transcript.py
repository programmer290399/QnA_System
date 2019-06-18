import re 
import json
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs
import urllib.request



def video_id_extractor(value):

    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    
    return None



def get_transcript_from_URL(url):
        video_id = video_id_extractor(url)
        print('Retriving :', video_id)
        if video_id is not None :
            try :
                transcript  = YouTubeTranscriptApi.get_transcript(video_id)
                return transcript
            except Exception as e :
                print('Error on :', url, ':' , e )

if __name__=='__main__':
    link = input("Enter the video link :")
    print(get_transcript_from_URL(link))