def char_to_decimal(c: str) -> int:
    if c.isdigit():
        return int(c)  # '0'-'9' -> 0-9
    elif "a" <= c <= "z":
        return ord(c) - 87  # 'a'-'z' -> 10-35
    elif "A" <= c <= "Z":
        return ord(c) - 29  # 'A'-'Z' -> 36-61
    raise ValueError(f"Invalid character '{c}' for base conversion")


def decimal_to_char(num: int) -> str:
    if 0 <= num < 10:
        return str(num)  # 0-9 -> '0'-'9'
    elif 10 <= num < 36:
        return chr(num + 87)  # 10-35 -> 'a'-'z'
    elif 36 <= num < 62:
        return chr(num + 29)  # 36-61 -> 'A'-'Z'
    raise ValueError(f"Invalid decimal value '{num}' for character conversion")


def convert_to_base10(from_base: int, number_str: str) -> int:
    number_str = number_str.lower() if from_base <= 36 else number_str
    return sum(
        char_to_decimal(c) * (from_base**i) for i, c in enumerate(number_str[::-1])
    )


def convert_from_base10(decimal_number: int, to_base: int) -> str:
    if decimal_number == 0:
        return "0"
    result = ""
    while decimal_number > 0:
        result = decimal_to_char(decimal_number % to_base) + result
        decimal_number //= to_base
    return result


def convert_base(from_base: int, number_str: str, to_base: int) -> str:
    if not (2 <= to_base <= 62 and 2 <= from_base <= 62):
        raise ValueError(f"Base must be between 2 and 62, got {to_base}")

    decimal_number = (
        int(number_str) if from_base == 10 else convert_to_base10(from_base, number_str)
    )
    return (
        str(decimal_number)
        if to_base == 10
        else convert_from_base10(decimal_number, to_base)
    )

if __name__ == "__main__":
    print(convert_base(10, "123", 16))  # 7B
    print(convert_base(16, "7B", 10))  # 123
    print(convert_base(10, "123", 2))  # 1111011
    print(convert_base(2, "1111011", 10))  # 123
    print(convert_base(10, "123", 62))  # 1D
