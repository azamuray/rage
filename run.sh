# Выбор установки для разных ОС
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  sudo apt install python3-pip portaudio19-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
  brew install python3-pip
  brew install portaudio
else
  echo "Failed to determine the OS"
fi

# Установка python библиотек
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# Запуск
python3 main.py
