flushdb:
	psql -U webadmin teamstarter < schema/drop.sql
	psql -U webadmin teamstarter < schema/create.sql
