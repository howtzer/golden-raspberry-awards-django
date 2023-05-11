from copy import deepcopy
from django.db import connection


def atualiza_segundo_valor(response, operacao):
    response[operacao][1]["interval"] = response[operacao][0]["interval"]
    response[operacao][1]["producer"] = response[operacao][0]["producer"]
    response[operacao][1]["previousWin"] = response[operacao][0]["previousWin"]
    response[operacao][1]["followingWin"] = response[operacao][0]["followingWin"]


def atualiza_response(response, indice, intervalo, operacao):
    response[operacao][indice]["interval"] = intervalo["intervalos"]["maxInterval"]
    response[operacao][indice]["producer"] = intervalo["produtor"]
    response[operacao][indice]["previousWin"] = intervalo["intervalos"]["maxIntervalRange"]["menorAno"]
    response[operacao][indice]["followingWin"] = intervalo["intervalos"]["maxIntervalRange"]["maiorAno"]


def load_movies_csv():
    movie_list = open("static/movielist.csv", "r").readlines()
    keys = deepcopy(movie_list[0].replace("\n", "").split(";"))
    movie_list.pop(0)
    movie_list_dict = []
    for linha in movie_list:
        linha = linha.replace("\n", "")
        lista_campos = linha.split(";")
        linha_dict = {}
        for key, value in zip(keys, lista_campos):
            linha_dict[key] = value
        movie_list_dict.append(linha_dict)
    return movie_list_dict


def get_produtores_premiados():
    sql = """select app_producer.id as prod_id
                    from app_movie
                    join app_movie_producer on (app_movie.id = app_movie_producer.movie_id_id)
                    join app_producer on (app_producer.id = app_movie_producer.producer_id_id)
                where app_movie.winner = 'yes'
                    group by app_producer.id
                    having count(app_movie.id) > 1
                    order by app_producer.producer"""
    cursor = connection.cursor()
    cursor.execute(sql)
    produtores_aptos = cursor.fetchall()
    intervalos = []
    
    for prod_id in produtores_aptos:
        sql_movies = """
        select app_movie.year, app_producer.producer
            from app_movie
            join app_movie_producer on (app_movie.id = app_movie_producer.movie_id_id)
            join app_producer on (app_producer.id = app_movie_producer.producer_id_id)
            where app_movie.winner = 'yes' and app_producer.id = '"""+str(prod_id[0])+"'"
        cursor.execute(sql_movies)
        produtor_filmes_premiados = cursor.fetchall()

        premiacoes = []
        produtor = produtor_filmes_premiados[0][1]

        for movie in produtor_filmes_premiados:
            ano_premiacao = movie[0]
            premiacoes.append(ano_premiacao)

        #calcula intervalos aqui
        premiacoes.sort()
        minIntervalRange = []
        maxIntervalRange = []
        interval = 0
        maxInterval = 0
        minInterval = 9999
        for i in range(0, len(premiacoes)):
            if i+1 < len(premiacoes):
                interval = premiacoes[i+1] - premiacoes[i]
                if interval > maxInterval:
                    maxInterval = interval
                    maxIntervalRange = {"menorAno":premiacoes[i], "maiorAno": premiacoes[i+1]}
                if interval < minInterval:
                    minInterval = interval
                    minIntervalRange = {"menorAno":premiacoes[i], "maiorAno": premiacoes[i+1]}
                    
        intervalos.append({"produtor":produtor,
            "intervalos": {"maxInterval":maxInterval,
                        "minInterval":minInterval,
                        "minIntervalRange": minIntervalRange,
                        "maxIntervalRange":maxIntervalRange}
            })
    return intervalos


RESPONSE_GET = {
        "min": [
        {
            "producer": "",
            "interval": 0,
            "previousWin": 0,
            "followingWin": 0
         },
        {
            "producer": "",
            "interval": 0,
            "previousWin": 0,
            "followingWin": 0
         }
        ],
        "max": [
        {
            "producer": "",
            "interval": 0,
            "previousWin": 0,
            "followingWin": 0
         },
        {
            "producer": "",
            "interval": 0,
            "previousWin": 0,
            "followingWin": 0
         }
        ]
    }