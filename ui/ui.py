"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
def side_barheader():
    return rx.color_mode_cond(
        light=rx.image(src="assests/lightlogo.svg", height="500px", width="500px"),  
        dark=rx.image(src="assests/darklogo.svg", height="500px", width="500px"),
    )


from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def image_pil_example():
    return rx.vstack(rx.image(src=ImageState.image))





def nav_bar()-> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Token Viz",size="8",weight="bold"),
            spacing="2",
        ),
        position="absolute",
        left="1.5em",
        top="1.5em",
    )






def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        nav_bar(),
        rx.color_mode.button(position="top-right"),
        rx.spacer(),
        rx.vstack(
            rx.vstack(
                rx.text("Tokens are displayed with different colors based on byte pair encoding."),
                image_pil_example(),
            ),
            position="absolute",
            top="5em",
            left="1.5em",
        ),
        
    )


app = rx.App()
app.add_page(index)

