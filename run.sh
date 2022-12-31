# Выбор установки для разных ОС
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  sudo apt install python3-pip portaudio19-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
  brew install python@3.8 python3.8-pip portaudio
else
  echo "Failed to determine the OS"
fi

# Установка python библиотек
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install poetry
poetry install

# Запуск
python main.py
