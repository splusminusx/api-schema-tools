
## Site

### Описание типа
Site
Сайт.
Таблица 79. Поля сайта

Контроллер: Sites.

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|department_site_bindings|False|Array.<[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)>|Список связей сайта с отделами.<br/>|
|is_lead|True|None|Включение/выключение функциональности генератора лидов.<br/>|
|updated_at|True|None|Дата последнего обновления.<br/>|
|offline_form_settings|False|None|Настройки офлайн формы.<br/>DEPRECATED!<br/>|
|x_widget_settings|True|None|Настройки продукта «X-widget».<br/>|
|is_site_prechats|True|None|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|id|True|None|ID сайта.<br/>|
|call_label_settings|True|None|Настройки ярлыка звонка.<br/>DEPRECATED!<br/>|
|prechats_chat|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_comlaint|True|None|Включение/выключение жалоб.<br/>|
|hold_rule|False|None|Сценарий удержания.<br/>|
|is_mobile|True|None|Включение/выключение мобильного вида виджета.<br/>|
|widget_settings|True|None|Настройки виджета.<br/>|
|prechats_lead|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|complaint_email|False|None|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|is_hidden_offline|True|None|Скрывать ярлык, если сотрудники офлайн.<br/>|
|is_vote|True|None|Включение/выключение функциональности оценки чата посетителем.<br/>|
|chat_welcome_settings|True|None|Настройки окна приветствия.<br/>DEPRECATED!<br/>|
|call_settings|True|None|Звонковые настройки сайта.<br/>|
|chat_form_settings|True|None|Настройки ярлыка и окна чата.<br/>DEPRECATED!<br/>|
|is_deleted|True|None|Признак удаленного объекта.<br/>|
|url|True|None|Адрес сайта.<br/>|
|is_callback|True|None|Включение/выключение функциональности «Перезвоните мне».<br/>|
|employees|False|Array.<[Employee](/docs/types/Employee.md)>|Список сотрудников, связанных с данным сайтом.<br/>|
|lead_form_settings|False|None|Настройки формы генератора лидов.<br/>DEPRECATED!<br/>|
|is_managed|True|None|True, если сайт входит в число своих сайтов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|is_custom_buttons|True|None|Признак заказного дизайна кнопок.<br/>Если true, то изменение некоторых визуальных настроек кнопок чата и звонка может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|offline_mail_settings|True|None|Настройки офлайн почты.<br/>|
|callback_url|False|None|Настройка Callback URL.<br/>|
|created_at|True|None|Дата создания.<br/>|
