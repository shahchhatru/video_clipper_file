from moviepy.editor import *
import os
import pytube
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
"""
Instruction:
for global setup 
    pip install moviepy
    pip install pytube 
    pip install imageio-ffmpeg
if using pipenv 
step 1 :clone the repository 
step 2: get into the folder with pipfile and pipfile.lock and run pipenv shell 
to activate environment.
step 3: run the file with  command pipenv run python file_name

"""

def video_downloader(youtube_link,path="video_folder"):
    """
    Args:
    youtube_link: pass the link of the video to be downloaded:

    """
    if not os.path.exists(path):
        os.mkdir(path)
    #for low resolution replace with
    #out_video=YouTube(youtube_link).streams.first().download(path)

    out_video=YouTube(youtube_link).streams.get_highest_resolution().download(path)

    return out_video

def video_clipper(video_path,start_time=0,interval_time=10,skip_time=0,subclip_no=0,no_of_clips=None,folder_name="subclipfolder",subclip_name="subclip_"):
    """
    all arguments are self descriptive but let me introduce you
    video_path: path of the video which is to be cliped it should be relative 
                '/video_folder/hello_love.mp4'
    no_of_clips: total no of clips that you want to have dividing your video
    folder_name: name of the folder where you want your clipped video to be stored.
    subclip_name: starting prefix for your clip example enter v_ if you want your 
            videos to arranged like v_1.mp4,v_2.mp4

    subclip_no: starting numerical index of subclip for example if you pass subclip_name
        ="v_" and subclip_no=6 then clips will be stored like v_6.mp4,v_7.mp4
    """
    clip_duration=VideoFileClip(video_path).duration
    n_clips=int((clip_duration-start_time)/(interval_time+skip_time))
    #subclip_no=0
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    end_time=start_time+interval_time
    if no_of_clips==None:
        no_of_clips=n_clips
    else:
        if no_of_clips>n_clips:
            print(f"there are only {n_clips} but you entered no_of_clips ={no_of_clips}")
            no_of_clips=n_clips
    
    
    for i in range(no_of_clips):
        video_file_path=os.path.join(folder_name,subclip_name+str(subclip_no+i)+".mp4")
        ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=video_file_path)
        
        start_time+=(interval_time+skip_time)
        end_time+=(interval_time+start_time)


        
    
def custom_clip(video_path,start_time=0,end_time=10,subclip_folder="subclip_folder",clip_name="custom_clip1"):
    if not os.path.exists(subclip_folder):
        os.mkdir(subclip_folder)
    video_file_path=os.path.join(subclip_folder,clip_name+".mp4")
    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=video_file_path)




#outvideo=video_downloader("https://www.youtube.com/watch?v=qY5HvKFmWmo")
#print(outvideo) #it simply prints the 


##video_clipper("video_folder/hello_love.mp4",no_of_clips=3)
##print("successfully ran")


custom_clip("video_folder/hello_love.mp4",start_time=60,end_time=70)