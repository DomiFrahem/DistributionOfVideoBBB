# DistributionOfVideoBBB

Если вам просто скинуть с одного сервера на другой видео,<br />
то обратитесь сюда: https://docs.bigbluebutton.org/admin/customize.html#transfer-published-recordings-from-another-server
<br />
<br />
Этот скрипт преднозначен для разбиение видео на сервера, при условии если на сервере BBB был подключен Moodle
<br />
<br />
Установка:<br />
<br />
1 git clone https://github.com/DomiFrahem/DistributionOfVideoBBB.git<br />
2 cd DistributionOfVideoBBB<br />
3 pip install -r /path/to/requirements.txt<br />
<br />
<br />
По параметрам:
<br />
<br />
PATH_LIST_SERVER - путь к файлу JSON где храняться список серверов<br />
PATH_FROM - путь до директории с видео<br />
PATH_TO - путь куда будем скидывать видео<br />
Изменить их можно в main.py
<br />
<br />
Запуск:<br />
python ./main.py
<br />
<br />
После того как раскидаете видео по серверам<br />
(придеться делать это в ручную, либо зарание примонтируйте директории на разных серверах)<br />
Используйте команду на самом сервере:<br />
bbb-conf --setip bbb.domain.ru<br />
<br />
