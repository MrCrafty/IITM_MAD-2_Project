from flask import request, json
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
            return "section already exists"
        section = Section(
            section_name=data["section_name"], description=data["description"])
        db.session.add(section)
        db.session.commit()
        return json.jsonify("{success: True, message: 'Section added Successfully'}")


class Book(Resource):
    def get(self, book_id):
        book = Book.query.filter_by(book_id=book_id).first()
        if (book):
            return book
        return "Book not found"


def initialize_route(api):
    api.add_resource(Sections, '/section')
