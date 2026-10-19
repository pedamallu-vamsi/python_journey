# ============================================================
# MAIN PROGRAM
# ============================================================
# This is the entry point of Detective Files.
#
# RANDOM NUMBER GENERATION:
# random.choice() randomly selects ONE of the three cases
# every time the program is executed.
#
# LIST:
# The cases imported from cases.py are stored in a list.
#
# SET:
# discovered_clues stores the investigations already completed.
#
# WHILE LOOP:
# Keeps the investigation running until the player solves
# the case or chooses to exit.
#
# IF / ELIF / ELSE:
# Controls menu choices, accusations and game decisions.
# ============================================================


import random

from cases import cases
from investigate import investigate

from utils import (
    show_case,
    show_menu,
    show_clues,
    final_result,
    get_suspect_names
)


def main():

    # ========================================================
    # RANDOM CASE SELECTION
    # ========================================================
    # Only the case is randomly selected.
    #
    # The culprit of each case is fixed in cases.py.
    # ========================================================

    case = random.choice(cases)

    # ========================================================
    # SET
    # ========================================================
    # Stores investigations that have already been completed.
    # ========================================================

    discovered_clues = set()

    investigations_done = 0
    wrong_guesses = 0

    # Display the selected case.
    show_case(case)

    # ========================================================
    # MAIN GAME LOOP
    # ========================================================

    while True:

        show_menu(
            case,
            discovered_clues
        )

        # ----------------------------------------------------
        # Get player input.
        # ----------------------------------------------------

        try:

            choice = int(
                input("\nEnter your choice: ")
            )

        except ValueError:

            print(
                "\n❌ Please enter a valid number."
            )

            continue

        investigation_count = len(
            case["investigations"]
        )

        # ====================================================
        # INVESTIGATION
        # ====================================================

        if 1 <= choice <= investigation_count:

            successful = investigate(
                case,
                choice,
                discovered_clues
            )

            # Only count a new investigation.
            if successful:

                investigations_done += 1

        # ====================================================
        # VIEW DISCOVERED CLUES
        # ====================================================

        elif choice == investigation_count + 1:

            show_clues(
                case,
                discovered_clues
            )

        # ====================================================
        # MAKE AN ACCUSATION
        # ====================================================

        elif choice == investigation_count + 2:

            suspects = get_suspect_names(case)

            print("\n" + "=" * 60)
            print("                 MAKE YOUR ACCUSATION")
            print("=" * 60)

            # FOR LOOP
            for number, suspect in enumerate(
                suspects,
                1
            ):

                print(
                    f"{number}. {suspect}"
                )

            try:

                accusation = int(
                    input(
                        "\nWho do you think is the culprit? "
                    )
                )

            except ValueError:

                print(
                    "\n❌ Please enter a valid number."
                )

                continue

            # ------------------------------------------------
            # Check whether the suspect number is valid.
            # ------------------------------------------------

            if (
                accusation < 1
                or accusation > len(suspects)
            ):

                print(
                    "\n❌ Invalid suspect choice."
                )

                continue

            accused_person = suspects[
                accusation - 1
            ]

            # =================================================
            # CORRECT ACCUSATION
            # =================================================

            if accused_person == case["culprit"]:

                final_result(
                    True,
                    investigations_done,
                    wrong_guesses
                )

                break

            # =================================================
            # WRONG ACCUSATION
            # =================================================

            else:

                wrong_guesses += 1

                print("\n❌ WRONG ACCUSATION!")

                print(
                    f"{accused_person} is innocent."
                )

                # ------------------------------------------------
                # WRONG GUESS #1
                # ------------------------------------------------

                if wrong_guesses == 1:

                    print("\n😬 WRONG AGAIN!")

                    print(
                        "You just accused an innocent person."
                    )

                    print(
                        "There are only THREE suspects, Detective."
                    )

                    print(
                        "Maybe investigate before throwing "
                        "accusations around? 💀"
                    )

                # ------------------------------------------------
                # WRONG GUESS #2
                # ------------------------------------------------

                elif wrong_guesses == 2:

                    print("\n💀 TWO WRONG GUESSES!")

                    print(
                        "You've now accused BOTH innocent suspects."
                    )

                    print(
                        "There were THREE suspects."
                    )

                    print(
                        "Congratulations... you've basically "
                        "solved the case by process of elimination. 😭"
                    )

                    print(
                        "Please don't let the police know about this."
                    )

        # ====================================================
        # EXIT
        # ====================================================

        elif choice == investigation_count + 3:

            print("\n" + "=" * 60)
            print("                 CASE ABANDONED")
            print("=" * 60)

            print(
                "\nThe culprit lives to see another day. 🕵️"
            )

            print(
                "Better luck on your next case, Detective!"
            )

            print("=" * 60)

            break

        # ====================================================
        # INVALID MENU CHOICE
        # ====================================================

        else:

            print("\n❌ Invalid choice.")

            print(
                "Please select an option from the menu."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()