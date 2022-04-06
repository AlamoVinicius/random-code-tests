import os

number2 = 10
def newReservation(number) -> bool:
    if number != number2:
        return True
    else:
        return False



free_hour = newReservation(10)
print(free_hour)
name = "Álamo"
reservation_timeStart = 13
reservation_timeEnd = 18
user = input("Digite o nome do usuário que irá reservar o sistema: ")
print(
    f"Horários reservados para maca 1 de {reservation_timeStart} as {reservation_timeEnd}")
newReservation_start = int( input("Escolha o um horário para reservar a maca: "))
   
if newReservation_start > reservation_timeStart and newReservation_start < reservation_timeEnd:
    print(f"horário já reservado por {name}")
else:
    newReservation_end = int(input("Digite o horário final da reserva: "))
    if newReservation_end < newReservation_start:
        os.system('cls')
        print("Não é possivel selecionar um horário final menor que o horário inicial!")
    elif newReservation_end - newReservation_start > 6:
        os.system('cls')
        print("Não é possivel selecionar mais que 6 horas para uma reserva!")
    elif newReservation_end > reservation_timeStart and newReservation_end < reservation_timeEnd:
        os.system('cls')
        print("Não é possivel selecionar horário final pois ja se encontra reservado.")
    else:
        os.system('cls')
        print( f"Horário reservado com sucesso por: {user} das {newReservation_start} as {newReservation_end}")




           
# lógica basica port tras do script de reserva que iremos desenvolver para o app do estudio 
# É necessário implementar as funções data base e uma interface amigável para funcionamento 
# tecnologias considerada para o desenvolvimento do sistema: 
'''
    front end => react.js/ next.js para versão web com servidor node js que irá fazer conexão com o banco de dados, tambem irá fazer toda a lógica de organização para os reservamento das estações de trabalho do estudio, assim como tambem irar gerar os arquivos html css para a página, ela precisa ser focada em versão mobile, será o ponto principal 
    database => node js / mongo db
    aplicativo mobile => react-native
    aplicativo desktop => electron ou csharp .net
    apis a considerar => uma api com a apresentação de um calendário para ficar mais facil de pegar os parâmetros
    apis de validação registro de usuários. 
'''