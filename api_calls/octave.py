#!/user/bin/env python


import json
import requests
import os
import wget


class Octave:
    def __init__(self):
        self.payload = {}
        self.headers = {'Authorization': '51fal5fybpmqk0i2v1potkxoh1neqbu1'}
        self.source_path = '{}/music/'.format(os.getenv('APP_PATH'))

    def getSongs(self, inputString):
        song_title = self.refactorSongName(inputString)
        url = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs?query=" + song_title + "&page=1&size=1"
        full_list = requests.request("GET", url, headers=self.headers, data=self.payload)
        data = json.loads(full_list.content)
        song_list = data['songs']
        if not song_list:
            print('No song found with that name')
            return 1
        song = song_list[0]
        self.getSong(song['id'], song['title'])
        return 0

    def getSong(self, song_id, song_title):
        url = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs/" + str(song_id)
        song = json.loads(requests.request("GET", url, headers=self.headers, data=self.payload).content)
        print(song['playUrl'])
        self.download(song['playUrl'])

    def refactorSongName(self, song_title):
        title = song_title.split(' ')
        output_title = '*'.join(title)
        print(output_title)
        return output_title

    def download(self, url, song_title):
        print('Downloading file:', song_title)
        wget.download(url, out='{}{}'.format(self.source_path, song_title))
        filename = wget.download(url)
        print(filename)
        return filename


if __name__ == "__main__":
    octave = Octave()
    octave.getSongs("hello there")
