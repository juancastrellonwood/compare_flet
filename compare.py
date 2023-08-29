import flet as ft

class Compare(ft.UserControl):
    def build(self):
        self.number_a = ft.TextField(
            bgcolor="#A0A0A0", 
            border_color='#ddaaff',
            border_width = 3,
            border_radius = 10,
            width= 100,
        )

        self.number_b = ft.TextField(
            bgcolor="#A0A0A0", 
            border_color='#ddaaff',
            border_width = 3,
            border_radius = 10,
            width= 100,
        )

        self.a_container = ft.Container(content = self.number_a, padding = 10, border_radius = 10)
        self.b_container = ft.Container(content = self.number_b, padding = 10, border_radius = 10)

        self.comparison_text = ft.Text(value =" ", 
                            size=50,
                            text_align='CENTER',
                            weight=ft.FontWeight.BOLD,)
        self.comparison_row = ft.Row(
            vertical_alignment="CENTER",
            controls=[self.comparison_text])

        self.comparison = ft.Row(
            spacing=50,
            alignment="CENTER",
            controls = [
                ft.Column(
                    horizontal_alignment="CENTER",
                    controls = [
                        ft.Text(                    
                            '!Número A¡', 
                            size=30,
                            text_align='CENTER',
                            weight=ft.FontWeight.BOLD,
                            font_family="Century Gothic Regular"
                        ),
                        self.a_container,
                    ]
                ),
                self.comparison_row,
                ft.Column(
                    horizontal_alignment="CENTER",
                    controls = [
                        ft.Text(                    
                            '!Número B¡', 
                            size=30,
                            text_align='CENTER',
                            weight=ft.FontWeight.BOLD,
                            font_family="Century Gothic Regular "
                        ),
                        self.b_container,
                    ]
                )
            ]
        )

        return ft.Column(
            horizontal_alignment="CENTER",
            controls = [
                ft.Text(
                    '¡Número mayor!', 
                    size=30,
                    text_align='CENTER',
                    weight=ft.FontWeight.BOLD,
                    font_family="Century Gothic Regular "
                ),
                ft.Text(
                    'Ingrese dos números para saber cuál es mayor.', 
                    size=16,
                    text_align='CENTER',
                    font_family="Century Gothic Regular "
                ),
                self.comparison,
                ft.FilledTonalButton(
                    text="Filled tonal button",
                    width=240,
                    height=50,
                    on_click = self.compare
                ),
                ft.Text(
                    'Designed by Wood 2023', 
                    size=10,
                    text_align='CENTER',
                    font_family="Century Gothic Regular "
                )
            ])

    def compare(self, e):
        a = int(self.number_a.value)
        b = int(self.number_b.value)
        status = self.compare_numbers(a, b)
        self.comparison_text.value =status
        self.comparison_row.visible = True
        self.update()

    def compare_numbers(self, a: int, b: int) -> str:
        color_blue = '#0000ff'
        color_transparent = '#00000000'
        if a>b: 
            self.a_container.bgcolor = color_blue
            self.b_container.bgcolor = color_transparent
            return '>'

        if a<b: 
            self.a_container.bgcolor = color_transparent
            self.b_container.bgcolor = color_blue
            return '>'
        
        if a==b: 
            self.a_container.bgcolor = color_blue
            self.b_container.bgcolor = color_blue
            return '='
