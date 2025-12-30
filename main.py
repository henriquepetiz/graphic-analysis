# main.py

from dados_jogos import AnalisadorJogos
import testes_jogos
import unittest
import sys

ARQUIVO_FINAL = 'extracted_data/steam_games.csv'

print("====================================================")
print("--- 1. EXECUTANDO TESTES DE UNIDADE COM A AMOSTRA ---")
print("====================================================")

suite = unittest.TestLoader().loadTestsFromModule(testes_jogos)
runner = unittest.TextTestRunner(verbosity=2)
resultado_testes = runner.run(suite)

if not resultado_testes.wasSuccessful():
    print("\n\nERRO FATAL: OS TESTES DE UNIDADE FALHARAM!")
    sys.exit(1)
else:
    print("\nTODOS OS TESTES PASSARAM! O código é confiável.")

print("\n" + "=" * 50)
print("--- 2. ANÁLISE FINAL COM O ARQUIVO COMPLETO ---")
print("=" * 50)

try:
    analisador = AnalisadorJogos()
    analisador.carregar_dados(ARQUIVO_FINAL)

    print(f"Dados Carregados do Arquivo Completo: {ARQUIVO_FINAL}\n")

    print("## Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?")
    res1 = analisador.consultar_percentual_gratis()
    print(f"> Resposta: Dos {res1['Total']} jogos analisados, **{res1['Gratuitos']}%** são gratuitos e **{res1['Pagos']}%** são pagos.")
    print("-" * 20)

    print("\n## Pergunta 2: Qual o ano com o maior número de novos jogos? (Com empate)")
    res2 = analisador.consultar_ano_maior_lancamento()
    print(f"> Resposta: O(s) ano(s) com o maior número de lançamentos ({res2['Contagem']} jogos) é(são): **{', '.join(res2['Ano(s)'])}**.")
    print("-" * 20)

    print("\n## Pergunta 3: Qual é a desenvolvedora com o maior número de jogos com Metacritic >= 90?")
    res3 = analisador.consultar_dev_metacritic_90()
    print(f"> Resposta: A desenvolvedora com mais jogos aclamados ({res3['Contagem']} títulos com Metacritic >= 90) é **{res3['Desenvolvedora']}**.")
    print("-" * 20)

except Exception as e:
    print(f"\nERRO FATAL NA EXECUÇÃO PRINCIPAL: {e}")

print("\n[PROGRAMA CONCLUÍDO]")
