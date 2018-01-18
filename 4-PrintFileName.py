import string
file_path = "/var/log/mysql/misc/mysqld.log"
search_string = "/"
last_search_index = file_path.rfind(search_string)
last_search_index = last_search_index + 1

file_name = file_path[ last_search_index: ]
print(file_name)
