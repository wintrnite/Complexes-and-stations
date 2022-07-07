import math

SRID_3857 = 3857
SRID_4326 = 4326
MAX_DISTANCE = 1000
DISTORTION_COEFFICIENT = math.cos(math.radians(42.3521))
ANSWER_CSV_HEADER = ['Название_ЖК', 'name', 'distance']
DISTANCE_LABEL = 'distance'
ANSWER_PATH = 'answer.csv'
