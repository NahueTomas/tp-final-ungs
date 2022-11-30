def traerMejores():
    with open('assets/txt/ranking.txt') as ranking:
        ranking = ranking.read()[:-1].split('\n')

    rankingDeListas = []
    for persona in ranking:
        rankingDeListas.append(persona.split('-'))

    rankingOrdenado = sorted(
        rankingDeListas, key=lambda persona: persona[1], reverse=True)

    return rankingOrdenado
