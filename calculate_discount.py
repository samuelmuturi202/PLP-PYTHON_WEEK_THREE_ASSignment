# Discount Calculatot

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Applies the discount only if discount_percent is 20% or higher.
    
    Parameters:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: Final price after discount (if applicable), otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
print("🛒 Welcome to the Discount Calculator!")
print("A discount of 20% or more is required to be applied.\n")

# Get input from user
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display result
print("\n" + "="*40)
print("             FINAL PRICE")
print("="*40)

if discount_percent >= 20:
    savings = original_price - final_price
    print(f"✅ Discount applied: {discount_percent}%")
    print(f"   Original price:   ${original_price:8.2f}")
    print(f"   You save:         ${savings:8.2f}")
    print(f"   Final price:      ${final_price:8.2f}")
else:
    print(f"🚫 No discount applied (minimum 20% required)")
    print(f"   Final price:      ${final_price:8.2f}")

print("="*40)