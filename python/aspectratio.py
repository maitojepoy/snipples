def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def aspect_ratio(w,h):
	cd = gcd(w,h)
	return w/cd,h/cd

def basis_crop(w1,h1,w2,h2):
	i1 = aspect_ratio(w1,h1)
	i2 = aspect_ratio(w2,h2)
	diffw = i1[0]-i2[0]
	diffh = i1[1]-i2[1]
	if diffw > diffh:
		return 'h'
	else:
		return 'w'