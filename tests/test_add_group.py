

def test_add_group(app):
    app.open_home_page()
    app.session.login()
    app.group.create()
    app.group.filling_in_group_data( "new_group", "Header", "vtgtr")
    app.group.save()
    app.session.logout()

def test_no_data_group(app):
    app.open_home_page()
    app.session.login()
    app.group.create()
    app.group.filling_in_group_data( " ", " ", " ")
    app.group.save()
    app.session.logout()


