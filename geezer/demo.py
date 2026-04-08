from geezer import log, warn


def process_checkout(user_id, amount, card_info):
    log(f"Starting checkout for user {user_id}", emoji="🛒", label="checkout")

    if not card_info.get("number"):
        warn("Missing card number", label="card validation")
        return False

    log("Card info validated", emoji="✅", label="card validation")

    # Simulate API call
    log("Calling Fortis API...", emoji="🔌", label="payment gateway")

    success = True  # Simulate success/failure
    if success:
        log(f"Transaction approved for ${amount}", emoji="💰", label="payment", force=True)
    else:
        log("Transaction failed", emoji="❌", label="payment error")

    log("Redirecting to receipt page", emoji="➡️", label="redirect")
    return True


if __name__ == "__main__":
    sample_card = {"number": "4111111111111111", "cvv": "123", "exp": "12/25"}
    process_checkout(user_id=42, amount="49.99", card_info=sample_card)
