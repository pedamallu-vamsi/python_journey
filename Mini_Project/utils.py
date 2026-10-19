# ============================================================
# UTILITY MODULE
# ============================================================
# This module contains helper functions used throughout
# Detective Files.
#
# LAMBDA:
# A lambda function is used to calculate the detective score.
#
# LIST:
# Used when extracting suspect names.
#
# FOR LOOP:
# Used to display suspects, investigations and clues.
#
# IF / ELIF / ELSE:
# Used for menu status, detective ratings and witty messages.
# ============================================================


def show_case(case):

    print("\n")
    print("=" * 60)
    print("                 🕵️ DETECTIVE FILES")
    print("=" * 60)

    print(f"\nCASE #{case['id']}: {case['title']}")
    print(f"Location: {case['location']}")

    print("\n" + case["description"])

    print("\nSUSPECTS:")

    # FOR LOOP
    for number, suspect in enumerate(case["suspects"], 1):

        name, role = suspect

        print(f"{number}. {name} - {role}")

    print("\n" + "=" * 60)


def show_menu(case, discovered_clues):

    print("\n" + "-" * 60)
    print("                    INVESTIGATION MENU")
    print("-" * 60)

    # FOR LOOP
    for number, investigation in enumerate(
        case["investigations"],
        1
    ):

        # IF / ELSE
        if investigation["name"] in discovered_clues:
            status = "✓"
        else:
            status = " "

        print(
            f"{number}. [{status}] "
            f"{investigation['name']}"
        )

    investigation_count = len(case["investigations"])

    print(
        f"{investigation_count + 1}. "
        "View discovered clues"
    )

    print(
        f"{investigation_count + 2}. "
        "Make an accusation"
    )

    print(
        f"{investigation_count + 3}. "
        "Exit"
    )

    print("-" * 60)


def show_clues(case, discovered_clues):

    print("\n" + "=" * 60)
    print("                 🔎 DISCOVERED CLUES")
    print("=" * 60)

    # IF
    if not discovered_clues:

        print("\nYou haven't discovered any clues yet.")
        print("Start investigating!")

        print("=" * 60)

        return

    clue_number = 1

    # FOR LOOP
    for investigation in case["investigations"]:

        if investigation["name"] in discovered_clues:

            print(
                f"\n{clue_number}. "
                f"{investigation['name']}"
            )

            print(
                f"   {investigation['clue']}"
            )

            clue_number += 1

    print("\n" + "=" * 60)


def final_result(correct, investigations, wrong_guesses):

    print("\n" + "=" * 60)

    # ========================================================
    # CORRECT ACCUSATION
    # ========================================================

    if correct:

        print("                 🎉 CASE SOLVED!")
        print("=" * 60)

        print("\nCongo, Detective! 🔎")

        # ----------------------------------------------------
        # LAMBDA FUNCTION
        # ----------------------------------------------------
        # Score starts at 100.
        #
        # Every investigation costs 5 points.
        # Every wrong accusation costs 40 points.
        #
        # max() prevents the score from becoming negative.
        # ----------------------------------------------------

        score = lambda x, y: max(
            0,
            100 - (x * 3) - (y * 40)
        )

        detective_score = score(
            investigations,
            wrong_guesses
        )

        print(f"\nInvestigations : {investigations}")
        print(f"Wrong guesses  : {wrong_guesses}")
        print(f"Detective Score: {detective_score}/100")

        print("\n" + "-" * 60)

        # ====================================================
        # WITTY PERFORMANCE COMMENTS
        # ====================================================

        if wrong_guesses == 0:

            if investigations <= 3:

                print("🧠 SHERLOCK MODE ACTIVATED.")
                print(
                    "First guess. Barely any investigation."
                )
                print(
                    "You solved this before the culprit"
                )
                print(
                    "even had time to panic. 🔥"
                )

            elif investigations <= 5:

                print("😎 Excellent work, Detective!")

                print(
                    "You gathered enough evidence"
                )

                print(
                    "and got the culprit on your first guess."
                )

            else:

                print("👏 Case solved!")

                print(
                    "You got the culprit on your first guess."
                )

                print(
                    "You did investigate a LOT though..."
                )

                print(
                    "Were you solving a crime or writing a thesis? 💀"
                )

        elif wrong_guesses == 1:

            print("😬 You solved it... but barely.")

            print(
                "You accused ONE innocent person"
            )

            print(
                "before finally figuring it out."
            )

            print(
                "There were only three suspects, Detective. 💀"
            )

            print(
                "Maybe use those clues next time?"
            )

        elif wrong_guesses == 2:

            print("💀 CASE SOLVED... SOMEHOW.")

            print(
                "You accused TWO innocent people."
            )

            print(
                "There were THREE suspects."
            )

            print(
                "At that point, you had practically"
            )

            print(
                "eliminated everyone except the culprit. 😭"
            )

            print(
                "The investigation department is concerned."
            )

        # ====================================================
        # DETECTIVE RATING
        # ====================================================

        print("\nDetective Rating: ", end="")

        if detective_score >= 90:

            print("★★★★★")

        elif detective_score >= 75:

            print("★★★★☆")

        elif detective_score >= 50:

            print("★★★☆☆")

        elif detective_score >= 25:

            print("★★☆☆☆")

        else:

            print("★☆☆☆☆")

        print("=" * 60)

    # ========================================================
    # CASE ABANDONED
    # ========================================================

    else:

        print("                 ❌ CASE ABANDONED")
        print("=" * 60)

        print("\nThe culprit lives to see another day. 🕵️")

        print(
            "You gave up before solving the case."
        )

        print("=" * 60)


def get_suspect_names(case):

    # ========================================================
    # LIST
    # ========================================================
    # Extract suspect names into a separate list.
    # ========================================================

    names = []

    for suspect in case["suspects"]:

        names.append(suspect[0])

    return names