import subprocess

def check_for_new_commits():
    # Загрузить информацию о новых коммитах
    subprocess.run(['git', 'fetch'])

    # Проверить разницу между локальной и удаленной ветками
    result = subprocess.run(['git', 'log', '--graph', '--pretty=format:%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset', '--abbrev-commit', '--date=relative', 'master..origin/master'], capture_output=True, text=True)

    # Проверить, есть ли новые коммиты
    if result.stdout:
        print("Есть новые коммиты:")
        print(result.stdout)
    else:
        print("Нет новых коммитов.")

if __name__ == "__main__":
    check_for_new_commits()

