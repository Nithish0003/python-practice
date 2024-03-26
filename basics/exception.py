def main_function():
    try:
        try:
            k=5//0
            print(k)
        except ZeroDivisionError as ze:
            print("error",ze)
    except KeyError as ke:
        print("Error message -----------> ",ke)
    except ZeroDivisionError as ze:
        print("Error message -----------> ",ze)
    else:
        print("No error")
    finally:
        print("Runs every time")
    # return
main_function()