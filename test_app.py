from app import hitung_total_sks, validasi_krs


def test_total_sks():
    data = [{"kode": "A", "sks": 3}, {"kode": "B", "sks": 2}]
    assert hitung_total_sks(data) == 5


def test_krs_valid():
    data = [{"kode": "A", "sks": 3}]
    assert validasi_krs(data)[0] is True


def test_krs_kosong():
    assert validasi_krs([])[0] is False


def test_krs_ganda():
    data = [{"kode": "A", "sks": 3}, {"kode": "A", "sks": 3}]
    assert validasi_krs(data)[0] is False


def test_krs_melebihi_batas():
    data = [{"kode": str(i), "sks": 5} for i in range(5)]
    assert validasi_krs(data)[0] is False
