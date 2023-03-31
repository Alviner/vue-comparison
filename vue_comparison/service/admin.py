import pathlib

from aiohttp import web
from aiohttp.hdrs import METH_GET
from aiomisc.service.aiohttp import AIOHTTPService

from vue_comparison import logger

log = logger.getChild('aiohttp')


class BaseView(web.View):
    @property
    def dist_path(self) -> pathlib.Path:
        return self.request.config_dict['dist_path']


class IndexHandler(BaseView):
    async def get(self) -> web.StreamResponse:
        index_file = self.dist_path / 'index.html'
        if not index_file.is_file():
            raise web.HTTPNotFound
        return web.FileResponse(index_file)


class StaticResource(web.StaticResource):
    async def _handle(self, request: web.Request) -> web.StreamResponse:
        directory = pathlib.Path(self._directory)
        filename = request.match_info['filename']
        file_path = (directory / filename).resolve()
        if directory not in file_path.parents:
            log.error(
                'Not serving file %r because it is outside static '
                'file directory %r (got filename %r)',
                file_path,
                directory,
                filename,
            )
            raise web.HTTPNotFound
        if (gzip_file := file_path.with_name(file_path.name + '.gz')).is_file():
            file_path = gzip_file
        return web.FileResponse(file_path)


class AdminService(AIOHTTPService):
    __required__ = ('dist_path',)

    dist_path: pathlib.Path

    async def create_application(self) -> web.Application:
        app = web.Application()
        self._set_requires(app)
        app.router.add_route(
            method=METH_GET,
            path='/',
            handler=IndexHandler,
        )
        app.router.register_resource(
            StaticResource('/assets', self.dist_path / 'assets')
        )
        return app

    def _set_requires(self, app: web.Application) -> None:
        for name in self.__required__:
            app[name] = getattr(self, name)
