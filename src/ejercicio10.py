def initializar_record(total_score, participants):
    for p in participants:
        total_score[p] = {
            'score' : 0,
            'rounds_wins' : 0,
            'max_points' : 0,
        }


def score_round(total_score, scores):
    mvp_round = {
        'participant': '',
        'score': 0
    }

    for participant, score in scores.items():
        score = sum(x for x in score.values())
        total_score[participant]['score'] += score
        if total_score[participant]['max_points'] < score: total_score[participant]['max_points'] = score
        
        # Calcular ganador ronda
        if score > mvp_round['score']:
            mvp_round['participant'] = participant
            mvp_round['score'] = score
        
    total_score[mvp_round['participant']]['rounds_wins'] += 1
    return mvp_round


def print_table(total_score, total_round=1):
    width = 18  # ancho único para todas las columnas

    headers = ["Cocinero", "Puntaje", "Rondas Ganadas", "Mejor Ronda"]
    if total_round > 1:
        headers.append("Promedio")

    # Header
    header = "".join(f"{h:<{width}}" for h in headers)
    print(header)
    print("-" * len(header))

    # Filas
    for participant, points in total_score.items():
        score = points['score']
        rounds_wins = points['rounds_wins']
        max_points = points['max_points']

        row_data = [participant, score, rounds_wins, max_points]

        if total_round > 1:
            row_data.append(f"{round(score / total_round, 1)}")

        row = "".join(f"{str(d):<{width}}" for d in row_data)
        print(row)

    print("-" * len(header))

def competence(rounds):
    round_number = 1
    total_score = {}
    for round in rounds:
        
        if not total_score: initializar_record(total_score, round['scores'].keys())

        print(f'Ronda {round_number} - {round['theme']}:')
        round_number += 1

        mvp_round = score_round(total_score, round['scores'])
        print(f'Ganador: {mvp_round['participant']} ({mvp_round['score']} pts)')

        # Ordeno dict por puntos totales
        total_score = {k: v for k, v in sorted(total_score.items(), key=lambda item: item[1]['score'], reverse=True)}

        print_table(total_score)
    
    print_table(total_score, len(rounds))
