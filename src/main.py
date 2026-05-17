"""Initial entry point for the Git branch experiment."""

from user import get_default_user
from order import get_default_order
from config import APP_NAME


def main() -> None:
    print(f"{APP_NAME} - initial version")
    print(f"User: {get_default_user()}")
    print(f"Order: {get_default_order()}")


if __name__ == "__main__":
    main()
