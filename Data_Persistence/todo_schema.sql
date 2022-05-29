-- Схема для примеров приложения to-do
-- Проекты - это высокоуровневые операции, состоящие из задач
create table project (
	name	    text primary key,
	description text,
	deadline    date
);

-- Задачи - это шаги, которые должны быть выполнены
-- для завершения проекта
create table task (
	id	    integer primary key autoincrement not null,
	priority    integer default 1,
	details text,
	status text,
	deadline date,
	completed_on date,
	project text not null references project(name)
);
