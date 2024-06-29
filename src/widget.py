from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """Маскирует номер карты или счета"""
    if "Счет" in string:
        return f"Счет {get_mask_account(string)}"
    else:
        card = get_mask_card_number(string[-16:])
        mask_card = string.replace(string[-16:], card)
        return mask_card


def get_data(data: str) -> str:
    """Функция, которая возвращает дату"""
    d = datetime.strptime(data, format("%Y-%m-%dt%H:%M:%S.%f"))
    return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa platinum 1111222233334444"))
    print(mask_account_card("Счет 1111222233335555"))
    print(get_data("2018-07-11T02:26:18.671407"))
