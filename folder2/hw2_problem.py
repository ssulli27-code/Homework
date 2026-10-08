def available_time(start_time, end_time):
    return end_time - start_time


def can_attend(available_hours, event_length):
    if available_hours >= event_length:
        return True
    else:
        return False


if __name__ == "__main__":
    start_time = int(input("What time are you free? "))
    end_time = int(input("What time do you need to leave? "))
    event_length = int(input("How many hours is the event? "))

    free_time = available_time(start_time, end_time)

    enough_time = can_attend(free_time, event_length)

    print(f"You have {free_time} hours available.")

    if enough_time:
        print("You have enough time to attend the event!")
    else:
        print("You do not have enough time to attend the event.")