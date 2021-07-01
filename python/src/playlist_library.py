from .video_library import VideoLibrary
"""A class used to represent a Playlist Library."""

class PlaylistLibrary:

    def __init__(self):
        self._playlists={}

    def create_playlist(self,name:str):
        if name.lower() not in self._playlists.keys():
            self._playlists[name]=[]
            return "Successfully created new playlist: "+name

        else:
            return "Cannot create playlist: Playlist with the same name already exists"

    def add_to_playlist(self,name,video_id):
        if name not in self._playlists.keys():
            return "Cannot add video to "+name+": Playlist does not exist"

        elif video_id==self._playlists[name]:
            return "Cannot add video to "+name+": Video already added"

        elif VideoLibrary().get_video(video_id) is None:
            return "Cannot add video to "+name+": Video does not exist"

        else:
            self._playlists[name].append(video_id)
            return "Added video to "+name+": "+VideoLibrary().get_video(video_id).title

    def show_playlists(self):
        return self._playlists.keys()

    def show_playlist(self,name):
        return self._playlists[name]

    def get_playlists(self):
        return self._playlists