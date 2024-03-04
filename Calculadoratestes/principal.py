import flet as ft

cornum = "#FFFFFF"
corfund = "#282C34"
corsim = "#6051D2"

def principal(page: ft.Page):
    page.title= "Calculadora Hightech Full HD"
    
    

    result = ft.Text(value= "0", size= 60, text_align=ft.TextAlign.END)

    page.add(
        ft.Row(controls=[result]),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC", color=corfund, bgcolor=corsim, expand= 1),
                ft.ElevatedButton(text="⇐", color=corfund, bgcolor=corsim, expand= 1),
                ft.ElevatedButton(text="%", color=corfund, bgcolor=corsim, expand= 1),
                ft.ElevatedButton(text="÷", color=corfund, bgcolor=corsim, expand= 1), 
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="8", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="9", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="×", color=corfund, bgcolor=corsim, expand= 1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="5", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="6", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="-", color=corfund, bgcolor=corsim, expand= 1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="2", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="3", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="+", color=corfund, bgcolor=corsim, expand= 1),   
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="(-)", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="0", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text=".", color=corfund, bgcolor=cornum, expand= 1),
                ft.ElevatedButton(text="=", color=corfund, bgcolor=corsim, expand= 1),
            ]
        ),
    )


ft.app(target=principal)