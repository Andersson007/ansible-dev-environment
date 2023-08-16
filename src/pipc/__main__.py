"""A runpy entry point for pipc.

This makes it possible to invoke CLI
via :command:`python -m ansible_cdk`.
"""

from .cli import main


if __name__ == "__main__":
    main()
