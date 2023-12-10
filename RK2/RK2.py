import unittest
from main import *

class TestDirector(unittest.TestCase):

    def test_director_creation(self):
        d = Director(1, "Иванов Сергей Викторович", 1, 245000)
        self.assertEqual(d.id, 1)
        self.assertEqual(d.fio, "Иванов Сергей Викторович")
        self.assertEqual(d.orchestra_id, 1)
        self.assertEqual(d.salary, 245000)


class TestOrchestra(unittest.TestCase):

    def test_orchestra_creation(self):
        o = Orchestra(1, "Первый")
        self.assertEqual(o.id, 1)
        self.assertEqual(o.name, "Первый")


class TestOrcDir(unittest.TestCase):

    def test_connection_creation(self):
        c = OrcDir(1, 1)
        self.assertEqual(c.orchestra_id, 1)
        self.assertEqual(c.director_id, 1)

class TestTaskExecution(unittest.TestCase):
    def setUp(self):
        self.orchestras, self.directors, self.connections = data_generate()
        self.main_list = list()
        for i in self.directors:
            for j in self.orchestras:
                if i.orchestra_id == j.id:
                    self.main_list.append((i.id, j.id, i.fio, j.name, i.salary))

    def test_task1(self):
        test_result = task1(self.main_list)
        goal_result = [["Абрамов Дмитрий Алексеевич", "Первый"],
                        ["Анатольев Алексей Александрович", "Октябрьский"],
                        ["Абакян Денис Павлович", "Октябрьский"],
                        ["Андреев Артем Николаевич", "Оркестр имени Некрасова"]]
        self.assertEqual(test_result, goal_result)

    def test_task2(self):
        test_result = task2(self.main_list)
        goal_result = [['Октябрьский', 162000],
                       ['Первый', 198000],
                       ['Симфонический', 217500],
                       ['Оркестр имени Некрасова', 267500],
                       ['Ленина', 286000]]
        self.assertEqual(test_result, goal_result)

    def test_task3(self):
        test_result = task3(self.main_list)
        goal_result = [['Абакян Денис Павлович', 'Октябрьский'],
                       ['Абрамов Дмитрий Алексеевич', 'Первый'],
                       ['Анатольев Алексей Александрович', 'Октябрьский'],
                       ['Андреев Артем Николаевич', 'Оркестр имени Некрасова'],
                       ['Волков Александр Владимирович', 'Октябрьский'],
                       ['Иванов Сергей Викторович', 'Первый'],
                       ['Козлов Дмитрий Иванович', 'Симфонический'],
                       ['Михайлов Иван Васильевич', 'Ленина'],
                       ['Морозов Максим Сергеевич', 'Симфонический'],
                       ['Некрасов Иван Олегович', 'Оркестр имени Некрасова'],
                       ['Николаев Андрей Петрович', 'Симфонический'],
                       ['Петров Андрей Сергеевич', 'Ленина'],
                       ['Семёнов Антон Александрович', 'Оркестр имени Некрасова'],
                       ['Смирнов Александр Игоревич', 'Первый'],
                       ['Соколов Владимир Николаевич', 'Ленина']]
        self.assertEqual(test_result, goal_result)

if __name__ == "__main__":
    unittest.main()
