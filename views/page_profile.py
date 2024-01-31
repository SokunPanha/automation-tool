import flet as ft 
from flet_route import Params, Routing, Basket
from component import ProfileDataTable_ChBox
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
                           ft.ElevatedButton("Add Account", style= ft.ButtonStyle(bgcolor= ft.colors.BLACK,color= "white"),icon= ft.icons.ADD, on_click= lambda _: page.go("/profile-create")),
                           ft.ElevatedButton("Register All",style= ft.ButtonStyle(bgcolor= ft.colors.BLACK,color= "white"),icon= ft.icons.LOGIN)
                     ]
                 ),
           
                ],
                alignment= ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ProfileDataTable_ChBox(page, params, basket,"/profile-update")
        ]
    )
        ]
    )