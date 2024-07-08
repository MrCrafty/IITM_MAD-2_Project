from flask import request
from website.util import Message
from . import db
from .models import Section
from flask_restful import Resource


class Sections(Resource):
    def get(self):
        data = Section.query.all()
        section = []
        for i in data:
            item = {}
            item["section_id"] = i.section_id
            item["section_name"] = i.section_name
            item["description"] = i.description
            section.append(item)
        return section

    def post(self):
        data = request.get_json()
        sections = list(Section.query.filter_by(
            section_name=data["section_name"]))
        if (len(sections) > 0):
            return Message("False", "Section already exists")
        section = Section(
            section_name=data["section_name"], description=data["description"])
        db.session.add(section)
        db.session.commit()
        return Message("True", "Section added Successfully")

    def delete(self):
        data = request.get_json()
        section_id = data["section_id"]
        section = Section.query.filter_by(section_id=section_id).first()
        if (section):
            db.session.delete(section)
            db.session.commit()
            return Message(True, "Section deleted Successfully")
        return Message(False, "Section not found")


class Book(Resource):
    def get(self, book_id):
        book = Book.query.filter_by(book_id=book_id).first()
        if (book):
            return book
        return "Book not found"

    def post(self):
        data = request.get_json()
        books = list(Book.query.filter_by(book_name=data["book_name"]))
        if (len(books) > 0):
            return Message(False, "Book already exists")
        book = Book(book_name=data["book_name"], section_id=data["section_id"],
                    content=data["content"], author=data["author"])
        db.session.add(book)
        db.session.commit()
        return Message(True, "Book added Successfully")


def initialize_api(api):
    api.add_resource(Sections, '/section')
    api.add_resource(Book, '/book')
