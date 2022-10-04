team = {
    'sachin':100,
    'kohli':500,
    'ganguly':300
}

output = dict(sorted(team.items(),key=lambda y:y[1]))

print(output)