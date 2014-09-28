import json
import os, errno
import re
import string
from Entry import Entry


class RolodexFormatter(object):
    """A class for parsing and formatting contacts from a rolodex."""

    outfile = 'result.out'
    name = re.compile(r"^[A-Za-z. ]+$")
    zip = re.compile(r"^\d{5}$")
    phone = re.compile(r"^\d{3} \d{3} \d{4}$")
    formatted_phone = re.compile(r"^\(\d{3}\)\-\d{3}\-\d{4}$")

    def __init__(self):
        self.entries = []
        self.errors = []

    def extract(self, filename):
        with open(filename) as f:
            data = f.read().splitlines()
        output = self.format_rolodex(data)
        self.remove(self.outfile)
        with open(self.outfile, 'w') as out:
            json.dump(output, out, indent=2, sort_keys=True)

    @staticmethod
    def remove(filename):
        try:
            os.remove(filename)
        except OSError as e:
            if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
                raise  # re-raise exception if a different error occured

    def format_rolodex(self, in_data):
        line_num = 0
        for line in in_data:
            self.parse_line(line, line_num)
            line_num += 1
        self.entries = sorted(self.entries)
        self.entries = map(Entry.json_prep, self.entries)
        return self.get_json()

    def get_json(self):
        return {'entries': self.entries, 'errors': self.errors}

    def parse_line(self, line, num):
        entry = string.split(line, ", ")
        normalized = None
        if len(entry) == 4:
            normalized = self.normalize_format_two(entry)
        if len(entry) == 5:
            if self.zip.match(entry[2]):
                normalized = self.normalize_format_three(entry)
            elif self.formatted_phone.match(entry[2]):
                normalized = self.normalize_format_one(entry)

        if normalized is not None:
            self.entries.append(normalized)
        else:
            self.errors.append(num)

    # Methods for validating and normalizing entries in rolodex

    # Expecting: Lastname, Firstname, Formatted Phone, Color, Zip
    def normalize_format_one(self, fields):
        # Some of these may have been checked by caller, but
        # fairly cheap check so let's not make assumptions
        if (len(fields) != 5 or
            not self.name.match(fields[0]) or
            not self.name.match(fields[1]) or
            not self.formatted_phone.match(fields[2]) or
            not self.name.match(fields[3]) or
            not self.zip.match(fields[4])):
            return None
        entry = Entry()
        entry.last_name = fields[0]
        entry.first_name = fields[1]
        entry.phone = self.normalize_formatted_phone(fields[2])
        entry.color = fields[3]
        entry.zip = fields[4]
        return entry

    # Expecting: Firstname Lastname, Color, Zip, Phone
    def normalize_format_two(self, fields):
        if (len(fields) != 4 or
            not self.name.match(fields[0]) or
            not self.name.match(fields[1]) or
            not self.zip.match(fields[2]) or
            not self.phone.match(fields[3])):
            return None
        entry = Entry()
        names = self.normalize_split_name(fields[0])
        if len(names) != 2:
            return None
        entry.first_name = names[0]
        entry.last_name = names[1]
        entry.color = fields[1]
        entry.zip = fields[2]
        entry.phone = self.normalize_phone(fields[3])
        return entry

    # Expecting: Firstname, Lastname, Zip, Phone, Color
    def normalize_format_three(self, fields):
        if (len(fields) != 5 or
            not self.name.match(fields[0]) or
            not self.name.match(fields[1]) or
            not self.zip.match(fields[2]) or
            not self.phone.match(fields[3]) or
            not self.name.match(fields[4])):
            return None
        entry = Entry()
        entry.first_name = fields[0]
        entry.last_name = fields[1]
        entry.zip = fields[2]
        entry.phone = self.normalize_phone(fields[3])
        entry.color = fields[4]
        return entry

    # Methods for normalizing fields in rolodex entries

    @staticmethod
    def normalize_phone(number):
        return string.replace(number, " ", "-")

    @staticmethod
    def normalize_formatted_phone(number):
        return number[1:4] + number[5:]

    @staticmethod
    def normalize_split_name(name):
        return string.rsplit(name, " ", 1)

if __name__ == "__main__":
    import sys
    formatter = RolodexFormatter()
    formatter.extract(sys.argv[1])