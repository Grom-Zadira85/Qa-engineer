"""      ===========   3.4 Использование фикстур в PyTest  ==============
                            Задание: область видимости фикстур

У нас есть набор тестов, который использует несколько фикстур. Посчитайте, сколько смайликов будет напечатано при 
выполнении этого тестового класса? """

import pytest

smile_list = []


def pytest_unconfigure(config):
    print("=====")


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    print("входим в session", smile_list)
    yield
    print("выходим из session ", smile_list)


@pytest.fixture(scope="class")
def prepare_faces():
    smile_list.append("^_^")
    print("^_^", "\n")
    yield
    smile_list.append(":3")
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    smile_list.append(":)")
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    smile_list.append(":-Р")
    print(":-Р", "\n")


class TestPrintSmilingFaces2:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass
