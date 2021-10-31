class TimeModel:
    def __init__(self, times_id, nome, pontos, ranking):
        self.times_id = times_id
        self.nome = nome
        self.pontos = pontos
        self.ranking = ranking

    def json(self):
        return {
            'times_id': self.times_id,
            'nome': self.nome,
            'pontos': self.pontos,
            'ranking': self.ranking
        }