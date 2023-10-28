from operator import itemgetter

class Director:
    def __init__(self, id_, fio_, orchestra_id_, salary_):
        self.id = id_
        self.fio = fio_
        self.orchestra_id = orchestra_id_
        self.salary = salary_

class Orchestra:
    def __init__(self, id_, name_):
        self.id = id_
        self.name = name_

class OrcDir:
    def __init__(self, orchestra_id_, director_id_):
        self.orchestra_id = orchestra_id_
        self.director_id = director_id_

def task1(mass):
    print("Задание №1")
    for i in mass:
        if i[2].startswith('А'):
            print('ФИО: {}, Оркестр: {}'.format(i[2], i[3]))
    print('')

def task2(mass):
    print("Задание №2")
    mass_help = dict()
    for i in mass:
        if i[3] not in mass_help:
            mass_help[i[3]] = i[4]
        else:
            mass_help[i[3]] = min(mass_help[i[3]], i[4])
    mass_help = sorted(mass_help.items(), key = lambda item: item[1])
    for i in mass_help:
        print('Оркестр: {}, Минимальная зарплата: {}'.format(i[0], i[1]))
    print('')

def task3(mass):
    print("Задание №3")
    mass = sorted(mass, key = itemgetter(2))
    for i in mass:
        print('ФИО: {}, Оркестр: {}'.format(i[2], i[3]))
    print('')
            
def main():
    orchestras = [
        Orchestra(1, "Первый"),
        Orchestra(2, "Ленина"),
        Orchestra(3, "Октябрьский"),
        Orchestra(4, "Симфонический"),
        Orchestra(5, "Оркестр имени Некрасова")]

    directors = [
        Director(1, "Иванов Сергей Викторович", 1, 245000),
        Director(2, "Смирнов Александр Игоревич", 1, 372500),
        Director(3, "Абрамов Дмитрий Алексеевич", 1, 198000),
        Director(4, "Петров Андрей Сергеевич", 2, 415000),
        Director(5, "Соколов Владимир Николаевич", 2, 286000),
        Director(6, "Михайлов Иван Васильевич", 2, 595000),
        Director(7, "Анатольев Алексей Александрович", 3, 162000),
        Director(8, "Абакян Денис Павлович", 3, 329000),
        Director(9, "Волков Александр Владимирович", 3, 443000),
        Director(10, "Козлов Дмитрий Иванович", 4, 217500),
        Director(11, "Николаев Андрей Петрович", 4, 525000),
        Director(12, "Морозов Максим Сергеевич", 4, 342000),
        Director(13, "Некрасов Иван Олегович", 5, 267500),
        Director(14, "Андреев Артем Николаевич", 5, 383000),
        Director(15, "Семёнов Антон Александрович", 5, 295000)]

    connections = [
        OrcDir(1, 1),
        OrcDir(1, 2),
        OrcDir(1, 3),
        OrcDir(2, 4),
        OrcDir(2, 5),
        OrcDir(2, 6),
        OrcDir(3, 7),
        OrcDir(3, 8),
        OrcDir(3, 9),
        OrcDir(4, 10),
        OrcDir(4, 11),
        OrcDir(4, 12),
        OrcDir(5, 13),
        OrcDir(5, 14),
        OrcDir(5, 15)]
    
    main_list = list()
    for i in directors:
        for j in orchestras:
            if i.orchestra_id == j.id:
                main_list.append((i.id, j.id, i.fio, j.name, i.salary))
    task1(main_list)
    task2(main_list)
    task3(main_list)
    

if __name__ == '__main__':
    main()

