from displays_PO import CellPhone
import pytest


def test_connect():
    display = CellPhone.CellPhone()
    display.start_server()
    return display


