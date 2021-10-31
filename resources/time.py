from flask_restful import Resource, reqparse
from operator import itemgetter

from models.time import TimeModel

times = [
    {
        'times_id': '1',
        'nome': 'Atletico Mineiro',
        'pontos': 45,
        'ranking': '1',
    },
    {
        'times_id': '2',
        'nome': 'Palmeiras',
        'pontos': 38,
        'ranking': '2',
    },
    {
        'times_id': '3',
        'nome': 'Flamengo',
        'pontos': 40,
        'ranking': '3',
    },
    {
        'times_id': '4',
        'nome': 'Fortaleza',
        'pontos': 33,
        'ranking': '4',
    }
]

rodadas = []


class Times(Resource):
    def get(self):
        global times
        times = sorted(times, key=itemgetter('pontos'), reverse=True)
        contador = 0
        for time in times:
            contador += 1
            time['ranking'] = contador
        return {'times': times}


class Time(Resource):

    def find_dados(times_id):
        for time in times:
            if time['times_id'] == times_id:
                return time
        return None

    def get(self, times_id):
        time = Time.find_dados(times_id)
        if time:
            return time
        return {'message': 'Time not found'}, 404

    def put(self, times_id):
        dados = CadastraTime.argumentos.parse_args()

        time_objeto = TimeModel(**dados)
        novo_time = time_objeto.json()
        time = Time.find_dados(times_id)
        if time:
            time.update(novo_time)
            return novo_time, 200
        times.append(novo_time)
        return novo_time

    def delete(self, times_id):
        global times
        times = [time for time in times if time['times_id'] != times_id]
        return {'message': 'Time deletado'}


class CadastraTime(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('times_id')
    argumentos.add_argument('nome')
    argumentos.add_argument('pontos')
    argumentos.add_argument('ranking')

    def post(self):
        dados = CadastraTime.argumentos.parse_args()

        time_objeto = TimeModel(**dados)
        novo_time = time_objeto.json()

        times.append(novo_time)
        return novo_time, 200


class Rodada(Resource):
    def get(self):
        return {'rodadas': rodadas}


class Rodadas(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('rodada_id')
    argumentos.add_argument('jogo')
    argumentos.add_argument('time1')
    argumentos.add_argument('time2')
    argumentos.add_argument('gols1')
    argumentos.add_argument('gols2')

    def get(self, rodada_id):
        pass

    def post(self):

        global rodadas

        dados = Rodadas.argumentos.parse_args()

        jogo = {**dados}

        for time in times:
            if time['nome'] == jogo['time1']:
                if jogo['gols1'] > jogo['gols2']:
                    time['pontos'] += 3
                if jogo['gols1'] < jogo['gols2']:
                    time['pontos'] += 0
                if jogo['gols1'] == jogo['gols2']:
                    time['pontos'] += 1
            if time['nome'] == jogo['time2']:
                if jogo['gols2'] > jogo['gols1']:
                    time['pontos'] += 3
                if jogo['gols2'] < jogo['gols1']:
                    time['pontos'] += 0

        rodadas.append(jogo)

        return rodadas, 200

    def put(self, rodada_id):
        pass
