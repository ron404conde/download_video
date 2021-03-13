from pytube import YouTube

print("Please choice: ")
print("1 for VIDEO")
print("2 for MP3")
print("===============")
download_mode = input("Download: ")

video_link = input("Enter Video URL: ")
video = YouTube(video_link)

if(download_mode == "1"):
    stream_video = video.streams.get_highest_resolution()
    stream_video.download()
elif(download_mode == "2"):
    stream_video = video.streams.get_audio_only()
    stream_video.download()
else:
    print("Incorect choice: 1 for video and 2 for mp3")

print("Done!")