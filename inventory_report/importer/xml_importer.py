from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".json"):
            raise ValueError("Arquivo inválido")
        if file_name.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        if file_name.endswith(".xml"):
            return Inventory.get_list_by_file_path(file_name)
