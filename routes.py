from flask import Blueprint, request, jsonify
from app.model import summarize_text

summarize_blueprint = Blueprint("summarize_blueprint", __name__)
home_blueprint = Blueprint("home_blueprint", __name__)


@home_blueprint.route("/", methods=["POST"])
def home():
    # try:
    #     input_text = request.json.get("text")
    #     print(input_text)
    #     text = f"I am {input_text}"
    #     return text
    #
    # except Exception as e:
    #     print(f"Home Error : {e}")
    #     return jsonify({"error": "Internal server error"}), 500

    try:
        input_text = request.json.get("text")
        print(input_text)

        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        summary = summarize_text(input_text)
        print(summary)
        return jsonify(summary)

    except Exception as e:
        print(f"Error during summarization: {e}")
        return jsonify({"error": "Internal server error"}), 500


# @summarize_blueprint.route("/summarize", methods=["POST"])
# def summarize():
#     try:
#         input_text = request.json.get("text")
#         print(input_text)
#
#         if not input_text:
#             return jsonify({"error": "No text provided"}), 400
#
#         summary = summarize_text(input_text)
#
#         return summary
#
#     except Exception as e:
#         print(f"Error during summarization: {e}")
#         return jsonify({"error": "Internal server error"}), 500
