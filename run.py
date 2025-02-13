import cmd

from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
    try:
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
    except Exception as e:
        print("Error load env: ", e)
        exit(0)

    cmd.run()
