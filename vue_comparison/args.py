import pathlib

from argclass import Argument, Group, LogLevel, Parser


class AddressPortGroup(Group):
    address: str = Argument(default="127.0.0.1")
    port: int = Argument(default=8080)


class AdminArguments(Parser):
    debug: bool = Argument(default=False)
    pool_size: int = Argument(default=4)

    http: AddressPortGroup = AddressPortGroup(title="HTTP options")

    log_level: str = LogLevel

    dist_path: pathlib.Path = Argument(required=True)
