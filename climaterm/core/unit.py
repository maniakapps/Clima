from enum import auto, unique
from climaterm.core.base_enum import BaseEnum


@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()
