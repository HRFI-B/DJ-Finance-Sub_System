def convert_bln(bulan_str):
    for i in range (len(bulan_str)):
        if bulan_str == 'JANUARI':
            return 1
        elif bulan_str == 'FEBRUARI':
            return 2
        elif bulan_str == 'MARET':
            return 3
        elif bulan_str == 'APRIL':
            return 4
        elif bulan_str == 'MEI':
            return 5
        elif bulan_str == 'JUNI':
            return 6
        elif bulan_str == 'JULI':
            return 7
        elif bulan_str == 'AGUSTUS':
            return 8
        elif bulan_str == 'SEPTEMBER':
            return 9
        elif bulan_str == 'OKTOBER':
            return 10
        elif bulan_str == 'NOVEMBER':
            return 11
        elif bulan_str == 'DESEMBER':
            return 12    