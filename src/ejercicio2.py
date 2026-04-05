from datetime import timedelta

'''
def duracion_playlist():
    durations = [x['duration'] for x in playlist ]
    durations_sg = 0
    durations_min = 0
    durations_hour = 0
    for dur in durations:
        time = dur.split(':')
        durations_sg += int(time[0]) * 60
        durations_sg += int(time[1])

    durations_min += durations_sg // 60
    durations_sg = durations_sg % 60
    durations_hour = durations_sg // 3600

    response = f'Duración total: {durations_hour}h {durations_min}m {durations_sg}s' if durations_hour > 0 else f'Duración total: {durations_min}m {durations_sg}s'

    return response
'''

def duracion_playlist(playlist):
    total = timedelta()
    for x in playlist:
        minutos, segundos = map(int, x['duration'].split(':'))
        total += timedelta(minutes=minutos, seconds=segundos)

    horas = int(total.total_seconds() // 3600)
    minutos = int((total.total_seconds() % 3600) // 60)
    segundos = int(total.total_seconds() % 60)

    if horas > 0:
        return f'Duración total: {horas}h {minutos}m {segundos}s'
    return f'Duración total: {minutos}m {segundos}s'

'''
def filter_playlist(filter='max'):
    time = timedelta(seconds=0) if filter == 'max' else  timedelta(days=1)
    filter_song = {}
    for x in playlist:
        minutos, segundos = map(int, x['duration'].split(':'))
        total = timedelta(minutes=minutos, seconds=segundos)
        if filter == 'max':
            if total > time: 
                time = total
                filter_song = x
        else:
            if total < time: 
                time = total
                filter_song = x

    return f'Canción más larga: "{filter_song['title']}" "{filter_song['duration']}"' if filter == 'max' else f'Canción más corta: "{filter_song['title']}" "{filter_song['duration']}"'
'''

def parse_duration(duration):
    minutos, segundos = map(int, duration.split(':'))
    return timedelta(minutes=minutos, seconds=segundos)

def filter_playlist(playlist, filter='max'):
    if filter == 'max':
        song = max( playlist, key=lambda song: parse_duration(song['duration']))
        return f'Canción más larga: "{song['title']}" "{song['duration']}"'
    else:
        song = min( playlist, key=lambda song: parse_duration(song['duration']))
        return f'Canción más corta: "{song['title']}" "{song['duration']}"'