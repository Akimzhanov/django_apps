"""
queryset - запросы в базу данных по умолчанию запросы отправляются через переменную objects
objects - Manager, который в себе все методы для обращения с БД

Model.objects.all() - SELECT * FROM model
SELECT * FROM model LIMIT 2 - Model.objects.all()[:2]
SELECT * FROM model WHERE status='close' - Model.objects.filter(status='close')
SELECT * FROM model WHERE title LIKE/ILIKE 'название(либо букву)' - Publication.objects.filter(title__icontains='а')
Publication.objects.get(id=1) - SELECT * FROM publication WHERE id=1 - возвращает по id

Publication.objects.create(title='название1', image = None, status='open', user=u1) ->
INSERT INTO publication(title, image, status, user) VALUES (...) - создает 

q = Publication.objects.filter(status='close').update(status='open') ->
UPDATE publication SET status='open' WHERE status='close' - обнавляет

Publication.objects.filter(title='название1').delete() ->
DELETE FROM publication WHERE title='название1' - удаляет
"""