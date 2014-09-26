import unittest
from Patterns import Patterns, EntryFormatOne


class PatternTest(unittest.TestCase):

    def test_name_pattern1(self):
        first_name = "Jazmine"
        last_name = "James"

        self.assertTrue(Patterns().name.match(first_name))
        self.assertTrue(Patterns().name.match(last_name))

    def test_name_pattern2(self):
        name = "Jazmine James"

        self.assertTrue(Patterns().name.match(name))

    def test_name_pattern3(self):
        name = "J.M. James"

        self.assertTrue(Patterns().name.match(name))

    def test_name_pattern4(self):
        name = "Jazmine M. James"

        self.assertTrue(Patterns().name.match(name))

    def test_name_pattern_doesnt_match_non_names1(self):
        numbers = "12345"

        self.assertFalse(Patterns().name.match(numbers))

    def test_name_pattern_doesnt_match_non_names2(self):
        robot_name = "J4zm1ne J4m3s"

        self.assertFalse(Patterns().name.match(robot_name))

    def test_name_pattern_not_case_sensitive(self):
        lowercase_name = "jazmine james"

        self.assertTrue(Patterns().name.match(lowercase_name))

    def test_zip_pattern1(self):
        zip_code = "12345"

        self.assertTrue(Patterns().zip.match(zip_code))

    def test_zip_pattern_doesnt_match_non_zips1(self):
        too_many_numbers = "123456"

        self.assertFalse(Patterns().zip.match(too_many_numbers))

    def test_zip_pattern_doesnt_match_non_zips2(self):
        too_few_numbers = "1234"

        self.assertFalse(Patterns().zip.match(too_few_numbers))

    def test_zip_pattern_doesnt_match_non_zips3(self):
        illegal_chars1 = "123-4"
        illegal_chars2 = "1234-5"

        self.assertFalse(Patterns().zip.match(illegal_chars1))
        self.assertFalse(Patterns().zip.match(illegal_chars2))

    def test_zip_pattern_doesnt_match_non_zips4(self):
        alphanumeric = "123a4"

        self.assertFalse(Patterns().zip.match(alphanumeric))

    def test_special_phone_pattern(self):
        number = "(623)-668-9293"

        self.assertTrue(EntryFormatOne().phone.match(number))

    def test_matches_first_format_extracted(self):
        entry = "Chandler, Kerri, (623)-668-9293, pink, 12312"
        expected = ["Chandler", "Kerri", "(623)-668-9293", "pink", "12312"]

        result = EntryFormatOne().extract(entry)
        self.assertIsNotNone(result)
        self.assertListEqual(expected, result)

    def test_invalid_first_format_rejected1(self):
        self.assertIsNone(EntryFormatOne().extract(""))

    def test_invalid_first_format_rejected2(self):
        invalid = "Chandler, Kerri"
        self.assertIsNone(EntryFormatOne().extract(invalid))

    def test_invalid_first_format_rejected3(self):
        invalid = "Chandler, Kerri, (623)-668-9293, pink, 123123121"
        self.assertIsNone(EntryFormatOne().extract(invalid))

    def test_invalid_first_format_rejected4(self):
        invalid = "lksjdkfjdkjf"
        self.assertIsNone(EntryFormatOne().extract(invalid))

    def test_invalid_first_format_rejected5(self):
        invalid = "Chandler, Kerri, (623)-668-9293, pink, 12312, blue"
        self.assertIsNone(EntryFormatOne().extract(invalid))

    # def test_matches_second_format(self):
    #     entry = "James Murphy, yellow, 83880, 018 154 6474"
    #     expected = ["James", "Murphy", "yellow", "83880", "018 154 6474"]
    #
    #     self.assertIsNotNone()


if __name__ == '__main__':
    unittest.main()
