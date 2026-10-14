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


# Etapa 2 - Cobertura de ramas (Branch Coverage)
# Cada decision se evalua verdadera y falsa al menos una vez:
# D1 (value > 0) y D2 (value % 2 == 0).
@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"]),   # D1 verdadera, D2 verdadera
    ([-1], []),                   # D1 falsa, D2 falsa
])
def test_branch_coverage(values, expected):
    assert process(values) == expected
