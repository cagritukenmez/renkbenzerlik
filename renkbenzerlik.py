def arrange(item,boyut,min,max):
  item_count,i=len(item),0

  for i in range(boyut):
    if(i<=item_count):
      item[i] = item[i]/((max-min)/100)
    else:
      item[i]=50/((max-min)/100)
  return item

def kokal(x):
  return x**(1/2)

def usal(x):
  return x**2

def vectorSimilarity(a,b):
  if len(a) != len(b):
    return -1
  else:
    len_ = len(a)
    total = 0
    for i in range(len_):
      total += usal(b[i]-a[i])
    distance = kokal(total)
    max_dist = 0
    for i in range(len_):
      max_dist += usal(100)
    max_dist = kokal(max_dist)
    return 1-(distance/max_dist)

turuncu = [255,170,0]
kirmizi = [255,0,0]
koyuKirmizi=[181,25,25]
kahverengi=[48,34,15]
siyah=[0,0,0]
beyaz=[255,255,255]
gri=[82,82,82]

turuncu_normalize = arrange(turuncu,3,0,255)
kirmizi_normalize = arrange(kirmizi,3,0,255)
koyuKirmizi_normalize = arrange(koyuKirmizi,3,0,255)
kahverengi_normalize = arrange(kahverengi,3,0,255)
siyah_normalize = arrange(siyah,3,0,255)
beyaz_normalize = arrange(beyaz,3,0,255)
gri_normalize = arrange(gri,3,0,255)

benzerlik_orani = vectorSimilarity(koyuKirmizi_normalize,kirmizi_normalize)
print("koyu kırmızı ve kırmızı")
print(benzerlik_orani)
benzerlik_orani = vectorSimilarity(koyuKirmizi_normalize,beyaz_normalize)
print("koyu kırmızı ve beyaz")
print(benzerlik_orani)
benzerlik_orani = vectorSimilarity(siyah_normalize,beyaz_normalize)
print("siyah ve beyaz")
print(benzerlik_orani)

benzerlik_orani = vectorSimilarity(turuncu_normalize,turuncu_normalize)
print("turuncu ve turuncu ")
print(benzerlik_orani)
