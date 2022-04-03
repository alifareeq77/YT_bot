import requests as requests
# from pytube import YouTube
# from pytube import Playlist
import re


def checking_input() -> str:
    while True:
        url = 'https://www.youtube.com/watch?v=99yGdRRNe0M&list=PLuBig59nkpxxQFW4j3ofXknuhqbgUh7ZX'

        # url = input("enter URL : ")
        if "https://www.youtube.com" in url:
            try:
                re.compile("list(.*)$").search(url).group(1)
                try:

                    r = requests.get(url)
                    r.raise_for_status()
                    return url

                except requests.exceptions.RequestException as e:
                    print(str(e))
                    pass
            except AttributeError as a:
                print(a)
                pass
            else:
                try:
                    re.compile("wtach(.*)$").search(url).group(1)
                    try:
                        r = requests.get(url)
                        r.raise_for_status()
                        return url
                    except ConnectionError as e:
                        return str(e)

                except AttributeError as a:
                    print(a)
                    pass

        else:
            print("please enter valid input")
            continue

        break


def download_playlist():
    pass


def main():
    print(checking_input())


if __name__ == "__main__":
    main()
