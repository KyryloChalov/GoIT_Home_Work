import shutil


def prepare_folder() -> None:
    TEST_FOLDER = "D:\\000"
    SOURSE_FOLDER = "D:\\000_Original"
    print("*** PROCESSING MODE ***")
    shutil.rmtree(TEST_FOLDER, ignore_errors=True)
    p = input("press any key >>> ")  # пауза
    print("foldes prepearing... ")
    shutil.copytree(SOURSE_FOLDER, TEST_FOLDER)

prepare_folder()  # це для отладки
