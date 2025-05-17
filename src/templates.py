SITUATION_TEMPLATE = """
<b>{situation_name}</b>

<b>Описание катастрофы:</b>
{situation_description}

<b>Особые правила:</b>
{rules}

<b>Помещения в бункере:</b>
{rooms}

<b>Время пребывания в бункере:</b>
{survival_time} лет

<b>Запасы продовольствия:</b>
Еда - {food_time} лет
Вода - {water_time} лет
Медикаменты - {medicine_time} лет
Оружие - {gun_time} лет

Необходимость в продолжении рода - {need_population}
"""

CHARACTERISTIC_TEMPLATE = """
<b>Ваша характеристика:</b>

Профессия:
{speciality}

Биология:
{gender} - {age} лет - {sex}

Состояние здоровья:
{health}

Знания и умения:
{knowledge}

Человеческие качества:
{qualities}

Хобби и увлечения:
{hobbies}

Фобии и слабости:
{phobias}

Багаж:
{baggage}

Факты:
{fact}

"""