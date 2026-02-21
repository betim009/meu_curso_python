from db import connection
from migrations import run_migrations
from seeders import run_seeders
from controller import *

if __name__ == "__main__":
    showTables()
    # print(select_all_produtos())