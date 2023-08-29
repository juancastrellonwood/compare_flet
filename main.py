import flet as ft
from compare import Compare
def main(page: ft.Page):
    page.title = "ToDo App"
    page.bgcolor = '#dde5f2'
    page.window_width = 600
    page.window_height = 333
    page.window_resizable = False   
    page.horizontal_alignment = "center"
    
    app = Compare()

    # add application's root control to the page
    page.add(app)

ft.app(target=main)