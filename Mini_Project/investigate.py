# ============================================================
# INVESTIGATION MODULE
# ============================================================
# This module handles all investigation activities.
#
# SET:
# discovered_clues stores the investigations already
# completed by the detective.
#
# STRINGS:
# Investigation names and clue descriptions are strings.
#
# IF / ELSE:
# Used to check whether an investigation is valid or
# has already been completed.
# ============================================================


def investigate(case, choice, discovered_clues):

    investigations = case["investigations"]

    # Check whether the selected investigation exists.
    if choice < 1 or choice > len(investigations):

        print("\n❌ Invalid investigation choice.")

        return False

    investigation = investigations[choice - 1]

    investigation_name = investigation["name"]
    clue = investigation["clue"]

    # --------------------------------------------------------
    # Check whether this investigation has already been done.
    # --------------------------------------------------------

    if investigation_name in discovered_clues:

        print("\n🔎 You already investigated this.")
        print("There is nothing new to discover here.")

        return False

    # Add the investigation to the set.
    discovered_clues.add(investigation_name)

    print("\n" + "=" * 60)
    print("                 🔎 INVESTIGATION")
    print("=" * 60)

    print(f"\nYou decided to: {investigation_name}")

    print("\n💡 CLUE FOUND:")
    print(clue)

    print("\n" + "=" * 60)

    return True