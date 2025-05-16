from geezer import log, enable_auto_tagging

enable_auto_tagging()


def process_checkout(user_id, amount, card_info):
    log(f"Starting checkout for user {user_id}", "checkout")

    if not card_info.get("number"):
        log("Missing card number", "card validation")
        return False

    log("Card info validated", "card validation")

    # Simulate API call
    log("Calling Fortis API...", "payment gateway")

    success = True  # Simulate success/failure
    if success:
        log(f"Transaction approved for ${amount}", "payment", "ok")
    else:
        log("Transaction failed", "payment error")

    log("Redirecting to receipt page", "redirect")
    return True


if __name__ == "__main__":
    sample_card = {"number": "4111111111111111", "cvv": "123", "exp": "12/25"}
    process_checkout(user_id=42, amount="49.99", card_info=sample_card)
