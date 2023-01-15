import questionary

answer = questionary.text("Is cereal soup?").ask()

message = "Try again"

if answer == 'yes':
    message = "Great job!"

print(message)
