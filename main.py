from flask import Flask
from livereload import Server
from reloadrable import ReloadableManager
from deui.html.engine import WebApp

from rootViewComponent import RootViewComponent

from logging import getLogger, DEBUG, StreamHandler, Formatter

logger = getLogger()
logger.setLevel(level=DEBUG)
sh = StreamHandler()
sh.setFormatter(Formatter("[%(levelname)s %(asctime)s %(name)s] %(message)s", datefmt="%y%m%d %H:%M:%S"))
sh.setLevel(level=DEBUG)
logger.addHandler(sh)
del sh

flask = Flask(__name__)

if __name__ == "__main__":
    with WebApp() as app:
        app.body(lambda: RootViewComponent())

        # start UI thread
        app.start()


        @flask.route('/')
        def index():
            # do something to update data models.
            RootViewComponent.lang = "en"
            return app.fetch_content().result()


        @flask.route('/ja/')
        def index_ja():
            # do something to update data models.
            RootViewComponent.lang = "ja"
            return app.fetch_content().result()


        # start Flask
        flask.debug = True
        server = Server(flask.wsgi_app)
        server.watch('*')
        server.watch('static/*')
        server.serve(open_url_delay=1)

        # finish
        app.stop()
        ReloadableManager.stop_on_modified_updates()
