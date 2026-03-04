"""
Генератор тестового лог-файла для Задачи 4.
Создаёт файл log.txt с различным количеством записей.
"""

from pathlib import Path
from datetime import datetime, timedelta
import random


def generate_log_file(
    filename: str = "log.txt",
    line_count: int = 50,
    error_ratio: float = 0.2,
) -> Path:
    """
    Генерирует тестовый лог-файл.

    Args:
        filename: Имя выходного файла
        line_count: Количество строк для генерации
        error_ratio: Доля строк с ошибками (0.0 - 1.0)

    Returns:
        Путь к созданному файлу
    """
    log_path = Path(filename)
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = {
        "INFO": [
            "Application started successfully",
            "User logged in",
            "Data loaded from database",
            "Cache cleared",
            "Configuration updated",
        ],
        "WARNING": [
            "High memory usage detected",
            "Slow query execution",
            "Deprecated API call",
            "Connection timeout retry",
            "Disk space running low",
        ],
        "ERROR": [
            "Database connection failed",
            "File not found",
            "Authentication error",
            "Null pointer exception",
            "Network timeout",
        ],
        "DEBUG": [
            "Variable x = 42",
            "Function called",
            "Loop iteration 5",
            "Memory allocated",
            "Request received",
        ],
    }

    base_time = datetime.now() - timedelta(hours=2)

    with log_path.open("w", encoding="utf-8") as file:
        for i in range(line_count):
            timestamp = base_time + timedelta(minutes=i * 2)
            time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            rand_value = random.random()
            if rand_value < error_ratio:
                level = "ERROR"
            elif rand_value < error_ratio + 0.15:
                level = "WARNING"
            elif rand_value < error_ratio + 0.25:
                level = "DEBUG"
            else:
                level = "INFO"

            message = random.choice(messages[level])
            line = f"[{level}] {time_str} - {message}\n"
            file.write(line)

    print(f"✅ Сгенерирован лог-файл: {log_path.absolute()}")
    print(f"   Строк: {line_count}, Ожидаемо ошибок: ~{int(line_count * error_ratio)}")
    return log_path


if __name__ == "__main__":
    generate_log_file()