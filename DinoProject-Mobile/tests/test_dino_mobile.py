from displays_PO import CellPhone
import pytest


def create_screen():
    display = CellPhone.CellPhone()
    # display.start_server()
    return display


