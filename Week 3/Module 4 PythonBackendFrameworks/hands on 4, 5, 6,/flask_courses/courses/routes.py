from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code):
    return jsonify(
        {
            "status": "success",
            "data": data
        }
    ), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return make_response_json([], 200)


@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required"}), 400

    return make_response_json(data, 201)


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    return make_response_json(
        {"course_id": course_id},
        200
    )


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()

    return make_response_json(
        {
            "course_id": course_id,
            "updated_data": data
        },
        200
    )


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    return make_response_json(
        {"course_id": course_id},
        200
    )