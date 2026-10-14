import pytest

from process import process


# Etapa 1 - Cobertura de sentencias (Statement Coverage)
# Con un valor positivo y par se ejecutan las sentencias S1 a S7.
@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"]),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected
