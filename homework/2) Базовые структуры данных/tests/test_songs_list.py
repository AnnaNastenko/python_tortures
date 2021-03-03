#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
import songs_list


class TestSongs(unittest.TestCase):

    def _search_inside_list(self, song_name: str, validator_songs_list=songs_list.violator_songs_list) -> float:
        song_name = song_name
        for song_row in validator_songs_list:
            if song_name in song_row:
                break
        song_duration = float(song_row[1])
        return song_duration

    def _search_inside_dict(self, song_name: str, violator_songs_dict=songs_list.violator_songs_dict) -> float:
        song_name = song_name
        song_duration = float(violator_songs_dict[song_name])
        return song_duration

    def test_sum1(self):
        songs = ['Halo', 'Enjoy the Silence', 'Clean']
        answer = sum((self._search_inside_list(song) for song in songs))
        self.assertAlmostEqual(answer, songs_list.sum1, msg=f"{songs}", places=1)

    def test_sum2(self):
        songs = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
        answer = sum((self._search_inside_dict(song) for song in songs))
        self.assertAlmostEqual(answer, songs_list.sum2, msg=f"{songs}", places=1)


if __name__ == "__main__":
    unittest.main()
