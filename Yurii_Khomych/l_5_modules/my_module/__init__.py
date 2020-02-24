print("We import my module")

print(f"Invoking __init__.py for {__name__}")
A = ["quux", "corge", "grault"]
__all__ = [
    "mod1",
]
# from my_module.mod1 import my_list


#
#
# if __name__ == '__main__':
#     pass
