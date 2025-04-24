# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if 20% or higher
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    return price  # Return original price if discount is less than 20%

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"Final price: ${final_price:.2f}")
