from nicegui import ui
from ui.index_page import index_f
#from ui.sell_page import sell_f
#from ui.statistics_page import statistics_f
from ui.warehouse_page import warehouse_f

@ui.page("/")
def index():
    index_f()

@ui.page("/warehouse")
def warehouse():
    warehouse_f()


@ui.page("/sell")
def sell():
    print("sell")


@ui.page("/statistics")
def statistics():
    print("statistics")

ui.run()