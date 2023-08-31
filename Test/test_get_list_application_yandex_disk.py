from Base_App import API_disk


def test_get_list_application(url, headers, pages):
    query = API_disk()
    path_list = (["%2f"])
    for i in path_list:
        response = (query.get_query_json(f'{url}{pages["resourses"]["base"]}{i}', headers))
        if response["type"] == "file":
            continue
        for _ in range(len(response["_embedded"]["items"])):
            data_path = response["_embedded"]["items"][_]["path"]
            path_list.append(data_path[data_path.find("disk:/") + 5:])
    
    assert sorted(path_list)
        

