fav_places = {
    'oscar' : ['colombia', 'mexico', 'bali', 'japom'],
    'leonardo' : ['calgary', 'edmonton', 'colombia', 'vancouver', 'bali', 
                  'tokio', 'brazil', 'amazon', 'switzerland'],
    'cecilia' : ['colombia', 'silvania', 'fusagasuga', 'roma', 'alemania'],
    'madison' : ['sandpoint', 'banff', 'koh samui', 'fernie']
}
print(" \n\t\tfavourite places database\n".upper())
ans = input('who do you wan to know about: '.title()).lower().strip()
for name, places in fav_places.items():
    if ans == name:
        print(f"{ans.title()}'s favourite places are:")
        for _place in places:
            print(f'\t{_place}'.title())
