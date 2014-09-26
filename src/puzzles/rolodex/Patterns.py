import re
from Entry import Entry


class Patterns(object):
    name = re.compile(r"^[A-Za-z. ]+$")
    zip = re.compile(r"^\d{5}$")  # assuming we are not accepting format 12345-6789
    phone = re.compile(r"")


class EntryFormatOne(Patterns):
    # override with special phone format
    phone = re.compile(r"^\(\d{3}\)\-\d{3}\-\d{4}$")

    def try_extract(self, text):
        entry = self.extract(text)
        if entry is not None:
            return self.normalize(entry)
        else:
            return None

    def extract(self, text):
        entry = re.split(", ", text)

        # Expecting: Lastname, Firstname, Special Phone, Color, Zip
        if (len(entry) == 5 and
            self.name.match(entry[0]) and
            self.name.match(entry[1]) and
            self.phone.match(entry[2]) and
            self.name.match(entry[3]) and
            self.zip.match(entry[4])):
            return entry
        else:
            return None

    @staticmethod
    def normalize(fields): #TODO normalize phone etc
        if len(fields) != 5:
            return None
        entry = Entry()
        entry.last_name = fields[0]
        entry.first_name = fields[1]
        entry.phone = fields[2]
        entry.color = fields[3]
        entry.zip = fields[4]
        return entry


# class EntryFormatTwo(Patterns):
#     def extract_format_two(self, text):
#         return None

