from unittest import TestCase
from classes.rooms import Rooms

class TestCreatRoom(TestCase):
    def test_create_room_successfully(self):
        nrooms = Rooms()
        initial_room_count = len(nrooms.all_rooms)
        blue_office = nrooms.create_room("Blue","office")
        self.assertTrue(blue_office)
        new_room_count = len(nrooms.all_rooms)
        self.assertEqual(initial_room_count - new_room_count,1)
        return true

    def teardown(self):
        print ("TEAR DOWN!")

    def test_basic(self):
        print ("I RAN!")
