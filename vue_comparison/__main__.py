from aiomisc import Service, bind_socket, entrypoint
from aiomisc.log import basic_config

from vue_comparison.args import AdminArguments
from vue_comparison.service.admin import AdminService


def main() -> None:
    args = AdminArguments()
    args.parse_args()
    basic_config(
        level=args.log_level, log_format='rich', buffered=False,
    )

    http = args.http
    sock = bind_socket(
        address=http.address, port=http.port, proto_name='http',
    )

    services: list[Service] = [
        AdminService(
            sock=sock,
            debug=args.debug,
            dist_path=args.dist_path,
        ),
    ]

    with entrypoint(
        *services,
        log_format='rich',
        log_level=args.log_level,
        pool_size=args.pool_size,
        debug=args.debug,
    ) as loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
