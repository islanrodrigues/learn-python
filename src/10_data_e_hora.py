# Para se trabalhar com data e hora é preciso importar módulos nativos do Python oriundos do package 'datetime'.
from datetime import date, time, datetime, timedelta

# === Trabalhando apenas com data (date) ===
# Buscando a data atual através do método today()
data_atual = date.today()
print(data_atual)
print(type(data_atual))  # saída -> <class 'datetime.date'>

# Formatando a data através do método strftime(), informando o formato através de diretivas.
data_atual_format = data_atual.strftime("%d/%m/%Y")
print(data_atual_format)
print(type(data_atual_format))  # saída -> <class 'str'>


print("- - - - - - - - - - -")


# === Trabalhando apenas com hora (time) ===
# Criando uma informação em formato de horário.
horario = time(hour=16, minute=25, second=12)
print(horario)
print(type(horario))  # saída -> <class 'datetime.time'>

# Formatando a hora.
horario_format = horario.strftime("%Hh:%Mmin:%Sseg")
print(horario_format)
print(type(horario_format))  # saída -> <class 'str'>


print("- - - - - - - - - - -")


# === Trabalhando com data e hora (datetime) ===
# Buscando a data e hora atual através do método now().
data_hora_atual = datetime.now()
print(data_hora_atual)
print(type(data_hora_atual))  # saída -> <class 'datetime.datetime'>

data_hora_especifica = datetime(2021, 3, 20, 17, 25, 12)
print(data_hora_especifica)  # saída -> 2021-03-20 17:25:12

# Formatando data e hora.
data_hora_format = data_hora_atual.strftime("%d/%m/%Y %Hh:%Mmin:%Sseg")
print(data_hora_format)

# Capturando informaçõe isoladas.
dia = data_hora_atual.day
print("Dia:", dia)

dia_semana = data_hora_atual.weekday()
print("Dia da Semana:", dia_semana)

mes = data_hora_atual.month
print("Mês:", mes)

ano = data_hora_atual.year
print("Ano:", ano)

hora = data_hora_atual.hour
print("Hora", hora)

minuto = data_hora_atual.minute
print("Minuto:", minuto)

# Retornando somente as informações de data ou somente as informações de hora.
somente_data = data_hora_atual.date()
print(somente_data)
print(type(somente_data))  # saída -> <class 'datetime.date'>

somente_horario = data_hora_atual.time()
print(somente_horario)
print(type(somente_horario))  # saída -> <class 'datetime.time'>


print("- - - - - - - - - - -")


# Convertendo de string para datetime através do método strptime(), informando como parâmetro a string que quer converter e o formato em que ela se encontra.
data_hora_str = "20/03/2021 17:43:55"
data_hora_convertida = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M:%S")

print(data_hora_convertida)
print(type(data_hora_convertida))  # saída -> <class 'datetime.datetime'>

# Realizando adição e subtração através do timedelta
nova_data_1 = data_hora_convertida + timedelta(days=365)
print(nova_data_1)  # saída -> 2022-03-2- 17:43:55

nova_data_2 = data_hora_convertida - timedelta(days=5, hours=10, minutes=40, seconds=55)
print(nova_data_2)  # saída -> 2021-03-15 07:03:00
