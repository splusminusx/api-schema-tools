
## Site

### Описание типа
Site<br/>Сайт.<br/>Таблица 79. Поля сайта<br/><br/>Контроллер: Sites.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**department_site_bindings**|False|Array.<[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)>|Список связей сайта с отделами.<br/>|
|**is_lead**|True|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности генератора лидов.<br/>|
|**updated_at**|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|**offline_form_settings**|False|[OfflineFormSettings](/docs/types/OfflineFormSettings.md)|Настройки офлайн формы.<br/>DEPRECATED!<br/>|
|**x_widget_settings**|True|[SiteXWidgetSettings](/docs/types/SiteXWidgetSettings.md)|Настройки продукта «X-widget».<br/>|
|**is_site_prechats**|True|[boolean](/docs/types/boolean.md)|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|**call_label_settings**|True|[CallLabelSettings](/docs/types/CallLabelSettings.md)|Настройки ярлыка звонка.<br/>DEPRECATED!<br/>|
|**prechats_chat**|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|**is_comlaint**|True|[boolean](/docs/types/boolean.md)|Включение/выключение жалоб.<br/>|
|**hold_rule**|False|[HoldRule](/docs/types/HoldRule.md)|Сценарий удержания.<br/>|
|**is_mobile**|True|[boolean](/docs/types/boolean.md)|Включение/выключение мобильного вида виджета.<br/>|
|**widget_settings**|True|[SiteWidgetSettings](/docs/types/SiteWidgetSettings.md)|Настройки виджета.<br/>|
|**prechats_lead**|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|**complaint_email**|False|[email](/docs/types/email.md)|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|**is_hidden_offline**|True|[boolean](/docs/types/boolean.md)|Скрывать ярлык, если сотрудники офлайн.<br/>|
|**is_vote**|True|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности оценки чата посетителем.<br/>|
|**chat_welcome_settings**|True|[ChatWelcomeSettings](/docs/types/ChatWelcomeSettings.md)|Настройки окна приветствия.<br/>DEPRECATED!<br/>|
|**call_settings**|True|[SiteCallSettings](/docs/types/SiteCallSettings.md)|Звонковые настройки сайта.<br/>|
|**chat_form_settings**|True|[ChatFormSettings](/docs/types/ChatFormSettings.md)|Настройки ярлыка и окна чата.<br/>DEPRECATED!<br/>|
|**is_deleted**|True|[boolean](/docs/types/boolean.md)|Признак удаленного объекта.<br/>|
|**url**|True|[string](/docs/types/string.md)|Адрес сайта.<br/>|
|**is_callback**|True|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности «Перезвоните мне».<br/>|
|**employees**|False|Array.<[Employee](/docs/types/Employee.md)>|Список сотрудников, связанных с данным сайтом.<br/>|
|**lead_form_settings**|False|[LeadFormSettings](/docs/types/LeadFormSettings.md)|Настройки формы генератора лидов.<br/>DEPRECATED!<br/>|
|**is_managed**|True|[boolean](/docs/types/boolean.md)|True, если сайт входит в число своих сайтов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|**is_custom_buttons**|True|[boolean](/docs/types/boolean.md)|Признак заказного дизайна кнопок.<br/>Если true, то изменение некоторых визуальных настроек кнопок чата и звонка может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|**offline_mail_settings**|True|[OfflineMailSettings](/docs/types/OfflineMailSettings.md)|Настройки офлайн почты.<br/>|
|**callback_url**|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|**created_at**|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
