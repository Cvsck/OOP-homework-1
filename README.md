# OOP-homework-1
# Установка всех зависимостей 
'''
pip install poetry
python.exe -m pip install --upgrade pip
poetry init
python -m venv env 
.\env\Scripts\activate
pip install isort black flake8 pep8
python.exe -m pip install --upgrade pip
pip install requests
pip install mypy
pip install pytest
pip install pytest-cov
pip install pytest-html
'''
# После обновления pyproject.toml, установите все зависимости:
'''
poetry install
'''
# Запуск тестов с отчетом покрытия и HTML отчетом
'''
pytest --cov=src --cov-report=html:htmlcov --html=report.html
'''

# Создание модуля
'''
main
'''
# В папке Tests добавлены тесты к модулям
'''
test_main.py

'''