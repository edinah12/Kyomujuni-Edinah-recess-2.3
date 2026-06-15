print("=== 2026 FIFA World Cup Team Manager ===")


# Pre-tournament Preparation

print("\n--- Pre-Tournament Preparation ---")

activities = ["Training", "Friendly Match", "Tactical Meeting", "Recovery"]

for activity in activities:

    if activity == "Training":
        print("Team is training to improve fitness and skills")

    elif activity == "Friendly Match":
        print("Team is playing a friendly match to test tactics")

    elif activity == "Tactical Meeting":
        pass   # Future tactical instructions can be added here
        print("Tactical meeting planned")

    elif activity == "Recovery":
        print("Players are recovering before the tournament")
        continue   # Move to the next activity


print("\nPreparation completed!")

# Group Stage Matches

print("\n--- FIFA World Cup Group Stage ---")

points = 0

match = 1
while match <= 3:
    print("\nMatch", match)

    result = input("Enter match result (win/draw/loss): ").lower()

    if result == "win":
        points += 3
        print("Great! The team won (+3 points)")

    elif result == "draw":
        points += 1
        print("The match ended in a draw (+1 point)")

    elif result == "loss":
        print("The team lost (0 points)")

    else:
        print("Invalid result entered")
        match += 1
        continue   # Skip this round if input is wrong

    print("Current points:", points)

    # Qualification check
    if points >= 7:
        print("Team has qualified for the knockout stage!")
        break   # Stop playing remaining matches

    match += 1


# Final Result

print("\n=== Tournament Summary ===")

print("Final points:", points)


if points >= 7:
    print("Status: Qualified")

else:
    print("Status: Group stage completed")