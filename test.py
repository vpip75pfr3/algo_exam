from unittest import TestCase
from main import confirm_rent, sort_list


class Working_With_main_Test(TestCase):
    def test_confirm_rent_1(self):
        rent_list_ = [(10, 11), (12, 19), (18, 22)]
        self.assertEqual(confirm_rent(rent_list_), False)

    def test_confirm_rent_2(self):
        rent_list_ = [(10, 11), (12, 13), (13, 14)]
        self.assertEqual(confirm_rent(rent_list_), True)

    def test_confirm_rent_3(self):
        rent_list_ = []
        self.assertEqual(confirm_rent(rent_list_), True)

    def test_sort_list_4(self):
        old_list_ = [21, 22, 19, 21]
        self.assertEqual(sort_list(old_list_), [19, 21, 21, 22])

    def test_sort_list_5(self):
        old_list_ = [13, 20, 22, 14]
        self.assertEqual(sort_list(old_list_), [13, 14, 20, 22])