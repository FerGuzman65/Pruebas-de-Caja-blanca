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


# Etapa 3 - Cobertura de caminos (Path Coverage)
# Cada valor puede tomar 4 rutas segun las decisiones D1 y D2:
#   A: 2  -> D1=V, D2=V -> ["positivo", "par"]
#   B: 1  -> D1=V, D2=F -> ["positivo"]
#   C: -2 -> D1=F, D2=V -> ["par"]
#   D: -1 -> D1=F, D2=F -> []
# Con listas de 2 valores existen 4 x 4 = 16 caminos posibles.
@pytest.mark.path
@pytest.mark.parametrize("values, expected", [
    ([2, 2], ["positivo", "par", "positivo", "par"]),   # A-A
    ([2, 1], ["positivo", "par", "positivo"]),          # A-B
    ([2, -2], ["positivo", "par", "par"]),              # A-C
    ([2, -1], ["positivo", "par"]),                     # A-D
    ([1, 2], ["positivo", "positivo", "par"]),          # B-A
    ([1, 1], ["positivo", "positivo"]),                 # B-B
    ([1, -2], ["positivo", "par"]),                     # B-C
    ([1, -1], ["positivo"]),                            # B-D
    ([-2, 2], ["par", "positivo", "par"]),              # C-A
    ([-2, 1], ["par", "positivo"]),                     # C-B
    ([-2, -2], ["par", "par"]),                         # C-C
    ([-2, -1], ["par"]),                                # C-D
    ([-1, 2], ["positivo", "par"]),                     # D-A
    ([-1, 1], ["positivo"]),                            # D-B
    ([-1, -2], ["par"]),                                # D-C
    ([-1, -1], []),                                     # D-D
])
def test_path_coverage(values, expected):
    assert process(values) == expected
