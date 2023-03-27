# Клиент для сбора характеристик ПК на Windows

Клиент собирает характеристики ПК, а так же укороченный SMART. Характериситики ПК собираются с помощью утилиты WMI. SMART собирается с помощью CrystalDiskInfo.

## Дополнительные возможности.

Для данного клиента был написан Client Placer, с помощью которого можно установить данный клиент, а так же добавить его в автозапуск. (Client Placer можно скачать по ссылке снизу)

## Клиент без сервера не будет работать! (Сервер можно скачать по ссылке снизу)

Данные отправляются и принимаются в зашифрованном виде по шифровке AES в CBC моде. Для работы клиента необходимо настроить client.cfg, который генерируется после запуска приложения.

### Сервер для сбора данных: https://github.com/crystalvega/PCInfoParser-Server
### Client Placer: https://github.com/crystalvega/PCInfoParser-Client-Placer
