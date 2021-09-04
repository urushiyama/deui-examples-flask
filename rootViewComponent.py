import html

from reloadrable import autoreload
from deui.core.viewComponent import ViewComponent
from deui.html.view import (
    HTML, Head, Meta, Title, Text, Body, Header, Main, Division, Image, Paragraph, Small, Heading, Form, FieldSet,
    Legend, Label, Input, Button, Aside, Anchor, Footer, Preformatted, Code, Joined, Idiomatic, Script
)

from bootstrap_links import BootstrapLinks
from navigation_bar import NavigationBar


@autoreload
class RootViewComponent(ViewComponent):
    lang = "en"

    def __str__(self):
        return "RootViewComponent"

    def body(self):
        with HTML(lang=RootViewComponent.lang, clazz="h-100"):
            with Head():
                Meta(name="viewport", content="width=device-width, initial-scale=1")
                Meta(charset="utf-8")
                BootstrapLinks()
                with Title():
                    Text(value="Hello Declarative HTML | DeUI")
            with Body(clazz=["d-flex", "w-100", "h-100", "mx-auto", "flex-column"]):
                with Header(clazz="mb-auto"):
                    NavigationBar()
                with Main(clazz=["container", "px-3", "mb-auto"]):
                    with Division(clazz=["row", "justify-content-center", "align-items-center", "my-3"]):
                        with Division(clazz=["col-sm-4"]):
                            Image(clazz=["img-fluid"], src="/static/DeUI_logo.png")
                        with Division(clazz=["col-sm-6"]):
                            with Paragraph(clazz="h3"):
                                Text(value="Declarative UI Wrapper Framework for Python")
                            with Paragraph():
                                with Small(clazz="text-muted"):
                                    with Joined():
                                        Text(value="The logo is inspired by Chinese sweets Jin Deui, which is "
                                                   "sesame-coated and fried rice cake wrapping lotus, black bean, "
                                                   "or red bean paste.")
                    with Division(clazz=["row", "align-items-center"]):
                        with Heading(level=1):
                            Text(value="Register your account")
                        with Paragraph():
                            Text(value="You have to make an account to use this service.")
                            Text(value="Please enter the form below and submit to register your account.")
                    with Division(clazz=["row", "align-items-center"]):
                        with Form():
                            with FieldSet():
                                with Legend():
                                    Text(value="Input your name here")
                                with Division(clazz="mb-3 row"):
                                    with Label(attr={"class": ["col-sm-3", "col-form-label"], "for": "inputFirstName"}):
                                        Text(value="First Name")
                                    with Division(clazz="col-sm-9"):
                                        Input(type="text", clazz="form-control", id="inputFirstName", placeholder="Jin")
                                with Division(clazz="mb-3 row"):
                                    with Label(attr={"class": ["col-sm-3", "col-form-label"], "for": "inputLastName"}):
                                        Text(value="Last Name")
                                    with Division(clazz="col-sm-9"):
                                        Input(type="text", clazz="form-control", id="inputLastName", placeholder="Deui")
                            with Button(clazz=["btn", "btn-primary", "mb-3"], type="submit"):
                                Text(value="Register")
                with Aside(clazz=["container", "px-3"]):
                    with Division(clazz="row"):
                        for i in range(3):
                            with Division(clazz="col-md mb-3"):
                                with Division(clazz="card"):
                                    with Image(clazz="card-img-top",
                                               src=f"https://picsum.photos/400/300/?random={html.escape(str(hash(i)))}",
                                               alt="random image for card"):
                                        with Division(clazz="card-body"):
                                            with Heading(level=5, clazz="card-title"):
                                                Text(value="Random Image")
                                            with Paragraph(clazz="card-text"):
                                                Text(
                                                    value="Lorem ipsum dolor sit amet, consectetur adipisicing elit, "
                                                          "sed do eiusmod tempor incididunt ut labore et dolore magna "
                                                          "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                                                          "ullamco laboris nisi ut aliquip ex ea commodo consequat.")
                                            with Anchor(href="#", clazz=["btn", "btn-primary", "stretched-link"]):
                                                Text(value="Go somewhere")
                with Footer(clazz=["mt-auto"]):
                    with Preformatted(clazz=["mb-0", "text-black-50", "bg-light", "d-flex", "align-items-center",
                                             "justify-content-center"]):
                        with Code():
                            with Joined():
                                Text(value="Code with ")
                                Idiomatic(clazz=["bi", "bi-suit-heart-fill", "text-danger"], alt="love")
                Script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js",
                       integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW",
                       crossorigin="anonymous")
