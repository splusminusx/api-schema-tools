## Acceptance
### Описание типа
Acceptance
Акт.
Таблица 9. Поля акта

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|invoice|True|Invoice|Счет.<br/>|
|service_name|False|string|Название услуги.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|number|True|numeric|Номер акта.<br/>|
|amount|True|numeric|Сумма.<br/>|
|file|True|file|Файл акта в формате PDF.<br/>|
|file_signed|False|file|Файл акта, подписанного клиентом.<br/>Допустимые типы файлов: PDF, TIFF, JPEG, PNG, GIF.<br/>Максимальный размер файла – 10 MB.<br/>|
|id|True|numeric|ID акта.<br/>|
