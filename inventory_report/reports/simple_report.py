import json
from datetime import datetime, date
from collections import Counter


class report_definition:
    @classmethod
    def oldest_fabrication_date(cls, info):
        fabrication = []
        for data in info:
            fabrication.append(data["data_de_fabricacao"])
        sorted_list = sorted(
            fabrication, key=lambda t: datetime.strptime(t, "%Y-%m-%d")
        )
        return sorted_list[0]

    @classmethod
    def next_due_date(cls, info):
        good_through = []
        for data in info:
            if data["data_de_validade"] > str(date.today()):
                good_through.append(data["data_de_validade"])
            sorted_list = sorted(
                good_through, key=lambda t: datetime.strptime(t, "%Y-%m-%d")
            )
        return sorted_list[0]

    @classmethod
    def most_current_company(cls, info):
        companies = []
        for data in info:
            companies.append(data["nome_da_empresa"])
        most = Counter(companies)
        most.most_common()
        return most.most_common()[0][0]


class SimpleReport:
    @classmethod
    def generate(self, file):
        with open(file) as report_file:
            content = json.load(report_file)
            by_age = report_definition.oldest_fabrication_date(content)
            by_due_date = report_definition.next_due_date(content)
            by_company_ocurrence = report_definition.most_current_company(
                content
            )
            report1 = f"Data de fabricação mais antiga: {by_age}"
            report2 = f"Data de validade mais próxima: {by_due_date}"
            report3_text = "Empresa com maior quantidade de produtos estocados"
            report3 = f"{report3_text}: {by_company_ocurrence}"

        return report1, report2, report3


print(SimpleReport.generate("./inventory_report/data/inventory.json"))
