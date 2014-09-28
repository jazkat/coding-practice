import json
import unittest
from Entry import Entry

class EntryTest(unittest.TestCase):

    #######################################################
    # Entry Sort Order
    #######################################################

    def test_entry_sort(self):
        entry1 = Entry("blue", "Allison", "Zane", "555-555-1234", "12345")
        entry2 = Entry("white", "Zack", "Banks", "123-123-4567", "23456")
        entry3 = Entry("dark blue", "Zack", "Monroe", "555-123-4567", "12345")
        entry4 = Entry("white", "Zack", "Banks", "123-456-7890", "23456")
        entry5 = Entry("purple", "Hillary", "Banks", "555-123-1234", "56789")
        entries = [entry1, entry2, entry3, entry4, entry5]
        entries = sorted(entries)

        self.assertEqual(entry5, entries[0])  # Banks, Hillary
        self.assertTrue(entries[1] == entry2 or entries[1] == entry4)  # Banks, Zack
        self.assertTrue(entries[2] == entry2 or entries[2] == entry4)  # Banks, Zack
        self.assertNotEqual(entries[1].phone, entries[2].phone)
        self.assertTrue(entry3, entries[3])  # Monroe, Zack
        self.assertTrue(entry1, entries[4])  # Zane, Allison

    #######################################################
    # Entry To Json
    #######################################################

    def test_entry_json_prep(self):
        entry1 = Entry("blue", "Allison", "Zane", "555-555-1234", "12345")
        entry2 = Entry("dark blue", "Zack", "Monroe", "555-123-4567", "12345")
        entries = map(Entry.json_prep, [entry2, entry1])
        output = json.dumps(entries, indent=2, sort_keys=True)
        expected = "[\n" + \
                    "  {\n" + \
                    "    \"color\": \"dark blue\", \n" + \
                    "    \"firstname\": \"Zack\", \n" + \
                    "    \"lastname\": \"Monroe\", \n" + \
                    "    \"phonenumber\": \"555-123-4567\", \n" + \
                    "    \"zipcode\": \"12345\"\n" + \
                    "  }, \n" + \
                    "  {\n" + \
                    "    \"color\": \"blue\", \n" + \
                    "    \"firstname\": \"Allison\", \n" + \
                    "    \"lastname\": \"Zane\", \n" + \
                    "    \"phonenumber\": \"555-555-1234\", \n" + \
                    "    \"zipcode\": \"12345\"\n" + \
                    "  }\n" + \
                    "]"

        self.assertEqual(expected, output)
