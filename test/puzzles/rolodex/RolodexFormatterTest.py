import json
import unittest
from RolodexFormatter import RolodexFormatter as Formatter
from Entry import Entry


class RolodexFormatterTest(unittest.TestCase):

    ################################
    # Pattern Matching - Name
    ###############################

    def test_name_pattern1(self):
        first = "Jazmine"
        last = "James"

        self.assertTrue(Formatter().name.match(first))
        self.assertTrue(Formatter().name.match(last))

    def test_name_pattern2(self):
        name = "J. M. James"

        self.assertTrue(Formatter().name.match(name))

    def test_name_pattern3(self):
        name = "Jazmine M James"

        self.assertTrue(Formatter().name.match(name))

    def test_name_pattern4(self):
        color = "blue"

        self.assertTrue(Formatter().name.match(color))

    def test_name_pattern_doesnt_match_non_name1(self):
        numbers = "12345"

        self.assertFalse(Formatter().name.match(numbers))

    def test_name_pattern_doesnt_match_non_name2(self):
        robot_name = "J4zm1ne J4m3s"

        self.assertFalse(Formatter().name.match(robot_name))

    def test_name_pattern_doesnt_match_non_name3(self):
        phone = "555-555-1234"

        self.assertFalse(Formatter().name.match(phone))

    ###############################
    # Pattern Matching - Zip
    ###############################

    def test_zip_pattern1(self):
        zip_code = "12345"

        self.assertTrue(Formatter().zip.match(zip_code))

    def test_zip_pattern_doesnt_match_non_zip1(self):
        too_long = "123456"

        self.assertFalse(Formatter().zip.match(too_long))

    def test_zip_pattern_doesnt_match_non_zip2(self):
        too_short = "1234"

        self.assertFalse(Formatter().zip.match(too_short))

    def test_zip_pattern_doesnt_match_non_zip3(self):
        not_valid = "123-4" # correct length but invalid

        self.assertFalse(Formatter().zip.match(not_valid))

    def test_zip_pattern_doesnt_match_non_zip4(self):
        not_valid = "1234-5" # correct number of digits but invalid

        self.assertFalse(Formatter().zip.match(not_valid))

    def test_zip_pattern_doesnt_match_non_zip5(self):
        alpha_numeric = "123a4"

        self.assertFalse(Formatter().zip.match(alpha_numeric))

    #######################################################
    # Pattern Matching - Phone with Formatting
    #######################################################

    def test_formatted_phone_pattern1(self):
        number = "(123)-456-7890"

        self.assertTrue(Formatter().formatted_phone.match(number))

    def test_formatted_phone_pattern_doesnt_match_wrong_format1(self):
        alpha_numeric = "(555)-555-123b"

        self.assertFalse(Formatter().formatted_phone.match(alpha_numeric))

    def test_formatted_phone_pattern_doesnt_match_wrong_format2(self):
        wrong_format = "123-456-7890"

        self.assertFalse(Formatter().formatted_phone.match(wrong_format))

    def test_formatted_phone_pattern_doesnt_match_wrong_format3(self):
        wrong_format = "123 456 7890"

        self.assertFalse(Formatter().formatted_phone.match(wrong_format))

    def test_formatted_phone_pattern_doesnt_match_wrong_format4(self):
        wrong_format = "(123) 456 7890"

        self.assertFalse(Formatter().formatted_phone.match(wrong_format))

    def test_formatted_phone_pattern_doesnt_match_wrong_format5(self):
        wrong_format = "(123)-456 7890"

        self.assertFalse(Formatter().formatted_phone.match(wrong_format))

    def test_formatted_phone_pattern_doesnt_match_wrong_format6(self):
        wrong_format = "(123) 456-7890"

        self.assertFalse(Formatter().formatted_phone.match(wrong_format))

    def test_formatted_phone_pattern_doesnt_match_wrong_format7(self):
        too_short = "(123)-456-789"

        self.assertFalse(Formatter().formatted_phone.match(too_short))

    def test_formatted_phone_pattern_doesnt_match_wrong_format8(self):
        too_long = "(123)-456-78900"

        self.assertFalse(Formatter().formatted_phone.match(too_long))

    def test_formatted_phone_pattern_doesnt_match_wrong_format9(self):
        too_long = "1(123)-456-7890"

        self.assertFalse(Formatter().formatted_phone.match(too_long))

    def test_formatted_phone_pattern_doesnt_match_wrong_format10(self):
        zip_code = "12345"

        self.assertFalse(Formatter().formatted_phone.match(zip_code))

    #######################################################
    # Pattern Matching - Phone without Formatting
    #######################################################

    def test_phone_pattern1(self):
        number = "555 123 4567"

        self.assertTrue(Formatter().phone.match(number))

    def test_phone_pattern_doesnt_match_wrong_format1(self):
        wrong_format = "(123)-456-7890"

        self.assertFalse(Formatter().phone.match(wrong_format))

    def test_phone_pattern_doesnt_match_wrong_format2(self):
        wrong_format = "555-555-1234"

        self.assertFalse(Formatter().phone.match(wrong_format))

    def test_phone_pattern_doesnt_match_wrong_format3(self):
        wrong_format = "(555) 123 4567"

        self.assertFalse(Formatter().phone.match(wrong_format))

    def test_phone_pattern_doesnt_match_wrong_format4(self):
        too_short = "555 123 456"

        self.assertFalse(Formatter().phone.match(too_short))

    def test_phone_pattern_doesnt_match_wrong_format5(self):
        too_long = "555 123 45678"

        self.assertFalse(Formatter().phone.match(too_long))

    def test_phone_pattern_doesnt_match_wrong_format6(self):
        too_long = "1234 567 1234"

        self.assertFalse(Formatter().phone.match(too_long))

    def test_phone_pattern_doesnt_match_wrong_format7(self):
        alpha_numeric = "555 123 456a"

        self.assertFalse(Formatter().phone.match(alpha_numeric))

    def test_phone_pattern_doesnt_match_wrong_format8(self):
        zip_code = "12345"

        self.assertFalse(Formatter().phone.match(zip_code))

    #######################################################
    # Normalize Name
    #######################################################

    def test_normalize_name1(self):
        name = "Jazmine James"
        expected = ["Jazmine", "James"]

        self.assertListEqual(expected, Formatter.normalize_split_name(name))

    def test_normalize_name2(self):
        name = "J.M. James"
        expected = ["J.M.", "James"]

        self.assertListEqual(expected, Formatter.normalize_split_name(name))

    def test_normalize_name3(self):
        name = "Jazmine M James"
        expected = ["Jazmine M", "James"]

        self.assertListEqual(expected, Formatter.normalize_split_name(name))

    def test_normalize_invalid_name_doesnt_have_two_elts(self):
        invalid = "Jaz"
        expected = ["Jaz"]

        self.assertListEqual(expected, Formatter.normalize_split_name(invalid))

    #######################################################
    # Normalize Phone
    #######################################################

    def test_normalize_phone(self):
        number = "555 123 4567"
        expected = "555-123-4567"

        self.assertEqual(expected, Formatter.normalize_phone(number))

    #######################################################
    # Normalize Formatted Phone
    #######################################################

    def test_normalize_formatted_phone(self):
        number = "(555)-123-4567"
        expected = "555-123-4567"

        self.assertEqual(expected, Formatter.normalize_formatted_phone(number))

    #######################################################
    # Normalize Entry - Format One
    #######################################################

    def test_normalize_format_one(self):
        entry = ["Lastname", "Firstname", "(703)-742-0996", "Blue", "10013"]
        result = Formatter().normalize_format_one(entry)

        self.assertIsNotNone(result)
        self.assertEqual("Firstname", result.first_name)
        self.assertEqual("Lastname", result.last_name)
        self.assertEqual("703-742-0996", result.phone)
        self.assertEqual("Blue", result.color)
        self.assertEqual("10013", result.zip)

    def test_normalize_invalid_format_one1(self):
        missing_lastname = ["Firstname Lastname", "(703)-742-0996", "Blue", "10013"]
        result = Formatter().normalize_format_one(missing_lastname)

        self.assertIsNone(result)

    def test_normalize_invalid_format_one2(self):
        invalid = ["Chandler", "Kerri", "(623)-668-9293", "pink", "123123121"]
        result = Formatter().normalize_format_one(invalid)

        self.assertIsNone(result)

    #######################################################
    # Normalize Entry - Format Two
    #######################################################

    def test_normalize_format_two1(self):
        entry = ["Firstname Lastname", "Red", "11237", "703 955 0373"]
        result = Formatter().normalize_format_two(entry)

        self.assertIsNotNone(result)
        self.assertEqual("Firstname", result.first_name)
        self.assertEqual("Lastname", result.last_name)
        self.assertEqual("Red", result.color)
        self.assertEqual("11237", result.zip)
        self.assertEqual("703-955-0373", result.phone)

    def test_normalize_format_two2(self):
        entry = ["J M James", "Red", "11237", "703 955 0373"]
        result = Formatter().normalize_format_two(entry)

        self.assertIsNotNone(result)
        self.assertEqual("J M", result.first_name)
        self.assertEqual("James", result.last_name)
        self.assertEqual("Red", result.color)
        self.assertEqual("11237", result.zip)
        self.assertEqual("703-955-0373", result.phone)

    def test_normalize_invalid_format_two1(self):
        too_many = ["Firstname", "Lastname", "Red", "11237", "703 955 0373"]
        result = Formatter().normalize_format_two(too_many)

        self.assertIsNone(result)

    def test_normalize_invalid_format_two2(self):
        missing_last_name = ["TheArtistFormerlyKnownAsPrince", "Red", "11237", "703 955 0373"]
        result = Formatter().normalize_format_two(missing_last_name)

        self.assertIsNone(result)

    def test_normalize_invalid_format_two3(self):
        invalid_phone = ["Firstname Lastname", "Red", "11237", "703-955-0373"]
        result = Formatter().normalize_format_two(invalid_phone)

        self.assertIsNone(result)

    #######################################################
    # Normalize Entry - Format Three
    #######################################################

    def test_normalize_format_three(self):
        entry = ["Firstname", "Lastname", "10013", "646 111 0101", "Green"]
        result = Formatter().normalize_format_three(entry)

        self.assertIsNotNone(result)
        self.assertEqual("Firstname", result.first_name)
        self.assertEqual("Lastname", result.last_name)
        self.assertEqual("10013", result.zip)
        self.assertEqual("646-111-0101", result.phone)
        self.assertEqual("Green", result.color)

    def test_normalize_invalid_format_three1(self):
        too_short = ["Firstname Lastname", "10013", "646 111 0101", "Green"]
        result = Formatter().normalize_format_three(too_short)

        self.assertIsNone(result)

    def test_normalize_invalid_format_three2(self):
        invalid_phone = ["Firstname", "Lastname", "10013", "(646)-111-0101", "Green"]
        result = Formatter().normalize_format_three(invalid_phone)

        self.assertIsNone(result)

    def test_normalize_invalid_format_three3(self):
        wrong_order = ["Firstname", "Lastname", "646 111 0101", "10013", "Green"]
        result = Formatter().normalize_format_three(wrong_order)

        self.assertIsNone(result)

    #######################################################
    # Parse Line
    #######################################################

    def test_parse_line1(self):
        line = "Booker T., Washington, 87360, 373 781 7380, yellow"
        formatter = Formatter()
        formatter.parse_line(line, 0)
        expected = Entry("yellow", "Booker T.", "Washington", "373-781-7380", "87360")

        self.assertListEqual([expected], formatter.entries)
        self.assertListEqual([], formatter.errors)

    def test_parse_line2(self):
        line = "Chandler, Kerri, (623)-668-9293, pink, 123123121"
        formatter = Formatter()
        formatter.parse_line(line, 1)

        self.assertListEqual([], formatter.entries)
        self.assertListEqual([1], formatter.errors)

    def test_parse_line3(self):
        line = "James Murphy, yellow, 83880, 018 154 6474"
        formatter = Formatter()
        formatter.parse_line(line, 2)
        expected = Entry("yellow", "James", "Murphy", "018-154-6474", "83880")

        self.assertListEqual([expected], formatter.entries)
        self.assertListEqual([], formatter.errors)

    def test_parse_line4(self):
        line = "asdfawefawea"
        formatter = Formatter()
        formatter.parse_line(line, 3)

        self.assertListEqual([], formatter.entries)
        self.assertListEqual([3], formatter.errors)

    def test_parse_line5(self):
        line = "Chandler, Kerri, (623)-668-9293, pink, 12312"
        formatter = Formatter()
        formatter.parse_line(line, 4)
        expected = Entry("pink", "Kerri", "Chandler", "623-668-9293", "12312")

        self.assertListEqual([expected], formatter.entries)
        self.assertListEqual([], formatter.errors)

    def test_parse_line6(self):
        line0 = "Booker T., Washington, 87360, 373 781 7380, yellow"
        line1 = "Chandler, Kerri, (623)-668-9293, pink, 123123121"
        line2 = "James Murphy, yellow, 83880, 018 154 6474"
        line3 = "asdfawefawea"
        line4 = "Chandler, Kerri, (623)-668-9293, pink, 12312"

        formatter = Formatter()
        formatter.parse_line(line0, 0)
        formatter.parse_line(line1, 1)
        formatter.parse_line(line2, 2)
        formatter.parse_line(line3, 3)
        formatter.parse_line(line4, 4)

        expected0 = Entry("yellow", "Booker T.", "Washington", "373-781-7380", "87360")
        expected2 = Entry("yellow", "James", "Murphy", "018-154-6474", "83880")
        expected4 = Entry("pink", "Kerri", "Chandler", "623-668-9293", "12312")
        expected = [expected0, expected2, expected4]

        self.assertListEqual(expected, formatter.entries)
        self.assertListEqual([1,3], formatter.errors)

    #######################################################
    # Format
    #######################################################

    def test_format(self):
        in_data = ["Booker T., Washington, 87360, 373 781 7380, yellow",
                   "Chandler, Kerri, (623)-668-9293, pink, 123123121",
                   "James Murphy, yellow, 83880, 018 154 6474",
                   "asdfawefawea"]
        formatter = Formatter()
        result = json.dumps(formatter.format_rolodex(in_data), sort_keys=True)
        expected = """{"entries": [""" + \
        """{"color": "yellow", "firstname": "James", "lastname": "Murphy", """ + \
        """"phonenumber": "018-154-6474", "zipcode": "83880"}, """ + \
        """{"color": "yellow", "firstname": "Booker T.", "lastname": "Washington", """ + \
        """"phonenumber": "373-781-7380", "zipcode": "87360"}], """ + \
        """"errors": [1, 3]}"""

        self.assertEqual(expected, result)

    #######################################################
    # Extract
    #######################################################

    def test_extract(self):
        formatter = Formatter()
        formatter.extract("rolodex_test1.txt")
        with open("result.out") as result:
            actual = result.read()
        with open("expected.out") as expected_result:
            expected = expected_result.read()

        self.assertEqual(expected, actual)
