from reloadrable import autoreload
from deui.core.viewComponent import ViewComponent
from deui.html.view import Link


@autoreload
class BootstrapLinks(ViewComponent):
    def body(self):
        Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css",
             rel="stylesheet",
             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1",
             crossorigin="anonymous")
        Link(rel="stylesheet",
             href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/font/bootstrap-icons.css")
