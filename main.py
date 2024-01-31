import flet as ft
from flet_route import Routing, path

from views import Home, Profile, Add_Profile, Edit_Profile, Edit_Profile1

def main(page: ft.Page):
    # page.window_center()
    # page.window_width =800
    # page.window_height =700
    app_routes = [
           path(url="/",clear=True, view=Home),
           path(url="/profile",clear=True, view=Profile),
           path(url="/profile-create",clear=True, view=Add_Profile),
           path(url="/profile-update",clear=True, view= Edit_Profile),
           path(url="/profile-update-1",clear=True, view= Edit_Profile1)
    ]
    Routing(page=page, app_routes=app_routes)
    page.go(page.route)
ft.app(target=main)