"""Functions for encoding and decoding strings."""
from __future__ import annotations

import typing as t

ENCODING = 'utf-8'


def to_optional_bytes(value, errors='strict'):  # type: (t.Optional[t.AnyStr], str) -> t.Optional[bytes]
    """Return the given value as bytes encoded using UTF-8 if not already bytes, or None if the value is None."""
    return None if value is None else to_bytes(value, errors)


def to_optional_text(value, errors='strict'):  # type: (t.Optional[t.AnyStr], str) -> t.Optional[str]
    """Return the given value as text decoded using UTF-8 if not already text, or None if the value is None."""
    return None if value is None else to_text(value, errors)


def to_bytes(value, errors='strict'):  # type: (t.AnyStr, str) -> bytes
    """Return the given value as bytes encoded using UTF-8 if not already bytes."""
    if isinstance(value, bytes):
        return value

    if isinstance(value, str):
        return value.encode(ENCODING, errors)

    raise Exception('value is not bytes or text: %s' % type(value))


def to_text(value, errors='strict'):  # type: (t.AnyStr, str) -> str
    """Return the given value as text decoded using UTF-8 if not already text."""
    if isinstance(value, bytes):
        return value.decode(ENCODING, errors)

    if isinstance(value, str):
        return value

    raise Exception('value is not bytes or text: %s' % type(value))
