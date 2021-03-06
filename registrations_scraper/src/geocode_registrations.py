"""Geocode offering and learner locations with the Google Geocoding API."""
import logging
import os
import pickle
import pandas as pd
from config import shared_directories
from utils.geocoding.geocoding import get_lat_lng
from utils.utils import _check_col_in_valid_range
from registrations_scraper.config import directories

# Instantiate logger
logger = logging.getLogger(__name__)

### IMPORT RAW DATA ###
os.chdir(directories.PROCESSED_DIR)
regs = pd.read_csv('lsr_processed.csv', sep=',', index_col=False, encoding='utf-8',
				   keep_default_na=False)
if not regs.shape[0] > 0:
	logger.critical('Failure: lsr_processed.csv is empty.')
	exit()

logger.debug('1/5: Data imported.')

# Load pickle for memoization
os.chdir(shared_directories.GEO_PICKLE_DIR)
with open('geo_dict.pickle', 'rb') as f:
	geo_dict = pickle.load(f)

logger.debug('2/5: Pickle imported.')

# New cities that failed to geocode/json
fail_ctr = 0

# Add offering latitude and longitude
regs['offering_lat'] = regs.apply(lambda x: get_lat_lng(x['offering_city_en'], x['offering_province_en'], geo_dict, fail_ctr)['lat'], axis=1)
regs['offering_lng'] = regs.apply(lambda x: get_lat_lng(x['offering_city_en'], x['offering_province_en'], geo_dict, fail_ctr)['lng'], axis=1)

# Add learner latitude and longitude
regs['learner_lat'] = regs.apply(lambda x: get_lat_lng(x['learner_city_en'], x['learner_province_en'], geo_dict, fail_ctr)['lat'], axis=1)
regs['learner_lng'] = regs.apply(lambda x: get_lat_lng(x['learner_city_en'], x['learner_province_en'], geo_dict, fail_ctr)['lng'], axis=1)

# Ensure new columns contain valid coördinates
if not _check_col_in_valid_range(regs['offering_lat'].unique(), -180, 180) and \
	   _check_col_in_valid_range(regs['offering_lng'].unique(), -180, 180) and \
	   _check_col_in_valid_range(regs['learner_lat'].unique(), -180, 180) and \
	   _check_col_in_valid_range(regs['learner_lng'].unique(), -180, 180):
	logger.critical('Failure: Invalid coördinates.')
	exit()

logger.debug('3/5: New columns created.')

# Export geo_dict to pickle for future re-use
os.chdir(shared_directories.GEO_PICKLE_DIR)
with open('geo_dict.pickle', 'wb') as f:
	pickle.dump(geo_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

logger.debug('4/5: Pickle exported.')

# Export results as CSV
os.chdir(directories.PROCESSED_DIR)
regs.to_csv('lsr_processed_geo.csv', sep=',', encoding='utf-8', index=False,
			quotechar='"', line_terminator='\r\n')

logger.debug('5/5: Data exported.')
