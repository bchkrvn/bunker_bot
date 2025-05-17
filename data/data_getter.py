import json
import os
import random


class DataGetter:
    files = {
        'situation': 'situations.json',
        'rules': 'rules.json',
        'rooms': 'rooms.json',
        'speciality': 'speciality.json',
        'health': 'health.json',
        'knowledge': 'knowledge.json',
        'qualities': 'qualities.json',
        'hobbies': 'hobbies.json',
        'phobias': 'phobias.json',
        'baggage': 'baggage.json',
        'fact': 'fact.json',
    }

    @classmethod
    def get_situation(cls) -> dict:
        values = cls._read_data('situation')
        return random.choice(values)

    @classmethod
    def get_rules(cls) -> dict:
        values = cls._read_data('rules')
        random.shuffle(values)
        return {'rules': '\n'.join(values[:5])}

    @classmethod
    def get_rooms(cls) -> dict:
        values = cls._read_data('rooms')
        random.shuffle(values)
        return {'rooms': '\n'.join(values[:5])}

    @classmethod
    def get_characteristics(cls) -> dict:
        characteristics = (
            'speciality',
            'health',
            'knowledge',
            'qualities',
            'hobbies',
            'phobias',
            'baggage',
            'fact',
        )

        data = {}
        for characteristic in characteristics:
            values = cls._read_data(characteristic)
            data[characteristic] = random.choice(values)

        return data

    @classmethod
    def _read_data(cls, data_type: str) -> list:
        path = os.path.join(os.path.dirname(__file__), cls.files[data_type])
        with open(path, 'r') as f:
            return json.load(f)
