from flask import Blueprint, request, json
from . import db
from .models import Section


api = Blueprint("api", __name__)


@api.route("/section", methods=["GET"])
def Sections():
    data = Section.query.all()
    section = []
    for i in data:
        item = {}
        item["section_id"] = i.section_id
        item["section_name"] = i.section_name
        item["description"] = i.description
        section.append(item)
    return section


@api.route("/addsection", methods=["POST"])
def AddSection():
    data = request.get_json()
    sections = list(Section.query.filter_by(section_name=data["section_name"]))
    if (len(sections) > 0):
        return "section already exists"
    section = Section(
        section_name=data["section_name"], description=data["description"])
    db.session.add(section)
    db.session.commit()
    return json.jsonify("{success: True, message: 'Section added Successfully'}")
