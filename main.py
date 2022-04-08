# import requests as requests
# import re
from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress


fuchsia = '\033[38;2;255;00;255m'
reset_color = '\033[39m'


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


#
# def valid_url() -> tuple[str, str] | str:
#     while True:
#         url = input("enter url: ")
#
#         # url = input("enter URL : ")
#         try:
#             re.compile("https://www.youtube.com/(.*)$").search(url).group(1)
#
#             if re.match("list(.*)$", url) is not None:
#                 try:
#
#                     r = requests.get(url)
#                     r.raise_for_status()
#                     return url, "playlist"
#
#                 except requests.exceptions.RequestException as e:
#                     print(str(e))
#                     pass
#             else:
#                 try:
#                     re.compile("watch(.*)$").search(url).group(1)
#                     try:
#                         r = requests.get(url)
#                         r.raise_for_status()
#                         return url, "single video"
#                     except ConnectionError as e:
#                         print("please enter valid input")
#                         return str(e)
#                         pass
#                 except (TypeError, AttributeError) as a:
#                     print(a)
#                     print("please enter valid input")
#
#                     pass
#
#         except AttributeError:
#             pass
#
#         else:
#             print("please enter valid input")
#             continue
#
#         break
#
def download_me() -> None:
    while True:
        url = 'https://youtube.com/playlist?list=PLF0tazU4jPNKsy2IahyE2tMntaLGZ-Js-'
        if "playlist" in url:
            p = Playlist(url=url)
            for vid in p.videos:
                size = convert_bytes(vid.streams.get_highest_resolution().filesize)
                resolution = vid.streams.get_highest_resolution().resolution
                title = vid.title
                print("title: " + title + "|| resolution: " + resolution + "|| file size: " + size)
                vid.streams.get_highest_resolution().download(output_path='.')
        elif "single video" in url:
            v = YouTube(url[0], on_progress_callback=on_progress)
            size = convert_bytes(v.streams.get_highest_resolution().filesize)
            # resolution = v.streams.get_highest_resolution().resolution
            title = v.title
            print("title: " + title + "|| resolution: " + "|| file size: " + size)
            v.streams.get_highest_resolution().download(output_path='.')
            print(f'\nFinished downloading:  {v.title}' + reset_color)


def main():

    download_me()


if __name__ == "__main__":
    main()
