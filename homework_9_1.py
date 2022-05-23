import requests
heroes_list = ['Hulk', 'Captain America', 'Thanos']


def who_is_smartest_hero(heroes_list):
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    max_intelligence = 0
    for hero in heroes_list:
        query = requests.get(url + hero)
        hero_intelligence = int(query.json()['results'][0]['powerstats']['intelligence'])
        if hero_intelligence > max_intelligence:
            smartest_hero = hero
    return smartest_hero


print(who_is_smartest_hero(heroes_list))
