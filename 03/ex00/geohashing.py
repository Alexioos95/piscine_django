import sys

def geohash(latitude, longitude, precision=9):
	lat_range = [-90.0, 90.0]
	lon_range = [-180.0, 180.0]
	bit = 0
	val = 0
	is_lon = True
	base = "0123456789bcdefghjkmnpqrstuvwxyz"
	res = []

	while len(res) < precision:
		if is_lon:
			mid = (lon_range[0] + lon_range[1]) / 2
			if longitude > mid:
				val = (val << 1) | 1
				lon_range[0] = mid
			else:
				val = (val << 1)
				lon_range[1] = mid
		else:
			mid = (lat_range[0] + lat_range[1]) / 2
			if latitude > mid:
				val = (val << 1) | 1
				lat_range[0] = mid
			else:
				val = (val << 1)
				lat_range[1] = mid
		bit += 1
		if bit == 5:
			res.append(base[val])
			bit = 0
			val = 0
		is_lon = not is_lon
	return ''.join(res)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python3 geohashing.py <latitude> <longitude>")
	else:
		try:
			latitude = float(sys.argv[1])
			longitude = float(sys.argv[2])
			geohash = geohash(latitude, longitude, 9)
			print(f"Geohash: {geohash}")
		except Exception as e:
			print(f"Error: {e}")
