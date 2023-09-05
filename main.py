# Essa atividade pretende entender como são calculadas métricas de software
# relacionadas a diferentes maneiras de ecrita de código.

materia = {
    'matéria': 'Engenharia economica para software'
}

materia.update(
    {
        'professor': 'Aline Brito'
    }
)

materia.update({'dia': '04/09/2023'})

print(
    'Olá, essa é a atividade da matéria de engenharia economica de software!'
)
print('')

for key, value in materia.items():
    print(key, value)
