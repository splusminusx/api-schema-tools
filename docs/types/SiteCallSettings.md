
## SiteCallSettings

### Описание типа
SiteCallSettings
Звонковые настройки сайта.
Таблица 80. Поля звонковых настроек сайта


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|visitor_callerid_type|True|[string](/docs/types/string.md)|Выбор номера телефона, отображаемого посетителю при исходящем звонке.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>employee – номер, указанный в поле phone_forward_number сотрудника.<br/>custom – номер, указанный в настройке visitor_callerid_custom.<br/>|
|visitor_callerid_custom|False|[phone](/docs/types/phone.md)|Номер телефона, который будет отображаться посетителю при исходящем звонке при visitor_callerid_type=custom.<br/>Обязательно, если visitor_callerid_type=custom.<br/>|
|greeting_type|True|[string](/docs/types/string.md)|Типа мелодии приветствия.<br/>Приветствие проигрывается всем звонящим, перед соединением с оператором. Оператор отвечает только после того как мелодия полностью проиграется.<br/>Возможные значения:<br/>none – без приветствия (по умолчанию);<br/>custom – пользовательское приветствие.<br/>|
|employee_callerid_type|True|[string](/docs/types/string.md)|Выбор номера телефона, отображаемого оператору при вызове X-widget.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>visitor – номер, указанный посетителем при заказе звонка.<br/>|
|background_type|True|[string](/docs/types/string.md)|Тип фоновой мелодии.<br/>Фоновая мелодия проигрывается во время ожидания, пока кто-нибудь из операторов не ответит на звонок.<br/>Возможные значения:<br/>none – без фоновой мелодии;<br/>default – стандартная фоновая мелодия  (по умолчанию);<br/>custom – пользовательская фоновая мелодия.<br/>|
|background_custom|False|[file](/docs/types/file.md)|Пользовательская фоновая мелодия.<br/>Обязательно, если background_type=custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
|greeting_custom|False|[file](/docs/types/file.md)|Пользовательское приветствие.<br/>Обязательно, если greeting_type = custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
