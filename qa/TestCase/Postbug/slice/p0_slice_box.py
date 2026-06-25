import dimaxer_ui as ui

# https://project.feishu.cn/dimaxer-dev/issue/detail/7013303433?parentUrl=%2Fdimaxer-dev%2Fissue%2Fhomepage
def slice_box():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.ribbon.hide_all")
    ui.item_click("post.ribbon.vis_vki59")
    ui.item_click("post.top.slice_panel")
    ui.combo_click("post.slice.combo_type", "Box")
    ui.item_click("post.slice.show_preview")
    ui.item_click("post.slice.apply")
    ui.item_click("post.ribbon.hide_all")
    ui.item_click("post.ribbon.vis_slice1")
    ui.capture_renderview(8)

