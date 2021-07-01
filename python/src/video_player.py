"""A video player class."""

from .video_library import VideoLibrary
from .playlist_library import PlaylistLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playlist_library=PlaylistLibrary()
        global playing_video_id
        global paused_video_id
        playing_video_id = ""
        paused_video_id=""

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        all_videos=self._video_library.get_all_videos()
        for video in all_videos:
            print(video.title+'('+video.video_id+')'+'[',*video.tags,']')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global playing_video_id

        all_videos = self._video_library.get_all_videos()
        if video_id not in [video.video_id for video in all_videos]:
            print("Cannot play video: Video does not exist")

        elif playing_video_id is "":
            playing_video_id=video_id
            playing_video_title=self._video_library.get_video(video_id).title
            print("Playing video:",playing_video_title)

        else:
            playing_video_title=self._video_library.get_video(playing_video_id).title
            print("Stopping video:", playing_video_title)
            playing_video_id = video_id
            playing_video_title = self._video_library.get_video(video_id).title
            print("Playing video:", playing_video_title)

    def stop_video(self):
        """Stops the current video."""
        global playing_video_id

        if playing_video_id is "":
            print("Cannot stop video: No video is currently playing")

        else:
            print("Stopping video:",self._video_library.get_video(playing_video_id).title)
            playing_video_id=""

    def play_random_video(self):
        """Plays a random video from the video library."""
        global playing_video_id
        all_videos = self._video_library.get_all_videos()
        rand=random.randint(0, len(all_videos)-1)

        if len(all_videos) is 0:
            print("No videos available")

        elif playing_video_id is not "":
            print("Stopping video:", self._video_library.get_video(playing_video_id).title)
            playing_video_id=""
            print("Playing video:",all_videos[rand].title)
            playing_video_id=all_videos[rand].video_id

        else:
            print("Playing video:", all_videos[rand].title)
            playing_video_id = all_videos[rand].video_id

    def pause_video(self):
        """Pauses the current video."""
        global playing_video_id
        global paused_video_id

        if playing_video_id is "" and paused_video_id is "":
            print("Cannot pause video: No video is currently playing")

        elif playing_video_id is "" and paused_video_id is not "":
            print("Video already paused:", self._video_library.get_video(paused_video_id).title)

        else:
            print("Pausing video:", self._video_library.get_video(playing_video_id).title)
            paused_video_id,playing_video_id=playing_video_id,""


    def continue_video(self):
        """Resumes playing the current video."""
        global playing_video_id
        global paused_video_id

        if paused_video_id is "" and playing_video_id is "":
            print("Cannot continue video: No video is currently playing")

        elif paused_video_id is "" and playing_video_id is not "":
            print("Cannot continue video: Video is not paused")

        else:
            print("Continuing video:", self._video_library.get_video(paused_video_id).title)
            playing_video_id, paused_video_id=paused_video_id, ""



    def show_playing(self):
        """Displays video currently playing."""
        global playing_video_id
        global paused_video_id

        if playing_video_id is "" and paused_video_id is "":
            print("No video is currently playing")

        else:
            if paused_video_id is not "":
                paused_video=self._video_library.get_video(paused_video_id)
                print("Currently playing:",
                      paused_video.title,
                      '(',paused_video.video_id,')',
                      '[',*paused_video.tags,'] - PAUSED')
            else:
                playing_video = self._video_library.get_video(playing_video_id)
                print("Currently playing:",
                      playing_video.title,
                      '(', playing_video.video_id, ')',
                      '[', *playing_video.tags, ']')


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print(self.playlist_library.create_playlist(playlist_name))


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print(self.playlist_library.add_to_playlist(playlist_name,video_id))

    def show_all_playlists(self):
        """Display all playlists."""
        playlists=self.playlist_library.show_playlists()
        if len(playlists) != 0:
            print("Showing all playlists")
            for keys in playlists:
                print(keys)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        videos=self.playlist_library.show_playlist(playlist_name)
        playlists=self.playlist_library.get_playlists()

        if playlist_name not in playlists:
            print("Cannot show playlist"+playlist_name+": Playlist does not exist")

        elif len(videos) ==0:
            print("Showing playlist: "+playlist_name)
            print("No videos here yet")

        elif len(videos)!= 0:
            print("Showing playlist: "+playlist_name)
            for v in videos:
                print(self._video_library.get_video(v).title+'('+ self._video_library.get_video(v).video_id+ ')'+'[',*self._video_library.get_video(v).tags,']')

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
