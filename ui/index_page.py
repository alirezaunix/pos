from nicegui import ui
def index_f():
    with ui.card().classes('w-full'):
        with ui.column().classes('w-full'):
            ui.label('Wellcome').classes('w-full text-center text-4xl')

    with ui.card().classes('w-full'):
        with ui.column().classes('w-full'):
            ui.button('Warehouse', on_click=lambda: ui.navigate.to("/warehouse")).classes('w-full')
            ui.button('Sell', on_click=lambda: ui.navigate.to("/sell")).classes('w-full')
            ui.button('Statistics', on_click=lambda: ui.navigate.to("/statistics")).classes('w-full')