import pytest
from app import check_document_existance, get_doc_owner_name, delete_doc, get_doc_shelf

# Task 1
def test_check_document_existance():
    result = check_document_existance("10006")
    assert True == result

@pytest.mark.parametrize('number, result', [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов")

])
def test_get_doc_owner_name(number, result):
    res = get_doc_owner_name(number)
    assert result == res


def test_delete_doc():
    res = delete_doc(["2207 876234"])
    assert res != True


@pytest.mark.parametrize('user_doc_number, result', [('10006', '2'), ('2207 876234', '1')])
def test_get_doc_shelf(user_doc_number, result):
    res =get_doc_shelf(user_doc_number)
    assert res == result


