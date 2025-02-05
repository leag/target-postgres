import pytest
from target_postgres.postgres import PostgresTarget

@pytest.mark.parametrize("test_date", [
    '2023-01-25 14:11:24',
    '2023-01-25 14:11:24 UTC',
    None,
])
def test_serialize_table_record_datetime_value(test_date):
    result = PostgresTarget.serialize_table_record_datetime_value(None, None, None, None, test_date)
    assert result

def test_invalid_datetime():
    test_date = 'invalid-date'
    with pytest.raises(ValueError):
        PostgresTarget.serialize_table_record_datetime_value(None, None, None, None, test_date)
