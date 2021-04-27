# Case-in, ЮФО, команда TeamRocket
## Платформа виртуальной адаптации удалённого сотрудника

**Требования**
- Python3 и модуль venv

```bash
sudo apt install -y python3-pip
sudo apt-get install python3-venv

```

**Подготовка к запуску**
В директории проекта выполнить
```bash
. prepare.sh

```

**Запуск отладочного сервера**
В директории проекта выполнить
```bash
python onboarding/manage.py runserver <IP>:<PORT>

```

пример:
```bash
sudo apt install -y python3-pip
sudo apt-get install python3-venv
. prepare.sh
python onboarding/manage.py runserver 0.0.0.0:8001

```
