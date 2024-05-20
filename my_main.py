#для примера - https://www.youtube.com/watch?v=ij-wNkDF88c&list=PLN0sMOjX-lm5Pz5EeX1rb3yilzMNT6qLM&index=5
import os

from sqlalchemy import and_
# это AND для исп-я внутри запросов
from my_models.database import DATABASE_NAME, Session
import my_models.create_database as db_creator
from my_models.kp_lots import Lots
from my_models.kp_goods import Goods


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()