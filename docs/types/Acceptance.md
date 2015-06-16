
## Acceptance

### Описание типа
Acceptance<br/>Акт.<br/>Таблица 9. Поля акта<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invoice*|True|[Invoice](/docs/types/Invoice.md)|Счет.<br/>|
|*service_name*|False|[string](/docs/types/string.md)|Название услуги.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*number*|True|[numeric](/docs/types/numeric.md)|Номер акта.<br/>|
|*amount*|True|[numeric](/docs/types/numeric.md)|Сумма.<br/>|
|*file*|True|[file](/docs/types/file.md)|Файл акта в формате PDF.<br/>|
|*file_signed*|False|[file](/docs/types/file.md)|Файл акта, подписанного клиентом.<br/>Допустимые типы файлов: PDF, TIFF, JPEG, PNG, GIF.<br/>Максимальный размер файла – 10 MB.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID акта.<br/>|
