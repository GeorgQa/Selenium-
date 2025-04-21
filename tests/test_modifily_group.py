from model.group import Group

def test_modify_group_name(app):
    app.open_home_page()
    app.session.login()
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.open_home_page()
    app.session.login()
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.open_home_page()
    app.session.login()
    app.group.modify_first_group(Group(footer="New footer"))
    app.session.logout()