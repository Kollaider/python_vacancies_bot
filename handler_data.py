
def handler(lst):

    lst_ids = []
    lst_out = []

    for i in lst:
        lst_ids.append(i['id'])

    lst_out.append(lst[0: 2])

    return lst_out

def prepare_mes(data):
    data_dict = {}
    for i, v in enumerate(data[0]):
        lst_data = []
        lst_data.append(data[0][i]['name'])
        lst_data.append(data[0][i]['url'])
        lst_data.append(data[0][i]['published_at'])

        data_dict[i] = lst_data

    return data_dict