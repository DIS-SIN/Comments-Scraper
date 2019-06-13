from comments_scraper.config.directories import PROCESSED_DIR
from utils.db import get_db, run_mysql

# Store DB connection in global var to avoid reconnecting after each query
cnx = get_db()
print('1/6: Connected to DB.')

# MySQL requires paths with forward slashes
PROCESSED_DIR = PROCESSED_DIR.replace('\\', '/')

drop_existing_table = """
	DROP TABLE IF EXISTS comments;
"""

create_table = """
	CREATE TABLE comments(
		course_code VARCHAR(20),
		survey_id VARCHAR(15),
		fiscal_year VARCHAR(9),
		quarter VARCHAR(5),
		learner_classif VARCHAR(80),
		offering_city_en VARCHAR(60),
		original_question VARCHAR(60),
		text_answer TEXT,
		offering_city_fr VARCHAR(60),
		short_question VARCHAR(60),
		text_answer_fr VARCHAR(90),
		overall_satisfaction TINYINT,
		stars TINYINT,
		PRIMARY KEY(survey_id, original_question)
	);
"""

load_data = """
	LOAD DATA LOCAL INFILE '{0}/comments_processed_ML.csv'
	INTO TABLE comments
	FIELDS OPTIONALLY ENCLOSED BY '"'
	TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
	IGNORE 1 LINES;
""".format(PROCESSED_DIR)

create_index = """
	CREATE INDEX idx_cc_sq ON comments(course_code, short_question);
"""

try:
	run_mysql(cnx, drop_existing_table)
	print('2/6: Dropped existing table.')
	run_mysql(cnx, create_table)
	print('3/6: Created new table.')
	run_mysql(cnx, load_data)
	print('4/6: Data loaded.')
	run_mysql(cnx, create_index)
	print('5/6: Index created.')
except Exception as e:
	print('We\'re having tremendous problems with: {0}'.format(e))
finally:
	cnx.close()
	print('6/6: Connection closed.')
