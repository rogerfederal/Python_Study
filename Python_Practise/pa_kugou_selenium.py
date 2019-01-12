import requests
from concurrent.futures import ProcessPoolExecutor


def download(url):
    song_title = url.split("#")[0]
    mp3 = url.split("#")[1]
    # print(str(mp3).replace("\n",""))
    # print(song_title," ",mp3)
    print("downloading {}".format(song_title))
    response = requests.get(str(mp3).replace("\n","")).content
    with open('/Users/u44084750/Desktop/mp33/{}.mp3'.format(song_title),'wb') as ff:
        ff.write(response)


if __name__ == "__main__":
    with open('/Users/u44084750/Desktop/mp3/url.txt') as f:
        urls = f.readlines()
        pool = ProcessPoolExecutor(max_workers=100)
        pool.map(download,urls)