# ============================================================
# CASE DATA
# ============================================================
# This file contains the three cases used in Detective Files.
#
# LIST:
# The 'cases' variable stores all three cases in a list.
#
# DICTIONARY:
# Each case is represented using a dictionary containing
# information such as the title, suspects, culprit and
# investigation options.
#
# TUPLE:
# Each suspect is stored as a tuple containing their name
# and their role.
#
# STRINGS:
# Case descriptions, suspect statements and clues are
# represented using strings.
# ============================================================


cases = [

    # ========================================================
    # CASE 1 - THE MISSING PAINTING
    # ========================================================

    {
        "id": 101,
        "title": "The Missing Painting",
        "location": "City Museum",

        "description": """
A priceless painting called "The Blue Moon" has disappeared
from the City Museum.

The museum closed at 9:00 PM.
The painting was last seen at 8:10 PM.

Three people were still inside the museum that evening.
""",

        # TUPLES
        "suspects": [
            ("Arjun", "Museum Guard"),
            ("Rahul", "Art Dealer"),
            ("Meera", "Museum Curator")
        ],

        # The culprit is FIXED.
        "culprit": "Rahul",

        "investigations": [

            {
                "name": "Interview Arjun",
                "clue": """
Arjun says he was checking the east wing between
8:15 PM and 8:40 PM.

He remembers hearing the gallery door close around
8:30 PM, but he did not see who entered or left.
"""
            },

            {
                "name": "Interview Rahul",
                "clue": """
Rahul says he left the museum shortly after 8:00 PM
because he had another appointment.

He claims he never entered the main gallery that evening.
"""
            },

            {
                "name": "Interview Meera",
                "clue": """
Meera says she was working in her office from 8:00 PM
until 8:45 PM.

She remembers Rahul asking her earlier that day whether
the museum's security cameras were working properly.
"""
            },

            {
                "name": "Examine the Gallery",
                "clue": """
A small piece of expensive black fabric is found near
the empty painting stand.

The fabric appears to have been torn recently.
"""
            },

            {
                "name": "Check Security Records",
                "clue": """
The main entrance was not opened between 8:05 PM and
8:40 PM.

However, the staff entrance was opened once at 8:27 PM.

Only staff members and approved museum visitors could
use that entrance.
"""
            },

            {
                "name": "Check the Painting Stand",
                "clue": """
The painting stand has several fresh fingerprints.

Most are difficult to identify, but one partial print
matches a person who had previously handled the painting
during a private viewing.
"""
            },

            {
                "name": "Check the Visitor Register",
                "clue": """
Rahul's name appears in the visitor register at 7:45 PM.

His recorded departure time is missing.

The guard says he normally records every visitor's
departure time.
"""
            }
        ]
    },


    # ========================================================
    # CASE 2 - THE STOLEN LAPTOP
    # ========================================================

    {
        "id": 102,
        "title": "The Stolen Laptop",
        "location": "University Computer Laboratory",

        "description": """
A laptop containing important research data has been stolen
from the university computer laboratory.

The laboratory was locked at 9:00 PM.

The laptop was confirmed to be on the desk at 7:30 PM.

Three people had legitimate access to the laboratory.
""",

        "suspects": [
            ("Kiran", "Lab Assistant"),
            ("Vikram", "Student"),
            ("Ananya", "Research Scholar")
        ],

        "culprit": "Kiran",

        "investigations": [

            {
                "name": "Interview Kiran",
                "clue": """
Kiran says he finished his work at 7:45 PM and left
the laboratory immediately.

He claims he did not return after that.
"""
            },

            {
                "name": "Interview Vikram",
                "clue": """
Vikram says he was working on an assignment until
around 8:10 PM.

He remembers seeing someone carrying a large black bag
near the laboratory door.
"""
            },

            {
                "name": "Interview Ananya",
                "clue": """
Ananya says she left the laboratory at approximately
8:00 PM.

She says Kiran was still inside when she left.

She also mentions that Kiran knew the location of the
spare laptop keys.
"""
            },

            {
                "name": "Check Computer Logs",
                "clue": """
A computer in the laboratory was accessed at 8:17 PM.

The account used was registered to Kiran.

However, the system does not record who physically used
the computer.
"""
            },

            {
                "name": "Check CCTV",
                "clue": """
The CCTV camera shows a person leaving the laboratory
at 8:23 PM carrying a large black bag.

The person's face cannot be seen clearly.

The person appears to be wearing a dark jacket.
"""
            },

            {
                "name": "Search the Laboratory",
                "clue": """
A broken USB drive is found underneath the desk.

The drive contains a folder that was recently accessed
from the laboratory computer.
"""
            },

            {
                "name": "Check Access Records",
                "clue": """
The laboratory door was opened at 8:14 PM using an
authorized staff access card.

Student access cards cannot open the laboratory after
8:00 PM.
"""
            }
        ]
    },


    # ========================================================
    # CASE 3 - THE MISSING DIAMOND
    # ========================================================

    {
        "id": 103,
        "title": "The Missing Diamond",
        "location": "Royal Hotel",

        "description": """
A valuable diamond has disappeared from a locked hotel room.

There are no signs of forced entry.

The diamond was confirmed to be inside the room at
10:30 PM and was discovered missing at midnight.

Three people had access to the room that night.
""",

        "suspects": [
            ("Riya", "Hotel Manager"),
            ("Sameer", "Security Officer"),
            ("Dev", "Hotel Guest")
        ],

        "culprit": "Sameer",

        "investigations": [

            {
                "name": "Interview Riya",
                "clue": """
Riya says she stayed at the reception desk between
10:30 PM and midnight.

She says she did not enter the guest's room after
10:00 PM.

She also confirms that the security department
possesses a master key.
"""
            },

            {
                "name": "Interview Sameer",
                "clue": """
Sameer says he spent the entire period between
10:30 PM and midnight near the main entrance.

He claims he never went upstairs.

He says the security cameras can confirm this.
"""
            },

            {
                "name": "Interview Dev",
                "clue": """
Dev says he returned to his room at around 11:20 PM.

He remembers seeing a security officer near his floor
but could not see the person's face clearly.
"""
            },

            {
                "name": "Check Key Records",
                "clue": """
The room was opened at 11:42 PM using the hotel's
security master key.

The manager's key was not used that night.
"""
            },

            {
                "name": "Check Security Cameras",
                "clue": """
The camera near the main entrance shows Sameer leaving
the reception area at 11:35 PM.

The camera on the second floor shows a security officer
entering the hallway at 11:41 PM.

The person's face is not visible.
"""
            },

            {
                "name": "Inspect the Door",
                "clue": """
There are no signs of forced entry.

The lock was opened normally using an authorized key.

There is also a faint scratch near the inside edge
of the door.
"""
            },

            {
                "name": "Search the Security Office",
                "clue": """
A small black box is found inside a drawer in the
security office.

It contains a spare room key and a handwritten note
with the number of the guest's room.
"""
            }
        ]
    }
]