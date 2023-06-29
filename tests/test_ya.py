from unittest import TestCase
import ya



class TestYandex(TestCase):
    def test_crate_folder(self):
        self.assertEqual(ya.yandex.create_folder('test'), 201, "folder created")

    def test_crate_folder_fail(self):
        self.assertEqual(ya.yandex.create_folder('test'), 201, "folder not created")
