from datetime import datetime, timedelta
from project import row_data, new_end_date, new_row_dv


def test_row_data():
    # date_format = "%Y-%m-%d"
    date_start = datetime.now().date()
    date_ndays = date_start + timedelta(days=7)
    date_start = f'{date_start}'
    date_ndays = f'{date_ndays}'
    default_value = ['Medicine Name', 'Daily', '7', date_start, date_ndays]
    output =  row_data(default_value)
    assert output == ['Medicine Name', 'Daily', 7, date_start, date_ndays]


def test_new_end_date():
    date_start_str = '2023-10-10'
    n = 7
    assert new_end_date(date_start_str, n) == '2023-10-17'


def test_new_row_dv():
    n = 7
    date_now = datetime.now().date()
    date_ndays = date_now + timedelta(days=n)
    date_now = f'{date_now}'
    date_ndays = f'{date_ndays}'
    assert new_row_dv(n) == ['Medicine Name', 'Daily', str(n), date_now, date_ndays]
