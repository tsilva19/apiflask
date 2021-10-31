from flask import Flask
from flask_restful import Api
from resources.time import Times, Time, Rodada, Rodadas, CadastraTime

app = Flask(__name__)
api = Api(app)


api.add_resource(Times, '/times')
api.add_resource(Time, '/time/<string:times_id>')
api.add_resource(CadastraTime, '/time')
api.add_resource(Rodada, '/rodada')
api.add_resource(Rodadas, '/rodada')
if __name__ == '__main__':
    app.run(debug=True)
