import random
from abc import ABC, abstractmethod

from src.templates import SITUATION_TEMPLATE, CHARACTERISTIC_TEMPLATE
from data.data_getter import DataGetter


class AbstractMessageCreator(ABC):
    @classmethod
    def get_message(cls):
        data = cls._get_data()
        msg = cls.template.format(**data)
        return msg

    @classmethod
    @abstractmethod
    def _get_data(cls) -> dict:
        pass

    @property
    @abstractmethod
    def template(self) -> str:
        pass


class SituationMessageCreator(AbstractMessageCreator):
    template = SITUATION_TEMPLATE

    @classmethod
    def _get_data(cls):
        situation = DataGetter.get_situation()
        rules = DataGetter.get_rules()
        rooms = DataGetter.get_rooms()
        time_data = cls.__get_time_data()

        data = {
            'need_population': random.choice(("присутствует", "отсутствует")),
            **situation,
            **rules,
            **rooms,
            **time_data,
        }
        return data

    @classmethod
    def __get_time_data(cls):
        survival_time = random.randint(3, 30)
        keys = {
            'food_time',
            'water_time',
            'medicine_time',
            'gun_time',
        }
        year_from = int(survival_time / 3)
        data = {k: random.randint(year_from, survival_time) for k in keys}
        data['survival_time'] = survival_time
        return data


class CharacteristicMessageCreator(AbstractMessageCreator):
    template = CHARACTERISTIC_TEMPLATE

    @classmethod
    def _get_data(cls):
        bio = cls._get_biology_data()
        characteristics = DataGetter.get_characteristics()
        data = {
            **bio,
            **characteristics,
        }
        return data

    @classmethod
    def _get_biology_data(cls) -> dict:
        data = {
            'age': random.randint(14, 105),
            'gender': random.choice(("Мужчина", "Женщина")),
            'sex': random.choice(("гетеро", "гомо", "асексуал")),
        }
        return data
