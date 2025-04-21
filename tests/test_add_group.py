from model.group import Group


def test_add_group(app):
    app.group.create()
    app.group.filling_in_group_data(Group(name="new_group ", header="Header ", footer="vtgtr "))
    app.group.save()

def test_no_data_group(app):
    app.group.create()
    app.group.filling_in_group_data(Group(name = " ", header = " ", footer = " "))
    app.group.save()
