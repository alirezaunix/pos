from nicegui import ui
import dbManager

def warehouse_f():
    with ui.card().classes('w-full'):
        with ui.column().classes('w-full'):
            n=ui.input(label='اسم کالا', placeholder='start typing').props('dir=rtl').classes('w-full text-center  font-bold')
            q=ui.number(label='تعداد کالا', placeholder='start typing').props('dir=rtl').classes('w-full text-center  font-bold')
            i=ui.number(label='قیمت خرید کالا', placeholder='start typing').props('dir=rtl').classes('w-full text-center  font-bold')
            o=ui.number(label='قیمت فروش کالا', placeholder='start typing').props('dir=rtl').classes('w-full text-center  font-bold')
            with ui.row().classes('w-full'):
                ui.button('Save', on_click=lambda: dbManager.writeDB(n.value,q.value,i.value,o.value)).classes('w-full')
                ui.button('Exit', on_click=lambda: ui.navigate.to("/warehouse")).classes('w-full')
