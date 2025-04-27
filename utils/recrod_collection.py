from .record import Record
import csv


class RecordCollection:
    def __init__(self, records=None):
        self._records = records or []

    def __iter__(self):
        return iter(self._records)

    def __getitem__(self, index):
        return self._records[index]

    def add(self, record):
        if not isinstance(record, Record):
            raise TypeError("Можно добавлять только экземпляры Record")
        self._records.append(record)

    def __repr__(self):
        return f"<{self.__class__.__name__} с {len(self._records)} записями>"

    @classmethod
    def from_csv(cls, filename):
        collection = cls()
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rec = Record(
                    row['№'],
                    row['ФИО'],
                    row['должность'],
                    int(row['трудовой стаж'])
                )
                collection.add(rec)
        return collection

    def save_to_csv(self, filename):
        if not self._records:
            return
        fieldnames = ['№', 'ФИО', 'должность', 'трудовой стаж']
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for rec in self._records:
                writer.writerow({
                    '№': rec.__dict__['№'],
                    'ФИО': rec.__dict__['ФИО'],
                    'должность': rec.__dict__['должность'],
                    'трудовой стаж': rec.__dict__['трудовой стаж']
                })

    @staticmethod
    def sort_by_string(records, field):
        return sorted(records, key=lambda r: getattr(r, field))

    @staticmethod
    def sort_by_numeric(records, field):
        return sorted(records, key=lambda r: getattr(r, field))


class WorkerCollection(RecordCollection):
    def filter_by_experience(self, threshold):
        return [r for r in self._records if r.__dict__['трудовой стаж'] > threshold]

    def filter_by_experience_gen(self, threshold):
        for r in self._records:
            if r.__dict__['трудовой стаж'] > threshold:
                yield r

