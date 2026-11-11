"""Aplikasi KRS sederhana untuk simulasi DevOps (UTS Cloud dan DevOps)."""
import threading

MAKS_SKS = 24
DATA_KRS = {}
_kunci = threading.Lock()


def hitung_total_sks(daftar_mk):
    """Menghitung total SKS dari daftar mata kuliah."""
    return sum(mk["sks"] for mk in daftar_mk)


def validasi_krs(daftar_mk):
    """KRS valid jika tidak kosong, tidak ada duplikat, dan total SKS tidak melebihi batas."""
    if not daftar_mk:
        return False, "KRS kosong"
    kode = [mk["kode"] for mk in daftar_mk]
    if len(kode) != len(set(kode)):
        return False, "Ada mata kuliah ganda"
    if hitung_total_sks(daftar_mk) > MAKS_SKS:
        return False, "Total SKS melebihi batas"
    return True, "KRS valid"


def simpan_krs(nim, daftar_mk):
    """Menyimpan KRS dengan kunci (lock) agar aman saat diakses bersamaan."""
    valid, pesan = validasi_krs(daftar_mk)
    if not valid:
        return False, pesan
    with _kunci:
        DATA_KRS[nim] = daftar_mk
    return True, "KRS tersimpan"


if __name__ == "__main__":
    contoh = [
        {"kode": "IF101", "nama": "Cloud Computing", "sks": 3},
        {"kode": "IF102", "nama": "DevOps", "sks": 3},
    ]
    print(hitung_total_sks(contoh))
    print(simpan_krs("248160066", contoh))
