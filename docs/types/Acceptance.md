
## Acceptance

### Описание типа
Акт.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invoice*|True|[Invoice](/types/Invoice)|Счет.<br/>|
|*service_name*|False|[string](/types/string)|Название услуги.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*number*|True|[numeric](/types/numeric)|Номер акта.<br/>|
|*amount*|True|[numeric](/types/numeric)|Сумма.<br/>|
|*file*|True|[file](/types/file)|Файл акта в формате PDF.<br/>|
|*file_signed*|False|[file](/types/file)|Файл акта, подписанного клиентом.<br/>Допустимые типы файлов: PDF, TIFF, JPEG, PNG, GIF.<br/>Максимальный размер файла – 10 MB.<br/>|
|*id*|True|[numeric](/types/numeric)|ID акта.<br/>|
