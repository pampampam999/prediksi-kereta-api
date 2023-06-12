
stasiun = {
        'magetan':['madiun'],
        'madiun': ['magetan', 'nganjuk'],
        'nganjuk': ['madiun', 'kertosono'],
        'kertosono': ['nganjuk','jombang','kediri'],
        'jombang': ['kertosono','mojokerto'],
        'kediri': ['kertosono'],
        'mojokerto': ['jombang','surabaya']}

def temukan_jalur(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    #print (jalur)
    if awal == akhir:
        return jalur
    if not graf.__contains__(awal):
        return None
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_baru = temukan_jalur(graf, titik, akhir, jalur)
            if jalur_baru: return jalur_baru
    return None

def temukan_semua_jalur(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir:
        return [jalur]
    if not graf.__contains__(awal):
        return []
    semua_jalur = []
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_jalur = temukan_semua_jalur(graf, titik, akhir, jalur)
            for jalur_baru in jalur_jalur:
                semua_jalur.append(jalur_baru)
    return semua_jalur

#print(temukan_jalur(stasiun, 'A', 'D'))
print(temukan_semua_jalur(stasiun, 'madiun', 'surabaya'))
