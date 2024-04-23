def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price after applying discount
final_price = calculate_discount(original_price, discount_percentage)

# Print final price
if final_price == original_price:
    print(f"No discount applied. Final price: ${final_price}")
else:
    print(f"Discount applied. Final price after discount: ${final_price}")