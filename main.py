# Importar o App, Builder (GUI) Graphic User Interface
# Criar o aplicativo
# Criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file(r'kivy\Cotacao_moedas\tela.kv')


class Aplicativo(App):

    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R$ {self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"BTC R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"ETH R$ {self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f"{moeda}BRL"]['bid']
        return cotacao


Aplicativo().run()
