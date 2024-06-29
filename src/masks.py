def get_mask_card_number(card_number: str) -> str:
    """Функиия, которая маскирует номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функиия, которая маскирует номер счета"""
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(str(1111222233334444)))
    print(get_mask_account(str(11112222333344445555)))
