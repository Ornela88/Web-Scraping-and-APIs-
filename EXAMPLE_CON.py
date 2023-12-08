schema="gans"
host="localhost aws"
user="admin" #root
password="psw"
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
