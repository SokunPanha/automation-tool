import flet as ft 
from flet_route import Params, Routing, Basket
from component import Button_Icon

def Profile(page:ft.Page, params: Params, basket: Basket ):
    page.title = 'Profile Page'
    params.name = "dara"
    basket.name = "dsdsd"
    return ft.View(
        controls=[
           ft.AppBar(
        leading= ft.IconButton(on_click= lambda _: page.go(f"/"), icon= ft.icons.ARROW_BACK),
        leading_width=40,
        title=ft.Text("Home"),
        center_title=False,
        bgcolor=ft.colors.GREY_900,
        elevation= 10,
        actions=[
              
        ],

    ),
    ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.TextField(hint_text= "Search", prefix_icon= ft.icons.SEARCH, height=50, border_radius=100, content_padding=ft.padding.symmetric(0,30) , border_color="white"),
                 ft.Row(
                     controls=[
                            Button_Icon(page,margin = 0,text = "Add", style= ft.ButtonStyle(
                  bgcolor= ft.colors.BLACK,
                  color= "white"
              ),icon= ft.icons.ADD, route= "/profile-create"),
                Button_Icon(page,margin = ft.margin.symmetric(0,5), text="Delete All", style= ft.ButtonStyle(
                  bgcolor= ft.colors.BLACK,
                  color= "white"
              ),icon= ft.icons.DELETE_FOREVER, route= "/")
                     ]
                 ),
           
                ],
                alignment= ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        ]
    )
        ]
    )