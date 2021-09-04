from reloadrable import autoreload
from deui.core.viewComponent import ViewComponent
from deui.html.view import (
    Navigation, Division, Anchor, Joined, Image, Text, Button, Span, UnorderedList, ListItem, Form, Input
)


@autoreload
class NavigationBar(ViewComponent):
    def body(self):
        with Navigation(clazz=["navbar", "navbar-expand-lg", "navbar-light", "bg-light"]):
            with Division(clazz="container-fluid"):
                with Anchor(clazz="navbar-brand", href="#"):
                    with Joined():
                        Image(src="/static/DeUI_logo.png", width="22", height="22",
                              clazz="d-inline-block align-text-bottom")
                        Text(value="DeUI")
                with Button(clazz="navbar-toggler", type="button",
                            data_bs_toggle="collapse", data_bs_target="#navbar-content",
                            aria_controls="navbar-content", aria_expanded="false",
                            aria_label="Toggle navigation"):
                    Span(clazz="navbar-toggler-icon")
                with Division(clazz=["collapse", "navbar-collapse"], id="navbar-content"):
                    with UnorderedList(clazz=["navbar-nav", "me-auto", "mb-2", "mb-lg-0"]):
                        with ListItem(clazz="nav-item"):
                            with Anchor(clazz=["nav-link", "active"], aria_current="page", href="#"):
                                Text(value="Home")
                        with ListItem(clazz="nav-item"):
                            with Anchor(clazz="nav-link", href="#"):
                                Text(value="Tutorial")
                        with ListItem(clazz="nav-item"):
                            with Anchor(clazz=["nav-link", "disabled"], href="#", tabindex="-1", aria_disabled="true"):
                                Text(value="Docs")
                    with Form(clazz="d-flex"):
                        Input(clazz=["form-control", "me-2"], type="search", placeholder="Search", aria_label="Search")
                        with Button(clazz=["btn", "btn-outline-success"], type="submit"):
                            Text(value="Search")
