def open_or_senior(data):
    new_list = []
    for list in data:
        if list[0] >= 55 and list[1] > 7:
            new_list.append('Senior')
        else:
            new_list.append('Open')
    return new_list