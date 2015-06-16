
## Acceptance

### Описание типа
Acceptance
Акт.
Таблица 9. Поля акта


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|invoice|True|None|Счет.<br/>|
|service_name|False|None|Название услуги.<br/>|
|created_at|True|None|Дата создания.<br/>|
|number|True|None|Номер акта.<br/>|
|amount|True|None|Сумма.<br/>|
|file|True|None|Файл акта в формате PDF.<br/>|
|file_signed|False|None|Файл акта, подписанного клиентом.<br/>Допустимые типы файлов: PDF, TIFF, JPEG, PNG, GIF.<br/>Максимальный размер файла – 10 MB.<br/>|
|id|True|None|ID акта.<br/>|
