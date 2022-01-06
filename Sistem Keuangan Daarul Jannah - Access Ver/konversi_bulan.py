def convert_bln(bulan_str):
    for i in range (len(bulan_str)):
        if bulan_str == 'JANUARI' or 'Januari':
            return 1
        elif bulan_str == 'FEBRUARI' or 'Februari':
            return 2
        elif bulan_str == 'MARET' or 'Maret':
            return 3
        elif bulan_str == 'APRIL' or 'April':
            return 4
        elif bulan_str == 'MEI' or 'Mei':
            return 5
        elif bulan_str == 'JUNI' or 'Juni':
            return 6
        elif bulan_str == 'JULI' or 'Juli':
            return 7
        elif bulan_str == 'AGUSTUS' or 'Agustus':
            return 8
        elif bulan_str == 'SEPTEMBER' or 'September':
            return 9
        elif bulan_str == 'OKTOBER' or 'Oktober':
            return 10
        elif bulan_str == 'NOVEMBER' or 'November':
            return 11
        elif bulan_str == 'DESEMBER' or 'Desember':
            return 12    