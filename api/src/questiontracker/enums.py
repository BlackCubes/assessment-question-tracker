from enum import StrEnum


class QuestionTrackerEnum(StrEnum):
    """
    A custom Enum class that extends StrEnum.

    This class inherits all functionality from StrEnum, including
    string representation and automatic value conversion to strings.

    Example:
        class Visibility(QuestionTrackerEnum):
            OPEN = "Open"
            RESTRICTED = "Restricted"

        assert str(Visibility.OPEN) == "Open"
    """
