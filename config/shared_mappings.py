CITY_DICT = {
	'BEIJING': 'PÉKIN',
	'BEIRUT': 'BEYROUTH',
	'BRUSSELS': 'BRUXELLES',
	'COPENHAGEN': 'COPENHAGUE',
	'DEN HAGUE - THE HAGUE': 'LA HAYE',
	'DETROIT': 'DÉTROIT',
	'FRANKFURT': 'FRANCFORT',
	'GENEVA': 'GENÈVE',
	'HANOI': 'HANOÏ',
	'HAVANA': 'LA HAVANE',
	'KINGSTON, JAMAICA': 'KINGSTON, JAMAÏQUE',
	'KUWAIT CITY': 'VILLE DE KOWEÏT',
	'KYIV': 'KIEV',
	'LONDON UK': 'LONDRES, R.-U.',
	'MOSCOW': 'MOSCOU',
	'NATIONAL CAPITAL REGION': 'RÉGION DE LA CAPITALE NATIONALE (RCN)',
	'NATIONAL CAPITAL REGION (NCR)': 'RÉGION DE LA CAPITALE NATIONALE (RCN)',
	'Online': 'En ligne',
	'ORLEANS, Ontario': 'ORLÉANS, Ontario',
	'PANAMA CITY': 'VILLE DE PANAMA',
	'PORT OF SPAIN': 'PORT D\'ESPAGNE',
	'PRETORIA': 'PRÉTORIA',
	'SAN JOSE, CA, USA': 'SAN JOSE, CALIFORNIE',
	'SAN JOSE DEL CABO, MEXICO': 'SAN JOSE DEL CABO, MEXIQUE',
	'SEOUL': 'SÉOUL',
	'SYDNEY, AUSTRALIA': 'SYDNEY, AUSTRALIE',
	'VIENNA': 'VIENNE',
	'WARSAW': 'VARSOVIE'
}


def city_map(my_city):
	"""Translate French cities as Cognos does not contain an offering_city_fr field."""
	if my_city in CITY_DICT:
		return CITY_DICT[my_city]
	else:
		return my_city
