# src/ip_validator/validator.py
"""Валидация IPv4-адресов."""

import re


# Каждый октет: 0–255
# 25[0-5]     → 250–255
# 2[0-4][0-9] → 200–249
# 1[0-9]{2}   → 100–199
# [1-9]?[0-9] → 0–99 (без ведущих нулей, кроме самого 0)
_OCTET = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"

_IPV4_RE = re.compile(
    rf"^"
    rf"{_OCTET}\."
    rf"{_OCTET}\."
    rf"{_OCTET}\."
    rf"{_OCTET}"
    rf"\Z"
)


def is_valid_ipv4(ip: str) -> bool:
    """Проверяет, является ли строка синтаксически корректным IPv4-адресом.

    Args:
        ip: строка для проверки.

    Returns:
        True, если адрес похож на корректный IPv4, иначе False.

    Examples:
        >>> is_valid_ipv4("192.168.1.1")
        True
        >>> is_valid_ipv4("256.1.1.1")
        False
        >>> is_valid_ipv4("192.168.1")
        False
    """
    if not isinstance(ip, str):
        return False
    if not ip or len(ip) > 15:  # максимум: "255.255.255.255" = 15 символов
        return False
    return _IPV4_RE.match(ip) is not None