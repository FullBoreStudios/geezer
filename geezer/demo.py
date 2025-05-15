from geezer import prnt

def process_checkout(user_id, amount, card_info):
    prnt(f"Starting checkout for user {user_id}", "🛒", "checkout")

    if not card_info.get("number"):
        prnt("Missing card number", "❌", "card validation")
        return False

    prnt("Card info validated", "✅", "card validation")

    # Simulate API call
    prnt("Calling Fortis API...", "🔌", "payment gateway")

    success = True  # Simulate success/failure
    if success:
        prnt(f"Transaction approved for ${amount}", "💰", "payment", "ok")
    else:
        prnt("Transaction failed", "🔥", "payment error")

    prnt("Redirecting to receipt page", "➡️", "redirect")
    return True


# Run a demo
if __name__ == "__main__":
    sample_card = {"number": "4111111111111111", "cvv": "123", "exp": "12/25"}
    process_checkout(user_id=42, amount="49.99", card_info=sample_card)
