import flet as ft 
from flet_route import Params, Basket
from component import Card_Icon
 

def Home (page:ft.Page, params: Params, basket: Basket ):
    page.title = 'Home Page'
    name = basket.get("name")

    return ft.View( 
        vertical_alignment= "center",
        controls=[
            ft.Column(
            controls=[
                ft.Text(value=name),
                ft.Row(
                    controls=[
                        Card_Icon(page,ft.icons.PERSON, "Profile", "/profile"),
                        Card_Icon(page,ft.icons.FACEBOOK_OUTLINED, "Active Ac", "/profile"),
                        Card_Icon(page,ft.icons.GROUP, "Group Post", "/profile"),
        ],
        alignment= ft.MainAxisAlignment.CENTER
        )
        ],
 )
        ]
    )