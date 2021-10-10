import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']

def intelligence_search(list_of_persons):
    compare_dict = {}
    for name in list_of_persons:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        result = requests.get(url=url)
        intelligence = int(result.json()['results'][0]['powerstats']['intelligence'])
        temp_dict = {name: intelligence}
        compare_dict.update(temp_dict)
    print(f'Самый умный {max(compare_dict, key=compare_dict.get)}')
    return

intelligence_search(hero_list)