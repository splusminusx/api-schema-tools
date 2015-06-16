## SiteChatSettings
### Описание типа
SiteChatSettings
Настройки продукта «Чат» уровня сайта.
Таблица 81. Поля настроек чата уровня сайта

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|offline_confirmation|True|string|Текст подтверждения в режиме офлайн. Отображается после успешной отправки запроса.<br/>Максимум 180 символов.<br/>|
|offline_contacts_required|False|string|Обязательность полей при offline_contacts=email_and_phone.<br/>Возможные значения:<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>|
|offline_welcome|True|string|Текст приветствия в режиме офлайн.<br/>Максимум 180 символов.<br/>|
|online_welcome|True|string|Текст приветствия в режиме онлайн.<br/>Максимум 180 символов.<br/>|
|offline_contacts|True|string|Запрашиваемые контактные данные в офлайн-режиме.<br/>Возможные значения:<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|