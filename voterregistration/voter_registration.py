# Predefined list of valid candidates
CANDIDATES = ["Bill Nye", "Bob Belcher", "Kenny McCormick"]

# List to store all registered voter dictionaries
voters = []


def register_voter():
    """Collect and validate voter info, then store it in the voters list."""
    print("\n[ Register New Voter ]")

    # --- Age Validation ---
    while True:
        age_input = input("How old are you? (must be 18-120): ").strip()
        if not age_input:
            print("Age can't be blank - please try again.")
        elif not age_input.isdigit():
            print("That doesn't look like a number. Whole numbers only.")
        elif not (18 <= int(age_input) <= 120):
            print("You'll have to wait a few more years to vote.")
        else:
            age = int(age_input)
            break

    # --- Candidate Choice Validation ---
    print(f"Candidates on the ballot: {', '.join(CANDIDATES)}")
    while True:
        candidate = input("Who are you voting for? ").strip()
        if not candidate:
            print("You have to pick a candidate from the list.")
        elif candidate not in CANDIDATES:
            print(f"Not a valid candidate. Pick one of: {', '.join(CANDIDATES)}")
        else:
            break

    # --- Voter ID Validation ---
    while True:
        voter_id = input("Enter your Voter ID (letters and numbers only, no spaces): ").strip()
        if not voter_id:
            print("Voter ID can't be empty.")
        elif not voter_id.isalnum():
            print("Voter ID has to be alphanumeric -- no special characters or spaces.")
        elif any(v["voter_id"] == voter_id for v in voters):
            print("That ID's already taken. Use a different one.")
        else:
            break

    # Build the voter record and add it to the list
    voter_record = {
        "voter_id": voter_id,
        "age": age,
        "candidate": candidate
    }
    voters.append(voter_record)
    print(f"\nGot it -- voter '{voter_id}' is registered.")


def display_all_voters():
    """Print every registered voter."""
    print("\n[ All Registered Voters ]")
    if not voters:
        print("Nobody's registered yet.")
        return
    for i, voter in enumerate(voters, start=1):
        print(f"\n  #{i}")
        print(f"    Voter ID  : {voter['voter_id']}")
        print(f"    Age       : {voter['age']}")
        print(f"    Candidate : {voter['candidate']}")


def search_voter():
    """Look up a voter by their ID."""
    print("\n[ Search by Voter ID ]")
    search_id = input("Enter the Voter ID to look up: ").strip()
    for voter in voters:
        if voter["voter_id"] == search_id:
            print(f"\nFound them:")
            print(f"  Voter ID  : {voter['voter_id']}")
            print(f"  Age       : {voter['age']}")
            print(f"  Candidate : {voter['candidate']}")
            return
    print(f"No voter found with ID '{search_id}'.")


def main():
    """Main menu -- runs the whole program."""
    print("=== Voting Registration System ===")
    while True:
        print("\nWhat do you want to do?")
        print("  1. Register a new voter")
        print("  2. Show all registered voters")
        print("  3. Search for a voter by ID")
        print("  4. Exit")

        choice = input("Pick an option (1-4): ").strip()

        if choice == "1":
            register_voter()
        elif choice == "2":
            display_all_voters()
        elif choice == "3":
            search_voter()
        elif choice == "4":
            print("\nWrapping up -- here's everyone who registered:")
            display_all_voters()
            print("\nDone.")
            break
        else:
            print("That's not a valid option. Enter a number 1 through 4.")


# Run it
main()
