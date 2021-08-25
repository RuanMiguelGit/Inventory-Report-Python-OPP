import json
import csv
# import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def get_list_by_file_path(cls, path):
        with open(path, mode="r") as csv_or_json_content:
            if path.endswith(".json"):
                return json.load(csv_or_json_content)
            elif path.endswith(".csv"):
                return list(csv.DictReader(csv_or_json_content))
            # elif path.endswith(".xml"):
            #     to_dict = xmltodict.parse(csv_or_json_content.read())
            #     return [dict(item) for item in to_dict["dataset"]["record"]]
            else:
                return None

    @classmethod
    def import_data(cls, path, report_type):
        readed_content = cls.get_list_by_file_path(path)
        if report_type == "simples":
            return SimpleReport.generate(readed_content)
        elif report_type == "completo":
            return CompleteReport.generate(readed_content)
        return None
