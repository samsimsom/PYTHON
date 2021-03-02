import math

## input

# Dairenin çap bilgisi isteniyor.
dairenin_capi = input('Dairenin Çapı : ')

# Dairenin yarıçap hesaplaması yapılıyor.
yari_cap = int(dairenin_capi) / 2

# pi sabiti.
pi = math.pi

# daire alnı hesaplama formülü
alan = int(pi * (yari_cap * yari_cap))

# Sonucu ekrana yadırıyorum
print("Çapı {}cm olan dairenin alanı: {}cm2 dir."
                    .format(dairenin_capi, alan)
                    )

