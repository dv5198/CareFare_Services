#!/usr/bin/python
import datetime
from db import *
from models.category import Category
from models.country import Country

category_fetch = """SELECT * FROM public.category_details where is_active=$1 ORDER BY category_id ASC """
category_fetch_count = (
    """SELECT COUNT(*) FROM public.category_details where is_active=$1"""
)
category_insert = """INSERT INTO public.category_details(
	category_id, category, category_description, is_active, created_at, updated_at)
	VALUES ($1, $2, $3, $4, $5, $6);"""


def add_category(conn, category, category_description, is_active):

    cursor = conn.cursor()
    cursor.execute("SELECT NEXTVAL('category_sequence')")
    category_id = cursor.fetchone()[0]
    now_Date = datetime.datetime.now()
    cursor.execute(
        category_insert,
        (category_id, category, category_description, is_active, now_Date, now_Date),
    )
    conn.commit()
    res = []
    res.append(
        Category(
            {
                "category_id": category_id,
                "category": category,
                "description": category_description,
                "status": is_active,
            }
        )
    )
    return res


def fetch_category(conn):
    cursor = conn.cursor()
    cursor.execute(category_fetch)
    res = []
    for rowTuple in cursor.fetchall():
        row = list(rowTuple)

        res.append(
            Category(
                {
                    "category_id": row[0],
                    "category": row[1],
                    "description": row[2],
                    "status": row[3],
                }
            )
        )

    conn.commit()
    return res


def get_category():

    conn = getPostgresCon()
    get_data = fetch_category(conn)
    conn.close()
    return get_data
