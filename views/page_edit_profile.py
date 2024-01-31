from flet import *
from api.profile import Profile
from component import ProfileDataTable
from flet_route import Params, Basket

def Edit_Profile(page :Page,  params: Params, basket: Basket): 
   
    profile_name = TextField(prefix_icon=icons.PERSON_3, width=350, hint_text= "Profile Name", border_color= "white")
    email =  TextField(prefix_icon=icons.EMAIL, width=350, hint_text="Email",  border_color= "white")
    password =  TextField(password= True, prefix_icon=icons.PASSWORD, hint_text= "Password", width=350, border_color= "white")
    key = TextField(password= True, prefix_icon=icons.PASSWORD, hint_text= "2FA Key", width=350, border_color= "white")
    
    profile = Profile()
    data = basket.get("data")
    pname = ""
    if data != None:
        profile_name.value = pname = data[0]
        email.value = data[1]["email"]
        password.value = data[1]["password"]
        key.value = data[1]["key"]
        page.update()
    def Clear(e):
        profile_name.value = ""
        email.value = ""
        password.value = ""
        page.update()
    def Edit(e):
        print(pname,profile_name.value,email.value, password.value)
        profile.update(pname,profile_name.value,email.value, password.value)
        page.update()
   
    
    return View(
        horizontal_alignment= CrossAxisAlignment.CENTER,
        controls=[
            AppBar(
                leading= IconButton(on_click=lambda _: page.go("/profile"),icon= icons.ARROW_BACK),
                title= Text("Profile"),
                leading_width= 40

            )
            ,
            Column(
        horizontal_alignment= "center" ,
        alignment= CrossAxisAlignment.CENTER,
        controls=[
            Text("Edit Profile"),
            profile_name,
            email,
            password,
            key,
            Container(
                width = 350,
                content=Row(
                    controls=[
                        ElevatedButton(text="Cancel",on_click= Clear, bgcolor="red", color="white"),
                        ElevatedButton(text="Save", bgcolor="indigo", color="white",  on_click= Edit)
                        ],
                        alignment= MainAxisAlignment.END
            )
            ),
            ProfileDataTable(page, params, basket, "/profile-update-1")
        ],
    )
        ]
    )



