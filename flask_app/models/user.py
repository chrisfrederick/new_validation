from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data["id"],
        self.first_name = data["first_name"],
        self.last_name = data["last_name"],
        self.email = data["email"],
        self.password = data["password"],
        self.created_at = data["created_at"],
        self.updated_at = data["updated_at"]


    @classmethod
    def insert_user(cls, data):
        query = ("INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)")
        return connectToMySQL("login_validation").query_db(query,data)

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        save_id = connectToMySQL("login_validation").query_db(query, data)
        return save_id


    @staticmethod
    def validation(data):
        is_valid = True
        if len(data["first_name"])<5:
            flash("Name must be at least 4 characters.")
            is_valid = False
        if len(data["last_name"])<5:
            flash("Last name must be at least 4 characters")
            is_valid = True
        if len(data["email"])<5:
            flash("Email must be at least 4 characters")
            is_valid = False
        if len(data["password"])<1:
            flash("You mjust enter a password")
            is_valid = False
        return is_valid