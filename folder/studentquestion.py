DOWNTOWN_HOTEL_PRICE = 165
TRAIN_PRICE = 45
AQUARIUM_PRICE = 35
TAX_RATE = 0.07

student_name = "Lydia"

hotel = "Downtown Hotel"
nights = 2
hotel_total = DOWNTOWN_HOTEL_PRICE * nights

transportation = "Train"
activity = "Aquarium"

subtotal = hotel_total + TRAIN_PRICE + AQUARIUM_PRICE

tax = subtotal * TAX_RATE

total_before_credit = subtotal + tax

dad_money = 25

final_total = total_before_credit - dad_money

trip_summary = (
    "BOSTON TRIP SUMMARY\n"
    + "Student: " + student_name + "\n"
    + "Hotel: " + hotel + "\n"
    + "Nights: " + str(nights) + "\n"
    + "Transportation: " + transportation + "\n"
    + "Activity: " + activity + "\n\n"
    + "Cost before tax: $" + str(subtotal) + "\n"
    + "Tax: $" + str(tax) + "\n"
    + "Total before Dad's Money: $" + str(total_before_credit) + "\n"
    + "Dad's Money: -$" + str(dad_money) + "\n"
    + "Final total: $" + str(final_total)
)

print(trip_summary)